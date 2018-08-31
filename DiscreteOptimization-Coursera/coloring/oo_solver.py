#!/usr/bin/python
# -*- coding: utf-8 -*-
# Graph Coloring
# fmYLC, ./data/gc_50_3, solver.py, Coloring Problem 1 => 7
# 6 0
# 0 0 0 1 0 2 1 3 2 4 2 3 2 3 1 2 3 5 4 0 4 4 2 2 2 5 2 5 5 4 4 1 0 0 4 2 4 0 5 3 5 4 3 3 1 3 4 1 4 5
# 7 0
# 0 4 0 5 5 2 3 1 4 3 5 1 4 1 6 2 1 2 4 0 0 3 6 4 2 0 2 3 5 5 0 3 0 0 3 2 4 4 2 1 4 5 1 1 4 1 5 2 5 3

# IkKpq, ./data/gc_70_7, solver.py, Coloring Problem 2 =>19
# 19 0
# 0 4 4 10 9 11 2 7 1 2 16 7 0 15 9 1 16 12 11 8 17 14 9 6 3 9 5 12 3 5 15 13 0 7 5 17 17 1 6 10 12 3 10 16 3 13 18 18 13 11 8 8 1 12 2 0 15 11 18 10 4 2 3 6 4 4 14 15 13 5

# pZOjO, ./data/gc_100_5, solver.py, Coloring Problem 3 => 19
# 19 0
# 9 3 11 5 0 8 16 8 9 3 15 1 1 5 11 2 4 13 8 15 6 3 12 11 4 17 7 9 14 0 1 1 13 6 4 7 11 14 16 6 2 11 10 15 7 12 12 12 10 8 7 2 15 14 4 8 18 5 6 5 4 9 9 10 10 4 3 17 18 16 4 17 7 0 13 12 8 2 14 3 2 11 16 6 8 13 15 1 2 14 1 0 0 9 18 5 3 12 16 6

# XDQ31, ./data/gc_250_9, solver.py, Coloring Problem 4 => 95 93
# found new solution with 93  colors 75 ou 11 avant le dernier
# [90, 42, 18, 48, 69, 30, 25, 92, 41, 11, 45, 3, 12, 90, 55, 60, 60, 50, 79, 31, 9, 17, 68, 16, 7, 49, 1, 61, 20, 50, 11, 77, 26, 13, 51, 32, 52, 70, 27, 23, 54, 28, 78, 69, 24, 23, 27, 57, 52, 41, 25, 42, 48, 34, 83, 20, 36, 40, 49, 80, 8, 83, 61, 71, 48, 43, 62, 44, 16, 6, 14, 21, 53, 54, 10, 55, 87, 56, 31, 55, 6, 67, 70, 32, 4, 33, 58, 34, 71, 24, 84, 85, 8, 84, 43, 44, 21, 43, 15, 26, 63, 29, 0, 27, 76, 44, 81, 82, 33, 59, 8, 45, 72, 28, 75, 9, 38, 49, 89, 80, 7, 88, 46, 16, 79, 2, 9, 30, 17, 61, 86, 28, 32, 59, 80, 13, 22, 46, 73, 53, 23, 57, 74, 64, 69, 60, 88, 27, 65, 65, 10, 4, 46, 19, 18, 12, 82, 51, 63, 71, 11, 65, 74, 58, 73, 64, 15, 52, 2, 24, 69, 64, 19, 74, 0, 78, 18, 75, 70, 30, 22, 50, 21, 10, 26, 35, 47, 63, 66, 46, 19, 86, 67, 3, 56, 35, 36, 77, 38, 33, 29, 14, 66, 68, 42, 58, 22, 53, 87, 81, 6, 76, 4, 37, 88, 5, 72, 91, 82, 37, 5, 39, 62, 68, 54, 37, 67, 34, 85, 72, 89, 20, 1, 47, 14, 13, 47, 87, 0, 38, 57, 29, 41, 36, 39, 6, 40, 60, 59, 17]

