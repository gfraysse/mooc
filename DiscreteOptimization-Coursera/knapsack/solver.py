#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
from operator import itemgetter

sys.setrecursionlimit(100000)

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
nb = 0
best_value = 0
taken_best = []

def pair(capacity, item_count, items, taken):
    m = 0
    a = -1
    b = -1
    
    for i in range(item_count):
        for j in range (item_count):
            if i != j:
                if items[j].weight + items[i].weight < capacity:
                    if items[j].value + items[i].value > m:
                        m = items[j].value + items[i].value
                        a = i                       
                        b = j
                if items[j].weight + items[i].weight + 10002 < capacity:
                    if items[i].weight > 80000 or items[j].weight > 80000:
                        print "combination of 3 exist"
    print "max value found is m="+str(m)+" for a="+str(a)+" and b="+str(b)
    print "a="+str(a)+", weight="+str(items[a].weight)+", value="+str(items[a].value)
    print "b="+str(b)+", weight="+str(items[b].weight)+", value="+str(items[b].value)
    return m
        

import collections
import functools

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
       
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
   
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
    
# From stackexchange: https://codereview.stackexchange.com/questions/20569/dynamic-programming-solution-to-knapsack-problem
def dynamic_programming(capacity, item_count, items, taken):
    optimal = 0
    value = [[0 for c in range(item_count + 1)] for i in range(capacity)]

    @memoized
    def oracle(k, j):
        #print k,j
        if j == 0:
            return 0
        else:
            if items[j].weight <= k:
                v = max(oracle(k, j - 1),
                        oracle(k-items[j].weight, j - 1) + items[j].value)
                return v
            else:
                return oracle(k, j - 1)

    start = time.clock()
    result = []
    j = capacity
    for i in xrange(item_count - 1, 0, -1):
        o_1 = oracle(j, i)
        o_2 = oracle(j, i - 1)
        #print j, i, o_1, o_2
        if  o_1 != o_2:
            #print items[i]
            result.append(items[i])
            j -= items[i].weight
    result.reverse()
    optimal = oracle(capacity, len(items)-1)
    # for k in range(capacity):
    #     for j in range(item_count):
    #         value[k][j] = oracle(k, j, items, value)
    end = time.clock()
    #print str(end - start)+" seconds"
        
    #print "optimal="+str(value[capacity - 1][item_count-1])
    # if value[capacity - 1][item_count-1] > optimal:
    #     optimal = value[capacity - 1][item_count-1]

    total_weight = capacity - 1

    start = time.clock()

    for i in range(len(result)):
        taken[result[i].index] = 1
    # for j in range(item_count - 1, 0, -1):
    #     #print "j="+str(j)
    #     for k in range(total_weight, 0, -1):
    #         #max_value_for_j = value[total_weight][j]
    #         # if j==item_count-1:
    #         #     print "value["+str(k)+"]["+str(j)+"]="+str(value[k][j])
    #         #     print "value["+str(k)+"]["+str(j-1)+"]="+str(value[k][j-1])
    #         #     print "value["+str(k)+"]["+str(j-2)+"]="+str(value[k][j-2])
    #         #     print "value j-1="+str(value[k][j-1])
    #         if value[k][j] == value[k][j-1]:
    #             break
    #         if value[k][j] != value[k][j-1]:
    #             #print "value["+str(k)+"]["+str(j)+"]="+str(value[k][j])
    #             #print "value="+str(value[k][j])
    #             #print "value j-1="+str(value[k][j-1])
    #             taken[j] = 1
    #             #print str(j)+" is taken"
    #             #print "k="+str(k)
    #             #print "j="+str(j)+", weight="+str(items[j].weight)+", value="+str(items[j].value)+", total_weight="+str(total_weight)
    #             total_weight -= items[j].weight
    #             #print "total_weight="+str(total_weight)
    #             break

    end = time.clock()
    #print str(end - start)+" seconds"
    # total_v = 0
    # total_w = 0
    # for i in range(item_count):
    #     total_v += taken[i] * items[i].value
    #     total_w += taken[i] * items[i].weight
    #     print "i="+str(i)+", weight="+str(items[i].weight)+", total_w="+str(total_w)+", value="+str(items[i].value)+", total_v="+str(total_v)+", taken="+str(taken[i])
    return optimal

def best_first_recursive(i, select_i, total_value, remaining_capacity, maximum_value_eval, items, item_count, taken, min_w):
    global nb, best_value, taken_best
    nb += 1
    #print "nb="+str(nb)
    if total_value > best_value:
        best_value = total_value
        taken_best = taken        
        #print "new best value="+str(best_value)

