#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

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
        
def oracle(k, j, items, value):
    if j == 0:
        return 0
    else:
        if items[j].weight <= k:
            v = max(value[k][j - 1], items[j].value + value[k - items[j].weight][j - 1])
            #print v
            return v
        else:
            return value[k][j - 1]

def dynamic_programming(capacity, item_count, items, taken):
    optimal = 0
    value = [[0 for c in range(item_count + 1)] for i in range(capacity)]
        
    for k in range(capacity):
        for j in range(item_count):
            value[k][j] = oracle(k, j, items, value)
            
    #print "optimal="+str(value[capacity - 1][item_count-1])
    if value[capacity - 1][item_count-1] > optimal:
        optimal = value[capacity - 1][item_count-1]

    total_weight = capacity - 1
    for j in range(item_count - 1, 0, -1):
        #print "j="+str(j)
        for k in range(total_weight, 0, -1):
            #max_value_for_j = value[total_weight][j]
            # if j==item_count-1:
            #     print "value["+str(k)+"]["+str(j)+"]="+str(value[k][j])
            #     print "value["+str(k)+"]["+str(j-1)+"]="+str(value[k][j-1])
            #     print "value["+str(k)+"]["+str(j-2)+"]="+str(value[k][j-2])
            #     print "value j-1="+str(value[k][j-1])
            if value[k][j] == value[k][j-1]:
                break
            if value[k][j] != value[k][j-1]:
                #print "value["+str(k)+"]["+str(j)+"]="+str(value[k][j])
                #print "value="+str(value[k][j])
                #print "value j-1="+str(value[k][j-1])
                taken[j] = 1
                #print str(j)+" is taken"
                #print "k="+str(k)
                #print "j="+str(j)+", weight="+str(items[j].weight)+", value="+str(items[j].value)+", total_weight="+str(total_weight)
                total_weight -= items[j].weight
                #print "total_weight="+str(total_weight)
                break

    # total_v = 0
    # total_w = 0
    # for i in range(item_count):
    #     total_v += taken[i] * items[i].value
    #     total_w += taken[i] * items[i].weight
    #     print "i="+str(i)+", weight="+str(items[i].weight)+", total_w="+str(total_w)+", value="+str(items[i].value)+", total_v="+str(total_v)+", taken="+str(taken[i])
    return optimal

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

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0 for i in range(item_count)]

    #value = pair(capacity, item_count, items, taken)
    value = dynamic_programming(capacity, item_count, items, taken)
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
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