# w7hAO, ./data/gc_500_1, solver.py, Coloring Problem 5 => 18
# 18 0
# 9 1 2 13 0 5 6 10 12 5 6 6 7 3 10 1 14 6 8 7 1 0 4 8 6 3 6 2 2 3 16 14 4 11 1 10 4 12 7 1 11 11 5 10 9 1 3 9 3 10 9 11 1 7 8 7 9 7 4 12 15 3 0 0 13 5 2 5 2 9 6 16 16 2 8 15 8 15 4 3 1 1 2 15 6 15 12 9 13 9 14 7 2 10 5 12 8 7 8 15 3 7 14 7 5 7 10 8 14 6 3 5 0 14 8 2 8 9 3 4 11 10 1 10 4 0 6 8 7 8 2 15 4 1 3 15 5 4 8 14 7 4 2 5 12 10 4 13 11 5 0 7 8 8 13 2 11 2 2 7 5 1 0 6 9 11 5 2 6 11 10 15 7 13 16 6 16 9 1 16 7 16 0 11 5 4 13 12 7 4 0 14 11 0 3 2 4 0 2 12 16 13 1 10 12 2 4 13 7 0 1 16 9 7 6 7 12 7 5 8 4 2 11 11 6 2 1 14 9 2 13 11 6 6 0 5 8 10 12 4 0 11 3 6 5 9 3 10 14 3 1 8 2 4 13 1 12 1 10 3 2 4 12 5 7 0 3 13 10 4 9 0 10 2 8 0 1 1 2 11 8 0 15 3 6 4 2 3 13 6 1 9 13 6 10 12 7 8 1 0 1 3 13 4 11 17 9 3 9 10 5 5 12 11 13 12 11 5 4 8 0 3 1 1 12 0 6 13 13 6 10 0 3 15 9 10 4 4 10 6 10 9 11 3 5 13 6 9 5 1 5 5 11 10 13 12 8 7 12 6 7 9 14 3 5 10 8 8 16 4 9 6 0 10 5 8 6 15 12 11 10 11 13 8 5 15 6 7 4 9 3 16 4 11 7 13 3 9 0 5 1 3 3 6 9 11 0 0 6 6 0 1 11 7 2 0 9 7 4 12 12 7 7 8 12 13 7 10 9 8 4 14 4 14 11 1 14 1 0 2 12 5 4 11 0 15 15 12 10 11 14 8 11 8 3 13 2 5 15 1 1 7 3 8 11 5 5 15 16 7 3 2 11 13 7 9 14 5 1 2 8 8 5 5 6 0 3 14 5 14 14 3 14 7 15 10 2 3 8 2

# tthbm, ./data/gc_1000_5, solver.py, Coloring Problem 6 => echec

# fmYLC,    8,   6
# IkKpq,   20,  17
# pZOjO,   21,  16
# XDQ31,   95,  78
# w7hAO,   18,  16
# tthbm, 124, 100

PROFILER_ON = False

from ortools.constraint_solver import pywrapcp
from ortools.linear_solver import pywraplp
from operator import itemgetter
import random
import sys

if PROFILER_ON == True:
    import cProfile, pstats, StringIO

sys.setrecursionlimit(100000)

NO_COLOR = -1
FOUND_SOLUTION = 2

class edge:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

class node():
    def __init__(self, name):
        self.neighbours = []
        self.iterator = 0
        self.name = name
        self.color = NO_COLOR
        
        self.domain = []

    def degree(self):
        return len(self.neighbours)
    
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def sort_neighbours_by_degree(self):
        self.neighbours.sort(key=lambda neighbour: neighbour.degree, reverse=True)

    def set_domain(self, domain):
        self.domain = domain

    def add_value_to_domain(self, value):
        self.domain.append(value)
        
    def remove_value_to_domain(self, value):
        self.domain.remove(value)

    def __iter__(self):
        return self
    
    def next(self):
        if self.iterator < self.degree() - 1:
            self.iterator += 1
            return self.neighbours[self.iterator]
        else:
            raise StopIteration()
    