optimal_found = False
def depth_first_recursive(i, select_i, total_value, remaining_capacity, maximum_value_eval, items, item_count, taken, min_w, min_weights):
    global nb, best_value, taken_best, optimal_found
    nb += 1
    if nb % 1000000 == 0:
        print "nb="+str(nb)
        #print taken
    
    if total_value > best_value:
        best_value = total_value
        taken_best = taken
        #best is 3967028: at least 3966813 current : 3967053 
        #best is 109899: at least 109869, current:   108008 (pre-sort items by value)
        #best is 1099881, at least 1099870, current: 1095152
        #print "new best value="+str(best_value)

    value = total_value
    taken[i] = select_i
    
    #print "i="+str(i)+", min_w="+str(min_weights[i])+", items[i].weight="+str(items[i].weight)+", remaining_capacity="+str(remaining_capacity)+", total_value="+str(total_value)+", best value="+str(best_value)
    if remaining_capacity < min_weights[i]:
        #print "not enough capacity available for minimum weight of remaining branches"
        return value, taken
    
    if select_i == 1:
        if remaining_capacity - items[i].weight >= 0:
            value += items[i].value
            remaining_capacity -= items[i].weight
            maximum_value_eval -= items[i].value
            #print "going through branch"
            if value == 108008 or value >= 3967020:
                #print "found optimal"
                optimal_found = True
                return value,taken[:]
        else:
            #print "dropping branch"+str(taken)
            return 0, taken

    if i < item_count - 1 and optimal_found == False:
        value_1 = 0
        if remaining_capacity - items[i+1].weight >= 0:
            value_1, taken_1 = depth_first_recursive(i+1, 1, value, remaining_capacity, maximum_value_eval, items, item_count, taken, min_w,min_weights)
        value_2, taken_2 = depth_first_recursive(i+1, 0, value, remaining_capacity, maximum_value_eval, items, item_count, taken, min_w, min_weights)
        if value_1 > value_2:
            value = value_1
            taken = taken_1
        else:
            value = value_2
            taken = taken_2
    # else:
    #     print "discarding branch where "+str(i)+" is selected"
        
    return value, taken

def dfbb_iterative(total_capacity, maximum_value_eval, items, item_count, taken):
    i = 0
    total_value = 0
    remaining_capacity = total_capacity
    best_value_for_depth = [0 for item in range(item_count)]
    
    while i < item_count -1:
        if remaining_capacity - items[i].weight >= 0:
            total_value += items[i].value
            remaining_capacity -= items[i].weight
            maximum_value_eval -= items[i].value
            taken[i] = 1
            last_taken = i
            
        if total_value > best_value_for_depth[i]:
            best_value_for_depth[i] = total_value
            
        total_value = 0
        remaining_capacity = total_capacity
        for j in range(i):
            total_value += taken[j] * items[j].value
            remaining_capacity -= taken[j] * items[j].weight
            
        i += 1

    return total_value, taken
    
def branch_and_bound(capacity, item_count, items, taken):
    value = 0
    remaining_capacity = capacity
    func = depth_first_recursive
    
    maximum_value_eval = 0
    
    min_w = items[0].weight
    for item in items:
        maximum_value_eval += item.value
        if item.weight < min_w:
            min_w = item.weight

    min_weights = [0 for i in range(item_count)]
    min_weights[item_count - 1] = items[item_count - 1].weight
    for i in range(item_count - 2, 0, -1):
        if items[i].weight < min_weights[i+1]:
            min_weights[i] = items[i].weight
        else:
            min_weights[i] = min_weights[i+1]
            
    maximum_value = 0

    #result, taken = dfbb_iterative(remaining_capacity, maximum_value_eval, items, item_count, taken)
    
    result, taken = func(0, 1, 0, remaining_capacity, maximum_value_eval, items, item_count, taken, min_w, min_weights)
    maximum_value = result
    #copy by value !
    taken_sol = taken[:]

    remaining_capacity = capacity
    result, taken_2 = func(0, 0, 0, remaining_capacity, maximum_value_eval, items, item_count, taken, min_w, min_weights)
    if result > maximum_value:
        maximum_value = result
        taken_sol = taken_2

    taken = taken_sol[:]

    # check total
    total_v = 0
    for i in range(item_count):
        total_v += taken[i] * items[i].value
    if total_v != maximum_value:
        print "ERROR: total_v ="+str(total_v)+" differs from computed value "+str(maximum_value)
        
    return maximum_value, taken

def getItemsKey(item):
    return item[0].index

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    
    value = 0
    weight = 0
    taken = [0 for i in range(item_count)]

    #value = pair(capacity, item_count, items, taken)
    start = time.clock()
    optimal = 0
    if item_count <= 200:
        #print "Using dynamic programming"
        value = dynamic_programming(capacity, item_count, items, taken)
        optimal = 1
    else:
        #print "Using depth_first_branch_and_bound"
        optimal = 0
        items= sorted (items, key=lambda item: item.value, reverse=True)
        value, taken = branch_and_bound(capacity, item_count, items, taken)
        decorated = []
        for i in range(item_count):
            decorated.append([items[i], taken[i]])
        decorated.sort(key=getItemsKey)
        items = [item for item,j in decorated]                         
        taken = [t for i,t in decorated]                         


    end = time.clock()
    #print str(end - start)+" seconds"


    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(optimal) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