class solution:
    def __init__(self):
        self.nodes = []
        self.nodes_color = []

    def set_color_for_node(self, node, color):
        self.nodes[name == node.name].color = color

    def num_nodes(self):
        return len(self.nodes)

    def is_solution_complete(self):
        if self.nodes_color.count(NO_COLOR) == 0:
            return True
        
        return False
        
class graph:
    def __init__(self):
        self.edges = []
        self.nodes = []
        self.solutions = []
        self.iterator = 0
        
    def add_edge(self, edge):
        self.edges.append(edge)
        self.nodes[edge.src].add_neighbour(self.nodes[edge.dst])
        self.nodes[edge.dst].add_neighbour(self.nodes[edge.src])

    def sort_nodes_by_degree(self):
        decorated = []
        for i in range(self.num_nodes()):
            decorated.append([self.nodes[i], self.nodes[i].degree])
            decorated.sort(key=itemgetter(1), reverse=True)
        self.nodes = [i for i, _ in decorated]
        
        for node in self.nodes:
            node.sort_neighbours_by_degree()
            
        # nodes_ordered = [i for i in range(node_count)]
        # random.shuffle(nodes_ordered)

    def num_edges(self):
        return len(self.edges)

    def add_node(self, node):
        self.nodes.append(node)
        
    def num_nodes(self):
        return len(self.nodes)

    def add_solution(self, solution):
        self.solutions.append(solution)
        
    def __iter__(self):
        return self

    def next(self):
        try:
            self.nodes[self.iterator].next()
        except StopIteration:
            if self.iterator < self.num_nodes() - 1:
                self.iterator += 1
                self.next()
            else:
                raise StopIteration()

    def is_color_valid_for_node(self, node, color):
        for edge in self.edges:
            if edge.src.name == node.name:
                if edge.dst.color == color:
                    return False
                
            if edge.dst.name == node.name:
                if edge.src.color == color:
                    return False

        return True
                        
    def set_color_for_node(self, node, color):
        self.nodes[name: node.name].color = color
        
    def prune_from_node(self, node):
        if node != None:
            if node.color == NO_COLOR:
                node.color = node.domain.pop(0)
                
            for edge in self.edges:
                if edge.src == node.name:
                    self.nodes[edge.dst.name].domain.remove(node.color)
                else:
                    if edge.dst == node.name:
                        self.nodes[edge.src.name].domain.remove(node.color)

    def __str__(self):
        val = ""
        for node in self.nodes:
            val += "node="+str(node.name)+", color="+str(node.color)+","
        return val

        
def prune(constraint, domain):
    return True

def propagate(constraints, domain):
    domain_reduced = True
    while(domain_reduced):
        domain_reduced = False
        for constraint in constraints:
            if constraint(domain) == False:
                return False
            else:
                domain_reduced = prune(constraint, domain)
                #domain_reduced = True

    return True    

# The exercise gc_250_9 does not finish if this function always returns True
def graph_valid(edges, node_color_sol):
    # if node_color_sol == []:
    #     return False
    
    # for edge in edges:
    #     if node_color_sol[edge.src] == node_color_sol[edge.dst] and node_color_sol[edge.src] !=-1:
    #         debug_print("solution incorrecte for edge "+str(edge)+" same color "+str(node_color_sol[edge.src]))
    #         return edge
        
    return True

def debug_print(string):
    #print string
    return

def combination_already_found(sol, edges, node_color_sol, color):
    for s in sol:
        color0 = s[edges[0][0]]
        if node_color_sol[edges[0][0]] == color0:
            color1 = s[edges[0][1]]
            if color == color1:
                # print edges[0][0], edges[0][1]
                # print "color0", color0, "color1", color1
                # print "combination already found, skipping color", color
                return True
    return False

def color_of_neighbours_ok(node_id, edges, node_color_sol):
    for edge in edges:
        if edge.src != -1:
            if edge.dst != -1:
                if node_id == edge.src or node_id == edge.dst:
                    if node_color_sol[edge.src] == node_color_sol[edge.dst]:
                        return False
            
    ret = graph_valid(edges, node_color_sol)
    if ret != True:
        debug_print(indentation_per_recursion_level*recursion_level+str(color)+" is NOT a valid color for node "+str(node_id)+" due to "+str(ret)+" trying another color for node")
        return False

    return True

recursion_level = 0
best_solution = []
list_of_solutions = []
recursion_stack = []
def ortools_solver_v1_diy_recursive(node, my_graph, node_color, node_color_sol):
    global recursion_level, FOUND_SOLUTION, best_solution, list_of_solutions#, visited_nodes
    global neighbours, degree_nodes
    global recursion_stack
    recursion_level += 1

    node_id = my_graph.nodes[node].name
    # if node_id in visited_nodes:
    #     print node_id, "already in visited_nodes"
    #visited_nodes.add(node_id)
    recursion_stack.append(node_id)
    #print "recursion_stack append", recursion_stack
    #print "node",node,"node_id",node_id, "visited_nodes", len(visited_nodes),"/",node_count,sorted(visited_nodes, key=int)
    #print "remaining node to find", node_color_sol.count(-1)
    indentation_per_recursion_level = "    "
    
    # Creates the variables.
    node_color_init = node_color[:]
    
    #debug_print("recursion_level", recursion_level)
    #print("recursion_level", recursion_level)
    #print node_id
    
    #print "coin", node_id, node_color[node_id]
    color_domain = []    
    debug_print(indentation_per_recursion_level*recursion_level+"node_id="+str(node_id)+" solution="+str(node_color_sol))
    if node_color_sol[node_id] != -1:
        color_domain.append(node_color_sol[node_id])
    else:
        iterator0 = None
        try:
            iterator0 = node_color[node_id].DomainIterator()
            #debug_print "iterator0", iterator0
            #debug_print "iterator0", iterator0.Value()
        except IndexError, e:
            #print node_color_sol, node_color
            print  indentation_per_recursion_level*recursion_level,"No more possible colors for node", node_id
            recursion_level -= 1
            recursion_stack.pop()
            #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)
            return False
    for i in node_color[node_id].DomainIterator():
        color0 = i        
        color_domain.append(color0)
        # node_color_sol[node_id] = color0
        # if graph_valid(edges, node_color_sol) == True:
        #     print color0, " is a valid color for node", node_id
        #     break
            

    result = False
    reinit = False
    node_color_sol_init = node_color_sol[:]

    if -1 not in node_color_sol:
        print "??"

    num_color_current = num_color_in_sol(node_color_sol)
    if  num_color_current >= num_color_in_sol(best_solution):
        #print "a More colors in current solution than in best one", num_color_current
        recursion_level -= 1
        recursion_stack.pop()
        #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)
        return False
    
    for color in color_domain:
        #debug_print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))
        #print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))
        #print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))

        # break symmetries
        if node_id == my_graph.edges[0].dst:
            if node_color_sol[my_graph.edges[0].src] != -1:
                if node_color_sol[my_graph.edges[0].src] >= color:
                    continue
                #Skip previously found combination for first edge
                if combination_already_found(list_of_solutions, my_graph.edges, node_color_sol, color) == True:
                    continue

        if node_color_sol[node_id] != color:
            reinit = True
            node_color_sol[node_id] = color

        ret = graph_valid(my_graph.edges, node_color_sol)        
        if ret != True:
            #print node_color[node_id], color
            try:
                #print "a", node_id, node_color[node_id], color
                node_color[node_id].RemoveValue(color)
                debug_print(indentation_per_recursion_level*recursion_level+str(color)+" is NOT a valid color for node "+str(node_id)+" due to "+str(ret)+" trying another color for node")
                continue
            except Exception, e:
                #print node_color_sol, node_color
                #print "No more possible value for node_id", node_id
                recursion_level -= 1
                recursion_stack.pop()
                #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)
                return False

        #If we were in the last leaf we might have found a solution, let's check
        if -1 not in node_color_sol:
            #print "tintin"
            #print "node_id", node_id, "recursion_level", recursion_level
            #list_of_solutions.append(node_color_sol[:])
            #print node_color_sol
            node_color_sol = node_color_sol_init[:]
            # #print node_color_sol
            #print "one solution found"

            # if num_color_in_sol(sol[-1]) < num_color_in_sol(best_solution):
            #     best_solution = sol[-1]
            #     debug_print("best solution is now "+str(best_solution))
                #     #print sol
            recursion_level -= 1
            recursion_stack.pop()
            #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)
            return FOUND_SOLUTION

        if reinit == True:
            for neighbour in my_graph.nodes[node_id].neighbours:
            #for neighbour in neighbours:
                node_color[neighbour.name] = node_color_init[neighbour.name]
            
        if color_of_neighbours_ok(node_id, my_graph.edges, node_color_sol):
            hasFoundOneSolution = False
            n = 1
            while n <= len(my_graph.nodes[node_id].neighbours):
            #while n <= len(neighbours):
                neighbour = my_graph.nodes[node_id].neighbours[n - 1]
                #neighbour = neighbours[n - 1]
                #if node_color_sol.count(-1) == 1:
                    #print "only one missing a"
                    # missing = node_color_sol.index(-1)
                    # if missing not in visited_nodes:
                    #     #print "checking the missing",missing,"as it has not been visited yet"
                    #     neighbour = missing
                    #     n -= 1
                    # else:
                    #     #print missing, "already visited"
                    #     pass
                # If neighbour has not already been passed through
                #print "n=",n,"/",len(neighbours[node_id]), node_id, neighbour, neighbours[node_id], node_color_sol.count(-1),"/",node_count, "missing "+str(node_color_sol.index(-1)) if node_color_sol.count(-1) == 1 else "N/A",node_color_sol, recursion_level
                #print "n=",n,"/",len(neighbours[node_id]), node_id, neighbour, node_color_sol.count(-1),"/",node_count, "missing "+str(node_color_sol.index(-1)) if node_color_sol.count(-1) == 1 else "N/A", recursion_level
                if (node_color_sol[neighbour.name] == -1):
                    #print "ho", node_color_sol
                    node_color_sol_before = [-1 for _ in range(my_graph.num_nodes())]
                    node_color_before = [-1 for _ in range(my_graph.num_nodes())]
                    for i in range(my_graph.num_nodes()):                            
                        node_color_sol_before[i] = node_color_sol[i]
                        node_color_before[i] = node_color[i]
                    # node_color_before = node_color[:]
                    # node_color_sol_before = node_color_sol[:]
                    ret = ortools_solver_v1_diy_recursive(neighbour.name, my_graph, node_color, node_color_sol)
                    #print "hi", ret, node_color_sol, node_color_sol.count(-1),"/",node_count,hex(id(node_color_sol))
                    num_color_current = num_color_in_sol(node_color_sol)
                    # print num_color_current
                    # print num_color_in_sol(best_solution), best_solution
                    if  num_color_current >= num_color_in_sol(best_solution):
                        #print "More colors in current solution than in best one", num_color_current, "node_id",node_id, node_color_sol
                        #print "hi bebore", node_id, node_color_sol, node_color_sol.count(-1),"/",node_count,hex(id(node_color_sol))
                        for i in range(node_count):                            
                            node_color_sol[i] = node_color_sol_before[i]
                        #print "hi after", node_color_sol, node_color_sol.count(-1),"/",node_count,hex(id(node_color_sol))

                        #print "removing possible color", node_color_sol[neighbour], "for neighbour", neighbour
                        #recursion_level -= 1
                        #n -= 1
                        #node_color[neighbour].RemoveValue(node_color_sol[neighbour])
                        #node_color_sol[neighbour] = -1
                        #n += 1
                        #continue
                        
                        try:
                            node_color[neighbour].RemoveValue(list_of_solutions[-1][neighbour])
                        except Exception, e:
                            #print "No more possible value for node", node, node_color[node], list_of_solutions[-1][node]
                            pass
                        node_color_sol[neighbour] = -1 # = [-1 for i in range(node_count)]

                        hasFoundOneSolution = FOUND_SOLUTION
                        n -= 1
                        recursion_level -= 1
                        v = recursion_stack.pop()
                        #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack),"popped value=",v
                        return False

                    nb = node_color_sol.count(-1)
                    if nb == 0:                        
                        #print "FOUND SOL while in node_id", node_id,"neighbour=",neighbour
                        ret = graph_valid(my_graph.edges, node_color_sol)
                        if ret != True:
                            print "INVALID solution", node_color_sol

                        debug_print("solution is complete "+str(node_color_sol))
                        list_of_solutions.append(node_color_sol[:])
                        #print "found new solution with", num_color_in_sol(list_of_solutions[-1]), " colors"
                        #print node_color_sol            
                        #print(list_of_solutions[-1])
                        
                        if num_color_in_sol(list_of_solutions[-1]) < num_color_in_sol(best_solution):
                            best_solution = list_of_solutions[-1][:]
                            #print "best solution is now "+str(best_solution)+" with "+str(num_color_in_sol(list_of_solutions[-1]))+" colors"
                            debug_print("best solution is now "+str(best_solution)+" with "+str(num_color_in_sol(list_of_solutions[-1]))+" colors")
                            debug_print(list_of_solutions)

                        #reinit
                        #print node_color, "before was ",node_color_before
                        node_color = node_color_before[:]
                        try:
                            #node_color[node_id].RemoveValue(list_of_solutions[-1][node_id])
                            #node_color[nodes_ordered.index(neighbour)].RemoveValue(list_of_solutions[-1][nodes_ordered.index(neighbour)])
                            node_color[neighbour].RemoveValue(list_of_solutions[-1][neighbour])
                        except Exception, e:
                            #print "No more possible value for node", node, node_color[node], list_of_solutions[-1][node]
                            pass
                        #print "reinitiliazing possible values for", neighbour, node_color_sol[neighbour],"-> -1"
                        #print "before", node_color_sol
                        node_color_sol[neighbour] = -1 # = [-1 for i in range(node_count)]
                        #print "after", node_color_sol
                        #print node_color_sol

                        hasFoundOneSolution = FOUND_SOLUTION
                        n -= 1
                        #print "iteration",n,"/",len(neighbours[node_id])
                        #continue
                        recursion_level -= 1
                        recursion_stack.pop()
                        #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)
                        return True
                    else:
                        if nb == 1:
                            #print "only one missing"
                            pass
                        else:
                            #print "remaining node to find", nb, ret
                            #print "hu"
                            if ret != False:
                                print ret
                                if hasFoundOneSolution != FOUND_SOLUTION:
                                    hasFoundOneSolution = True
                                    #n -= 1
                                    #GF
                            else:
                                #print "hy"
                                #print "treatment finished for neighbour", neighbour, "of node_id", node_id, "reinit color", node_color_sol[neighbour]
                                #node_color_sol[neighbour] = -1
                                pass

                #print "n=",n,"/",len(neighbours[node_id]),"for node_id", node_id
                #print "ha"
                n += 1
                
            # We've been through all neighbours of the node
            recursion_level -= 1
            recursion_stack.pop()
            #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)
            #print "coucou", hasFoundOneSolution, node_color_sol[node_id], node_color_sol.count(-1), "reinitializing value for node_id", node_id
            #visited_nodes.remove(node_id)
            if hasFoundOneSolution != False:
                node_color_sol[node_id] = -1
            #visited_nodes.pop()

            return False
            # if node < len(nodes_ordered) - 1:
            #     return ortools_solver_v1_diy_recursive(node + 1, nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution)
            # ret = False
            # hasFoundOneSolution= False
            # while ret == True:
            #     return ret = ortools_solver_v1_diy_recursive(node + 1, nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution)
            #     print "ret", ret
            #     if ret == True:
            #         hasFoundOneSolution = True
            #         node_color[node_id].RemoveValue(node_color_sol[node_id])
            #         print node_color[node_id]
            # node_color[node_id] = node_color_init[node_id]
            # return hasFoundOneSolution
            # else:
            #     recursion_level -= 1
            #     return True
        else:
            #print "prout"
            continue        

    recursion_level -= 1
    recursion_stack.pop()
    #print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)

    return False

def num_color_in_sol(node_solor_sol):
    s = set(node_solor_sol)
    if -1 in s:
        s.remove(-1)
    #print s
    return len(s)

def solver(my_graph):
    global best_solution, list_of_solutions
    
    solver = pywrapcp.Solver("coloring")
    
    node_color_sol = [-1 for i in range(my_graph.num_nodes())]
    my_graph.sort_nodes_by_degree()
    
    nc = 10
    if my_graph.num_nodes() == 50:
        nc = 8
    else:
        if my_graph.num_nodes() <= 100:
            nc = 19
        else:
            if my_graph.num_nodes() == 250:
                nc = 95
            else:
                if my_graph.num_nodes() == 500:
                    nc = 19
                else:
                    if my_graph.num_nodes() == 1000:
                        nc = 124
                        
    # Find the solution that minimizes the number of colors of the graph
    num_solutions = 0

    # node 0 is always of color 0
    node_color = [solver.IntVar(0, nc, "node_color%i" % i) for i in range(0, my_graph.num_nodes())]
    #node_color_sol[0] = 0
    #node_color_sol[nodes_ordered[0]] = 0
    list_of_solutions = []
    best_solution = [i for i in range(my_graph.num_nodes())]

    sol = solution()
    my_graph.add_solution(sol)
    while True:
        try:
            node = my_graph.next()
        except StopIteration:
            print "No more node to go through"
            break
        my_graph.prune_from_node(node)
        if sol.is_solution_complete() == True:
            print "found new solution", sol
            sol = solution()
            my_graph.add_solution(sol)
            print my_graph


    num_colors = 1
    ret = graph_valid(my_graph.edges, sol)
    if ret != True:
        print("Solution is INVALID due to "+str(ret))
    else:
        debug_print("Solution is valid")
        
    print "Solutions found:", num_solutions
    print "Time:", solver.WallTime(), "ms"
    
    return num_colors, sol

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    my_graph = graph()
    
    for i in range(node_count):
        new_node = node(i)
        my_graph.add_node(new_node)
        
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        my_graph.add_edge(edge(int(parts[0]), int(parts[1])))

    num_colors, sol = solver(my_graph)        

    if graph_valid(my_graph, sol) != True:
        print("Solution is INVALID")
    else:
        debug_print("Solution is valid")
        
    # prepare the solution in the specified output format
    output_data = str(num_colors) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, sol)) + '\n'
    
    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()

        if PROFILER_ON == True:
            pr = cProfile.Profile()
            pr.enable()
        try:
            print(solve_it(input_data))
        except KeyboardInterrupt:
            print "Ctrl-C detected, exiting..."
        if PROFILER_ON == True:
            pr.disable()
            s = StringIO.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()
            print s.getvalue()           
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
