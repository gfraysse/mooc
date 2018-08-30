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

from ortools.constraint_solver import pywrapcp
from ortools.linear_solver import pywraplp
from operator import itemgetter
import random
import sys

sys.setrecursionlimit(100000)
FOUND_SOLUTION = 2

# https://github.com/google/or-tools/blob/master/examples/python/coloring_ip.py
def ortools_alternate_solver(node_count, edge_count, edges):
    solver = pywrapcp.Solver("coloring")
    # x[i,c] = 1 means that node i is assigned color c
    nc = 10
    #x = {}
    x = [0 for _ in range(nc*node_count)]

    for v in range(node_count):
        for j in range(nc):
            #x[v, j] = solver.IntVar(0, 1, 'v[%i,%i]' % (v, j))
            #x[nc*v+j] = solver.IntVar(0, 1, 'v[%i]' % (nc*v+j))
            x[nc*v+j] = solver.IntVar(0, 1, 'v[%i,%i]' % (v, j))
            #print nc*v+j

    #print x
    # u[c] = 1 means that color c is used, i.e. assigned to some node
    u = [solver.IntVar(0, 1, 'u[%i]' % i) for i in range(nc)]

    # number of colors used, to minimize
    solver.Add(solver.Sum(u) >= 2)
    obj = solver.Sum(u)

    #
    # constraints
    #
    
    # each node must be assigned exactly one color
    for i in range(node_count):
        #solver.Add(solver.Sum([x[i, c] for c in range(nc)]) == 1)
        solver.Add(solver.Sum(x[c] for c in range(i*nc,(i+1)*nc)) == 1)

    # adjacent nodes cannot be assigned the same color
    # (and adjust to 0-based)
    for i in range(edge_count):
        for c in range(nc):
            #a = x[edges[i][0], c]
            a = x[edges[i][0]*nc + c]
            #b = x[edges[i][1], c]
            b = x[edges[i][1]*nc + c]
            print "edge:"+str(edges[i])+" a="+str(a)+" b="+str(b)+" u["+str(c)+"]="+str(u[c])
            solver.Add(a + b <= u[c])

    # objective
    objective = solver.Minimize(obj, 1)

    db = solver.Phase(x,
                      solver.CHOOSE_FIRST_UNBOUND,
                      solver.ASSIGN_RANDOM_VALUE)

    collector = solver.LastSolutionCollector()
    collector.AddObjective(obj)
    #
    # solution
    #
    solver.Solve(db,[objective, collector])
    
    #print 'number of colors:', int(solver.Objective().Value())
    #print 'colors used:', [int(u[i].Value()) for i in range(nc)]

    # for v in range(node_count):
    #     print 'v%i' % v, ' color '
    #     for c in range(nc):
    #         if int(x[v, c].Value()) == 1:
    #             print(c)

    # Iterates through the solutions, displaying each.
    num_solutions = 0
    num_colors = 0
    solution = []
    while solver.NextSolution():
        solution = []
        print x

        # Displays the solution just computed.
        for v in range(node_count):
            for c in range(nc):
                #print(node_color[i].Value())
                #if num_solutions == 0:
                solution.append(x[v, c].Value())
                
        num_colors = max(solution)+1
        num_solutions += 1
                #print num_colors, solution

    solver.EndSearch()
    print "Solutions found:", num_solutions
    print "Time:", solver.WallTime(), "ms"
    
    return num_colors, solution

# https://github.com/google/or-tools/blob/master/examples/python/coloring_ip.py
def ortools_linear_solver(node_count, edge_count, edges):
    solver = pywraplp.Solver('CoinsGridGLPK',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # x[i,c] = 1 means that node i is assigned color c
    nc = 10
    x = {}

    for v in range(node_count):
        for j in range(nc):
            x[v, j] = solver.IntVar(0, 1, 'v[%i,%i]' % (v, j))
            #print nc*v+j

    #print x
    # u[c] = 1 means that color c is used, i.e. assigned to some node
    u = [solver.IntVar(0, 1, 'u[%i]' % i) for i in range(nc)]

    # number of colors used, to minimize
    solver.Add(solver.Sum(u) >= 2)
    obj = solver.Sum(u)

    #
    # constraints
    #
    
    # each node must be assigned exactly one color
    for i in range(node_count):
        solver.Add(solver.Sum([x[i, c] for c in range(nc)]) == 1)

    # adjacent nodes cannot be assigned the same color
    # (and adjust to 0-based)
    for i in range(edge_count):
        for c in range(nc):
            a = x[edges[i][0], c]
            b = x[edges[i][1], c]
            solver.Add(a + b <= u[c])

    # objective
    objective = solver.Minimize(obj)

    #
    # solution
    #
    solver.Solve()
    num_colors = int(solver.Objective().Value())
    print 'number of colors:'+str(num_colors)
    print 'colors used:'+ str([int(u[i].SolutionValue()) for i in range(nc)])

    solution = []
    for v in range(node_count):
        #print 'v%i' % v, ' color '
        for c in range(nc):
            if int(x[v, c].SolutionValue()) == 1:
                solution.append(c)
                #print(c)

    print "Time:", solver.WallTime(), "ms"
    
    return num_colors, solution

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
    
#GF TODO
def ortools_diy_solver(node_count, edge_count, edges):
    degree_nodes = [0 for _ in range(node_count)] 
    neighbours = [[] for _ in range(node_count)]
    for e in range(edge_count):
        neighbours[edges[e][0]].append(edges[e][1])
        neighbours[edges[e][1]].append(edges[e][0])
    for i in range(len(neighbours)):
        degree_nodes[i] += len(neighbours[i])
    #print "degree", degree_nodes

    nodes_unordered = [i for i in range(node_count)]
    decorated = []
    for i in range(node_count):
        decorated.append([nodes_unordered[i], degree_nodes[i]])
    decorated.sort(key=itemgetter(1), reverse=True)
    nodes_ordered = [i for i, _ in decorated]                         

    #print  "nodes_ordered", nodes_ordered
    # Creates the variables.
    nc = 10
    node_color = [0 for _ in range(nc * node_count)]

    # reification of the constraint node_color[v*nc+c] is 0 or 1 whether node v is of color c
    for v in nodes_ordered:
        for c in range(nc):
            node_color[nc * v + c] = solver.IntVar(0, 1, 'v[%i,%i]' % (v, c))
            #print nc*v+j

    # each node must be assigned exactly one color
    for i in nodes_ordered:
        constraint = solver.Sum(node_color[c] for c in range(i * nc,(i + 1) * nc)) == 1
        solver.Add(constraint)
        
    # u[c] = 1 means that color c is used, i.e. assigned to some node
    u = [solver.IntVar(0, 1, 'u[%i]' % i) for i in range(nc)]

    # Creates the constraints.    
    edge_origin_color = [0 for _ in range(edge_count)]
    edge_destination_color = [0 for _ in range(edge_count)]
    for e in range(edge_count):
        a_total = 0 
        b_total = 0 
        for c in range(nc):
            a = node_color[edges[e][0] * nc + c]
            b = node_color[edges[e][1] * nc + c]
            a_total += a * (10**c)
            b_total += b * (10**c)
            #print a,b
            solver.Add(a + b <= u[c])
            #solver.Add(a + b <= 1)
        #print e, a_total, b_total
        edge_origin_color[e] = a_total
        edge_destination_color[e] = b_total
        constraint = edge_origin_color[e] != edge_destination_color[e] 
        solver.Add(constraint)
        #print constraint.DebugString()

    # To reduce symmetry, consider an order on the first two vertices
    first_edge_vertex = edges[0][0]
    first_edge_vertex_neighbour = neighbours[0][0]
    #print first_edge_vertex, first_edge_vertex_neighbour
    full_color_node_1 = 0
    full_color_node_2 = 0
    full_color_1 = 0
    full_color_2 = 0
    for c in range(nc):
        full_color_node_1 += node_color[0 * nc +c] * (10**c)
        full_color_node_2 += node_color[1 * nc +c] * (10**c)
        full_color_1 += node_color[first_edge_vertex * nc +c] * (10**c)
        full_color_2 += node_color[first_edge_vertex_neighbour * nc +c] * (10**c)
    #print full_color_1, full_color_2
    solver.Add(full_color_1 < full_color_2)
    solver.Add(full_color_node_1 <= full_color_node_2)

    colored_items = [0 for _ in range(nc)]
    for c in range(nc):
        for v in nodes_ordered:
            colored_items[c] += node_color[nc * v + c]

    nb_colors_used = solver.Sum(colored_items[c] != 0 for c in range(nc))
        
    # Find the solution that minimizes the number of colors of the graph
    obj_var = nb_colors_used
    solver.Add(obj_var > 1)
    solver.Add(obj_var < max(degree_nodes))
    objective_monitor = solver.Minimize(obj_var, 1)



def ortools_solver_v2(node_count, edge_count, edges):
    solver = pywrapcp.Solver("coloring")
    
    degree_nodes = [0 for _ in range(node_count)]
    neighbours = [[] for _ in range(node_count)]
    for e in range(edge_count):
        neighbours[edges[e][0]].append(edges[e][1]) #solver.IntVar(edge[1],edge[1]))
        neighbours[edges[e][1]].append(edges[e][0]) #solver.IntVar(edge[0],edge[0]))
    for i in range(len(neighbours)):
        degree_nodes[i] += len(neighbours[i])

    #print "degree", degree_nodes

    nodes_unordered = [i for i in range(node_count)]
    decorated = []
    for i in range(node_count):
        decorated.append([nodes_unordered[i], degree_nodes[i]])
    decorated.sort(key=itemgetter(1), reverse=True)
    nodes_ordered = [i for i, _ in decorated]                         

    #print  "nodes_ordered", nodes_ordered
    # Creates the variables.    
    #nodes = [solver.IntVar(0, node_count - 1, "node%i" % i) for i in nodes_ordered]
    nc = 10
    node_color = [0 for _ in range(nc * node_count)]

    # reification of the constraint node_color[v*nc+c] is 0 or 1 whether node v is of color c
    for v in nodes_ordered:
        for c in range(nc):
            node_color[nc * v + c] = solver.IntVar(0, 1, 'v[%i,%i]' % (v, c))
            #print nc*v+j

    # each node must be assigned exactly one color
    for i in nodes_ordered:
        constraint = solver.Sum(node_color[c] for c in range(i * nc,(i + 1) * nc)) == 1
        solver.Add(constraint)
        
    # u[c] = 1 means that color c is used, i.e. assigned to some node
    u = [solver.IntVar(0, 1, 'u[%i]' % i) for i in range(nc)]

    #lb_color_total_nodes = [0 for _ in range(node_count)] # number of nodes for each color lower bound
    #ub_color_total_nodes = [node_count for _ in range(node_count)] # number of nodes for each color upper bound
    
    # Creates the constraints.    
    edge_origin_color = [0 for _ in range(edge_count)]
    edge_destination_color = [0 for _ in range(edge_count)]
    for e in range(edge_count):
        # neighbours[edges[e][0]].append(edges[e][1]) #solver.IntVar(edge[1],edge[1]))
        # neighbours[edges[e][1]].append(edges[e][0]) #solver.IntVar(edge[0],edge[0]))

        a_total = 0 
        b_total = 0 
        for c in range(nc):
            a = node_color[edges[e][0] * nc + c]
            b = node_color[edges[e][1] * nc + c]
            a_total += a * (10**c)
            b_total += b * (10**c)
            #print a,b
            solver.Add(a + b <= u[c])
            #solver.Add(a + b <= 1)
        #print e, a_total, b_total
        edge_origin_color[e] = a_total
        edge_destination_color[e] = b_total
        constraint = edge_origin_color[e] != edge_destination_color[e] 
        solver.Add(constraint)
        #print constraint.DebugString()

    # To reduce symmetry, consider an order on the first two vertices
    first_edge_vertex = edges[0][0]
    first_edge_vertex_neighbour = neighbours[0][0]
    #print first_edge_vertex, first_edge_vertex_neighbour
    full_color_node_1 = 0
    full_color_node_2 = 0
    full_color_1 = 0
    full_color_2 = 0
    for c in range(nc):
        full_color_node_1 += node_color[0 * nc +c] * (10**c)
        full_color_node_2 += node_color[1 * nc +c] * (10**c)
        full_color_1 += node_color[first_edge_vertex * nc +c] * (10**c)
        full_color_2 += node_color[first_edge_vertex_neighbour * nc +c] * (10**c)
    #print full_color_1, full_color_2
    solver.Add(full_color_1 < full_color_2)
    solver.Add(full_color_node_1 <= full_color_node_2)

    colored_items = [0 for _ in range(nc)]
    for c in range(nc):
        for v in nodes_ordered:
            colored_items[c] += node_color[nc * v + c]

    nb_colors_used = solver.Sum(colored_items[c] != 0 for c in range(nc))
    #print nb_colors_used
    #print colored_items
    # for i in range(len(neighbours)):
    #     degree_nodes[i] += len(neighbours[i])
        #ub_color_total_nodes[i] -= len(neighbours[i])
        #print i, neighbours[i], lb_color_total_nodes[i],  ub_color_total_nodes[i]

    # for i in range(node_count):
    #     solver.Add(lb_color_total_nodes[i] < ub_color_total_nodes[i])
    #     solver.Add(solver.Sum[i] < ub_color_total_nodes[i])
    #     solver.Add(solver.Sum[i] > lb_color_total_nodes[i])
    # Absurd neighbors of a node can be of the same color...
    # for n in neighbours:
    #     print n
        #solver.Add(solver.AllDifferent(n))
        
    # Find the solution that minimizes the number of colors of the graph
    obj_var = nb_colors_used
    solver.Add(obj_var > 1)
    solver.Add(obj_var < max(degree_nodes))
    objective_monitor = solver.Minimize(obj_var, 1)
                               
    db = solver.Phase(node_color,
                      solver.CHOOSE_FIRST_UNBOUND,
                      solver.ASSIGN_MAX_VALUE)
    
    collector = solver.FirstSolutionCollector()

    solution = []
    # Add the interesting variables to the SolutionCollector.
    collector.Add(node_color)
    collector.AddObjective(obj_var)
    
    solver.NewSearch(db, [objective_monitor, collector])
    
    # Iterates through the solutions, displaying each.
    num_solutions = 0
    num_colors = 0
    while solver.NextSolution():
        print "Time:", solver.WallTime(), "ms"
        solution = []

        #print nb_colors_used.Var().Value()
        #print full_color_1.Var().Value(), full_color_2.Var().Value()
        #print a_total.Var().Value(), b_total.Var().Value()
        # for e in range(edge_count):
        #     print e, edges[e][0], edge_origin_color[e].Var().Value(), edges[e][1], edge_destination_color[e].Var().Value()
        #print u
        # Displays the solution just computed.
        #print "nodes", nodes
        #for v in nodes_ordered:
        for v in range(node_count):
            #print "nodes", nodes[v].Value()
            for c in range(nc):
                #print v,c, node_color[nc * v + c]
                if node_color[nc * v + c].Value() == 1:
                    #print(node_color[i].Value())
                    #if num_solutions == 0:
                    solution.append(c)

        num_colors = nb_colors_used.Var().Value() #max(solution)-min(solution)+1
        num_solutions += 1
        print num_colors, solution

    solver.EndSearch()
    print "Solutions found:", num_solutions
    print "Time:", solver.WallTime(), "ms"
    
    return num_colors, solution

def graph_valid(edges, node_color_sol):
    if node_color_sol == []:
        return False
    
    for edge in edges:
        if node_color_sol[edge[0]] == node_color_sol[edge[1]] and node_color_sol[edge[0]] !=-1:
            debug_print("solution incorrecte for edge "+str(edge)+" same color "+str(node_color_sol[edge[0]]))
            return edge
        
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

recursion_level = 0
def ortools_solver_v1_diy_recursive_old(node_id, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution):
    global recursion_level, FOUND_SOLUTION
    recursion_level += 1

    #print "remaining node to find", node_color_sol.count(-1)
    indentation_per_recursion_level = "    "
    
    # Creates the variables.
    node_color_init = node_color[:]
    #degree_nodes = [0 for _ in range(node_count)]
    neighbours = [[] for _ in range(node_count)]
    for e in range(edge_count):
        neighbours[edges[e][0]].append(edges[e][1]) #solver.IntVar(edge[1],edge[1]))
        #neighbours[edges[e][1]].append(edges[e][0]) #solver.IntVar(edge[0],edge[0]))

    #debug_print("neighbours", neighbours)
    #debug_print("recursion_level", recursion_level)

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
        
    for color in color_domain:
        debug_print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))
        #print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))
        #print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))

        # break symmetries
        if node_id == edges[0][1]:
            if node_color_sol[edges[0][0]] != -1:
                if node_color_sol[edges[0][0]] >= color:
                    continue
                #Skip previously found combination for first edge
                if combination_already_found(sol, edges, node_color_sol, color) == True:
                    continue

        if node_color_sol[node_id] != color:
            reinit = True
            node_color_sol[node_id] = color
        ret = graph_valid(edges, node_color_sol)
        
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
                return False

        #If we were in the last leaf we might have found a solution, let's check
        if -1 not in node_color_sol:
            #print "tintin"
            #print "node_id", node_id, "recursion_level", recursion_level
            #sol.append(node_color_sol[:])
            #print node_color_sol
            node_color_sol = node_color_sol_init[:]
            # #print node_color_sol
            # print "one solution found"

            # if num_color_in_sol(sol[-1]) < num_color_in_sol(best_solution):
            #     best_solution = sol[-1]
            #     debug_print("best solution is now "+str(best_solution))
                #     #print sol
            recursion_level -= 1
            return FOUND_SOLUTION

        if reinit == True:
            for neighbour in neighbours[node_id]:
                node_color[neighbour] = node_color_init[neighbour]
            
        if neighbours[node_id] != []:
            for neighbour in neighbours[node_id]:
                if node_color_sol[neighbour] == -1:
                    debug_print(indentation_per_recursion_level*recursion_level+"considering neighbour "+str(neighbour)+" for node "+str(node_id))
                    result = ortools_solver_v1_diy_recursive(neighbour, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution)

                    if result == FOUND_SOLUTION:
                        print "yeeeeeeeeeeeeeees"
                        
                    if result == False:
                        debug_print(indentation_per_recursion_level*recursion_level+"Invalid solution, trying another color for node"+str(node_id))
                        #try:
                            #if neighbour == 9:
                            #    print "b", neighbour, node_color[neighbour], color
                            #node_color[neighbour].RemoveValue(color)
                        #except Exception, e:
                        #    print "No more possible solution for node", neighbour, node_color[neighbour], color
                        break
                    ret = graph_valid(edges, node_color_sol)
                    if ret != True:
                        debug_print(indentation_per_recursion_level*recursion_level+str(color)+" is NOT a valid color for node "+str(node_id)+" due to "+str(ret)+" trying another color for node")
                        result = False
                        break

            # #GF TO FIX to compute multiple solutions
            # if -1 not in node_color_sol:
            #     #print node_color_sol
            #     # print color, node_id
            #     # print "tintin"
            #     sol.append(node_color_sol[:])
            #     print node_color_sol
            #     node_color_sol = node_color_sol_init[:]
            #     #print node_color_sol
            #     print "one solution found"
            #     if num_color_in_sol(sol[-1]) < num_color_in_sol(best_solution):
            #         best_solution = sol[-1]
            #         debug_print("best solution is now "+str(best_solution))
            #         #print sol
            #     continue

            if result == False:
                debug_print(indentation_per_recursion_level*recursion_level+str(color)+" is NOT a valid color for node "+str(node_id)+" trying another color for node")
                #print node_id, node_color[node_id], color
                try:
                    # if node_id == 9:
                    #     print "c", node_id, node_color[node_id], color
                    node_color[node_id].RemoveValue(color)
                except Exception, e:
                    #print "No more possible values for node_id", node_id
                    pass
                break                
                
        else:
            debug_print("node "+str(node_id)+" has no neighbour")
            #print("node "+str(node_id)+" has no neighbour")
            recursion_level -= 1
            return True
        
        if result == True:
            #print(str(color)+" is a valid color for node "+str(node_id))
            recursion_level -= 1
            return True           

    # print indentation_per_recursion_level*recursion_level, "node",node_id, "color0", color0, "neighbours", neighbours[node_id]

    # ret = False
    # for neighbour in neighbours[node_id]:
    #     print indentation_per_recursion_level*recursion_level, "  neighbour", neighbour
    #     if node_color_sol[node_id] != -1 and node_color_sol[neighbour] != -1:
    #         print indentation_per_recursion_level*recursion_level, "  colors already found, going through next neighbour"
    #         if node_color_sol[node_id] != node_color_sol[neighbour]:
    #             print "haha"
    #             continue
    #         else:
    #             recursion_level -= 1
    #             print "bb"
    #             return False
            
    #     if node_color_sol[neighbour] == -1:
    #         print indentation_per_recursion_level*recursion_level, "looking for a color for node", neighbour
    #         iterator1 = None
    #         try:
    #             iterator1 = node_color[neighbour].DomainIterator()                
    #         except IndexError, e:
    #             print e
    #             print  indentation_per_recursion_level*recursion_level,"No more adjacent vertex for node", node_id
    #             return True
    #         for j in node_color[neighbour].DomainIterator():                        
    #             color1 = j
    #             print indentation_per_recursion_level*recursion_level, " testing color for node",node_id, "color0", color0, "neighbour", neighbour, "color1", color1
    #             if color1 == color0:
    #                 print "  ==", color0, " not a possible value"
    #                 node_color[neighbour].RemoveValue(color1)
    #                 print indentation_per_recursion_level*recursion_level, "********* neighbour", neighbour, node_color[neighbour]
    #             else:
    #                 node_color_sol[neighbour] = color1
    #                 if graph_valid(edges, node_color_sol) == True:
    #                     print indentation_per_recursion_level*recursion_level, " valid color for", neighbour, "node_color_sol1", node_color_sol
    #                     if neighbours[neighbour] != []:
    #                         ret = ortools_solver_v1_diy_recursive(neighbour, node_count, edge_count, edges, node_color, node_color_sol)
    #                         if ret != False:
    #                             #recursion_level -= 1
    #                             #return False
    #                             break
    #                     else:
    #                         return True
    #     else:
    #         print "dd"

    # if ret == False:
    #     print "cc"
    #     return False
    # else:
    #     print node_id, node_color[node_id], color0
    #     #node_color[node_id].RemoveValue(color0)
    #     print indentation_per_recursion_level*recursion_level, "node_id", node_id, node_color[node_id]
    #     print "tata"
    #     recursion_level -= 1

    #print best_solution
    #print "toto", result
    # if -1 not in node_color_sol:
    #     print("solution is complete "+str(node_color_sol)+" recursion_level "+str(recursion_level)+" for node_id "+str(node_id))
    #     #print sol[-1]
    #     recursion_level -= 1
    #     return FOUND_SOLUTION

    recursion_level -= 1
    return False

def color_of_neighbours_ok(node_id, edges, node_color_sol):
    for edge in edges:
        if edge[0] != -1:
            if edge[1] != -1:
                if node_id == edge[0] or node_id == edge[1]:
                    if node_color_sol[edge[0]] == node_color_sol[edge[1]]:
                        return False
            
    ret = graph_valid(edges, node_color_sol)
    if ret != True:
        debug_print(indentation_per_recursion_level*recursion_level+str(color)+" is NOT a valid color for node "+str(node_id)+" due to "+str(ret)+" trying another color for node")
        return False

    return True

best_solution = []
list_of_solutions = []
visited_nodes = set([])
recursion_stack = []
def ortools_solver_v1_diy_recursive(node, nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol):
    global recursion_level, FOUND_SOLUTION, best_solution, list_of_solutions, visited_nodes
    global recursion_stack
    recursion_level += 1

    node_id = nodes_ordered[node]
    # if node_id in visited_nodes:
    #     print node_id, "already in visited_nodes"
    visited_nodes.add(node_id)
    recursion_stack.append(node_id)
    #print "recursion_stack append", recursion_stack
    #print "node",node,"node_id",node_id, "visited_nodes", len(visited_nodes),"/",node_count,sorted(visited_nodes, key=int)
    #print "remaining node to find", node_color_sol.count(-1)
    indentation_per_recursion_level = "    "
    
    # Creates the variables.
    node_color_init = node_color[:]
    neighbours = [[] for _ in range(node_count)]
    for e in range(edge_count):
        neighbours[edges[e][0]].append(edges[e][1])
        neighbours[edges[e][1]].append(edges[e][0])

    # Sort neighbours by degrees (number of adjacent nodes)
    degree_nodes = [0 for _ in range(node_count)]
    for i in range(len(neighbours)):
        #debug_print("neighbours of node #"+str(i)+" are "+str(neighbours[i]))
        degree_nodes[i] += len(neighbours[i])
        #print "degree of node",i,"is",degree_nodes[i]

    #print("neighbours"+str(neighbours))
    neighbours_unordered = [i for i in range(node_count)]
    for n in range(len(neighbours)):
        decorated = []
        #print n,neighbours[n]
        for i in range(len(neighbours[n])):
            decorated.append([neighbours[n][i], degree_nodes[neighbours[n][i]]])
        decorated.sort(key=itemgetter(1), reverse=True)
        neighbours[n] = [i for i, _ in decorated]                         
        #print n,neighbours[n]

    #print("neighbours"+str(neighbours))
    #print("neighbours"+str(neighbours[node_id]))
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
        if node_id == edges[0][1]:
            if node_color_sol[edges[0][0]] != -1:
                if node_color_sol[edges[0][0]] >= color:
                    continue
                #Skip previously found combination for first edge
                if combination_already_found(list_of_solutions, edges, node_color_sol, color) == True:
                    continue

        if node_color_sol[node_id] != color:
            reinit = True
            node_color_sol[node_id] = color

        ret = graph_valid(edges, node_color_sol)        
        if ret != True:
            #print node_color[node_id], color
            try:
                #print "a", node_id, node_color[node_id], color
                node_color[node_id].RemoveValue(color)
                debug_print(indentation_per_recursion_level*recursion_level+str(color)+" is NOT a valid color for node "+str(node_id)+" due to "+str(ret)+" trying another color for node")
                continue
            except Exception, e:
                #print node_color_sol, node_color
                print "No more possible value for node_id", node_id
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
            for neighbour in neighbours[node_id]:
                node_color[neighbour] = node_color_init[neighbour]
            
        if color_of_neighbours_ok(node_id, edges, node_color_sol):
            hasFoundOneSolution = False
            n = 1
            while n <= len(neighbours[node_id]):
                neighbour = neighbours[node_id][n - 1]
                if node_color_sol.count(-1) == 1:
                    #print "only one missing a"
                    missing = node_color_sol.index(-1)
                    if missing not in visited_nodes:
                        #print "checking the missing",missing,"as it has not been visited yet"
                        neighbour = missing
                        n -= 1
                    else:
                        #print missing, "already visited"
                        pass
                # If neighbour has not already been passed through
                #print "n=",n,"/",len(neighbours[node_id]), node_id, neighbour, neighbours[node_id], node_color_sol.count(-1),"/",node_count, "missing "+str(node_color_sol.index(-1)) if node_color_sol.count(-1) == 1 else "N/A",node_color_sol, recursion_level
                if (node_color_sol[neighbour] == -1):
                    #print "ho", node_color_sol
                    node_color_sol_before = [-1 for _ in range(node_count)]
                    node_color_before = [-1 for _ in range(node_count)]
                    for i in range(node_count):                            
                        node_color_sol_before[i] = node_color_sol[i]
                        node_color_before[i] = node_color[i]
                    # node_color_before = node_color[:]
                    # node_color_sol_before = node_color_sol[:]
                    ret = ortools_solver_v1_diy_recursive(nodes_ordered.index(neighbour), nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol)
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
                        ret = graph_valid(edges, node_color_sol)
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
            visited_nodes.remove(node_id)
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

    print "pouet"
    recursion_level -= 1
    recursion_stack.pop()
    print "recursion_stack pop   ", recursion_stack,"len=",len(recursion_stack)

    return False

def ortools_solver_v1_diy_recursive_greedy(node, nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol):
    global recursion_level, FOUND_SOLUTION, best_solution, list_of_solutions, visited_nodes
    global recursion_stack
    recursion_level += 1

    node_id = nodes_ordered[node]
    #print "node",node,"node_id",node_id
    #print "remaining node to find", node_color_sol.count(-1)
    indentation_per_recursion_level = "    "
    
    # Creates the variables.
    node_color_init = node_color[:]
    neighbours = [[] for _ in range(node_count)]
    for e in range(edge_count):
        neighbours[edges[e][0]].append(edges[e][1])
        neighbours[edges[e][1]].append(edges[e][0])

    #print("neighbours"+str(neighbours))
    #print("neighbours"+str(neighbours[node_id]))
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
        
    if num_color_in_sol(node_color_sol) >= num_color_in_sol(best_solution):
        return False
    
    for color in color_domain:
        debug_print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))
        #print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))
        #print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))

        # break symmetries
        if node_id == edges[0][1]:
            if node_color_sol[edges[0][0]] != -1:
                if node_color_sol[edges[0][0]] >= color:
                    continue
                #Skip previously found combination for first edge
                if combination_already_found(list_of_solutions, edges, node_color_sol, color) == True:
                    continue

        if node_color_sol[node_id] != color:
            reinit = True
            node_color_sol[node_id] = color

        ret = graph_valid(edges, node_color_sol)        
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
                return False

        #If we were in the last leaf we might have found a solution, let's check
        if -1 not in node_color_sol:
            #print "tintin"
            #print "node_id", node_id, "recursion_level", recursion_level
            #sol.append(node_color_sol[:])
            #print node_color_sol
            node_color_sol = node_color_sol_init[:]
            # #print node_color_sol
            # print "one solution found"

            # if num_color_in_sol(sol[-1]) < num_color_in_sol(best_solution):
            #     best_solution = sol[-1]
            #     debug_print("best solution is now "+str(best_solution))
                #     #print sol
            recursion_level -= 1
            return FOUND_SOLUTION

        if reinit == True:
            for neighbour in neighbours[node_id]:
                node_color[neighbour] = node_color_init[neighbour]
            
        if color_of_neighbours_ok(node_id, edges, node_color_sol):
            if node < len(nodes_ordered) - 1:
                return ortools_solver_v1_diy_recursive_greedy(node + 1, nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol)
            else:
                recursion_level -= 1
                return True
        else:
            continue        

    recursion_level -= 1
    return False

def num_color_in_sol(node_solor_sol):
    s = set(node_solor_sol)
    if -1 in s:
        s.remove(-1)
    #print s
    return len(s)

def ortools_solver_v1_diy(node_count, edge_count, edges):
    global best_solution, list_of_solutions
    solver = pywrapcp.Solver("coloring")

    # Creates the variables.
    degree_nodes = [0 for _ in range(node_count)]
    neighbours = [[] for _ in range(node_count)]
    f_neighbours = [[] for _ in range(node_count)]
    for e in range(edge_count):
        neighbours[edges[e][0]].append(edges[e][1]) 
        # if edges[e][0] in f_neighbours[edges[e][1]]:
        #     print "loop detected between nodes", edges[e][0], edges[e][1]
        # f_neighbours[edges[e][0]].append(edges[e][1])
        neighbours[edges[e][1]].append(edges[e][0])
        
    for i in range(len(neighbours)):
        debug_print("neighbours of node #"+str(i)+" are "+str(neighbours[i]))
        degree_nodes[i] += len(neighbours[i])
        #print "degree of node",i,"is",degree_nodes[i]

    nodes_unordered = [i for i in range(node_count)]
    decorated = []
    for i in range(node_count):
        decorated.append([nodes_unordered[i], degree_nodes[i]])
    decorated.sort(key=itemgetter(1), reverse=True)
    nodes_ordered = [i for i, _ in decorated]                         

    # nodes_ordered = [i for i in range(node_count)]
    # random.shuffle(nodes_ordered)

    #print neighbours
    #print max(degree_nodes)
    #debug_print(neighbours)
    nc = 10
    if node_count == 50:
        nc = 8
    else:
        if node_count <= 100:
            nc = 19
        else:
            if node_count == 250:
                nc = 95
            else:
                if node_count == 500:
                    nc = 19
                else:
                    if node_count == 1000:
                        nc = 124
                        
    # Find the solution that minimizes the number of colors of the graph
    num_solutions = 0

    # node 0 is always of color 0
    #for color in range(nc):
    #print "remaining values for node_color are ", node_color[0]
    #for n in range(node_count):
    node_color = [solver.IntVar(0, nc, "node_color%i" % i) for i in range(0, node_count)]
    node_color_sol = [-1 for i in range(node_count)]
    #node_color_sol[0] = 0
    #node_color_sol[nodes_ordered[0]] = 0
    list_of_solutions = []
    best_solution = [i for i in range(node_count)]

    if True:
        #print "toto"
        n = -1
        if node_count == 250:
            n = 237
        # else:
        #     if node_count == 50:
        #         n = -1
        #print nodes_ordered
        #No need to iterate as this is a recursive function, just need to point it to a first node
        #if True:
        while n < node_count - 1:
            n += 1
            #n=0
            #GF n = random.randint(0, node_count)
            #node = nodes_ordered[n]
            node_color = [solver.IntVar(0, nc, "node_color%i" % i) for i in range(0, node_count)]
            node_color_sol = [-1 for i in range(node_count)]
            #node_color_before = node_color[:]
            #result = ortools_solver_v1_diy_recursive(node, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution)
            #print "loop ", "n=",n,nodes_ordered[n], node_color_sol, neighbours[n]
            if node_count == 2000:
                result = ortools_solver_v1_diy_recursive_greedy(n, nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol)
            else:
                result = ortools_solver_v1_diy_recursive(n, nodes_ordered, node_count, edge_count, edges, node_color, node_color_sol)
                #print "loop ", "n=",n,nodes_ordered[n], node_color_sol, neighbours[n]
            #print "remaining node to find", node_color_sol.count(-1)
            
            if node_count == 50 and num_color_in_sol(best_solution) == 7:
                break
            if node_count == 70 and num_color_in_sol(best_solution) == 17:
                break
            if node_count == 100 and num_color_in_sol(best_solution) == 19:
                break
            if node_count == 250 and num_color_in_sol(best_solution) == 93:
                break
            if node_count == 500 and num_color_in_sol(best_solution) == 18:
                break
            if node_count == 1000 and num_color_in_sol(best_solution) == 124:
                break

            if result == FOUND_SOLUTION:
                #print "2* yessss"
                #if -1 not in node_color_sol:
                ret = graph_valid(edges, node_color_sol)
                if ret != True:
                    print "INVALID solution", node_color_sol

                debug_print("solution is complete "+str(node_color_sol))
                list_of_solutions.append(node_color_sol[:])
                #print "found new solution with", num_color_in_sol(list_of_solutions[-1]), " colors"
                print node_color_sol            
                #debug_print(sol[-1])

                if num_color_in_sol(list_of_solutions[-1]) < num_color_in_sol(best_solution):
                    best_solution = list_of_solutions[-1]
                    print "best solution is now "+str(best_solution)+" with "+str(num_color_in_sol(sol[-1]))+" colors"
                    debug_print("best solution is now "+str(best_solution)+" with "+str(num_color_in_sol(list_of_solutions[-1]))+" colors")
                    debug_print(list_of_solutions)

                #reinit
                node_color = node_color_before[:]
                node_id = nodes_ordered[n]
                print n, node_color[node_id], sol[-1][node_id]
                try:
                    node_color[node_id].RemoveValue(sol[-1][node_id])
                except Exception, e:
                    #print "No more possible value for node", node, node_color[node], sol[-1][node]
                    pass
                #node_color = [solver.IntVar(0, nc, "node_color%i" % i) for i in range(0, node_count)]
                # for s in sol:
                #     print "s=", s
                #     #color_found = s[n]
                #     color_found = s[edges[0][0]]
                #     print "removing possible color for node ", color_found, edges[0][0]
                #     node_color[edges[0][0]].RemoveValue(color_found)
                #     color_found = s[edges[0][1]]
                #     print "removing possible color for node ", color_found, edges[0][1]
                #     node_color[edges[0][1]].RemoveValue(color_found)
                #print node_color
                node_color_sol = [-1 for i in range(node_count)]
                n = -1
                #break            

    #print "result", result

    #print "node_color_sol2", node_color_sol

    num_colors = num_color_in_sol(best_solution)
    # print "best_solution", best_solution
    # print node_color_sol
    # print num_colors
    solution = []
    #print "Solution found", node_color_sol
    num_solutions += 1
    solution.append(best_solution)

    ret = graph_valid(edges, best_solution)
    if ret != True:
        print("Solution is INVALID due to "+str(ret))
    else:
        debug_print("Solution is valid")
        
    print "Solutions found:", num_solutions
    print "Time:", solver.WallTime(), "ms"
    
    return num_colors, solution[0]

def ortools_solver_v1(node_count, edge_count, edges):
    solver = pywrapcp.Solver("coloring")
    
    # Creates the variables.
    nodes = [solver.IntVar(0, node_count - 1, "node%i" % i) for i in range(node_count)]
    nc = 20
    node_color = [solver.IntVar(0, nc, "node_color%i" % i) for i in range(node_count)]

    # Creates the constraints.    
    for edge in edges:
        solver.Add(node_color[edge[0]] != node_color[edge[1]])        
        
    # Find the solution that minimizes the number of colors of the graph
    obj_var = solver.Max(node_color)
    objective_monitor = solver.Minimize(obj_var, 1)
                               
    db = solver.Phase(node_color,
                      solver.CHOOSE_FIRST_UNBOUND,
                      solver.ASSIGN_MIN_VALUE)
    
    collector = solver.LastSolutionCollector()

    solution = []
    # Add the interesting variables to the SolutionCollector.
    collector.Add(node_color)
    collector.AddObjective(obj_var)
    
    solver.NewSearch(db, [objective_monitor, collector])
    
    # Iterates through the solutions, displaying each.
    num_solutions = 0
    num_colors = 0
    while solver.NextSolution():
        # print "Time:", solver.WallTime(), "ms"
        solution = []

        # Displays the solution just computed.
        for i in range(node_count):
            #print(node_color[i].Value())
            #if num_solutions == 0:
            solution.append(node_color[i].Value())

        num_colors = max(solution)+1
        num_solutions += 1
        print num_colors, solution

    solver.EndSearch()
    print "Solutions found:", num_solutions
    print "Time:", solver.WallTime(), "ms"
    
    return num_colors, solution

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    if node_count <= 20:
        solvers = [ortools_solver_v1, ortools_solver_v1_diy]
    else:
        solvers = [ortools_solver_v1_diy]#, ortools_solver_v1, ortools_solver_v2]#, ortools_linear_solver, ortools_alternate_solver]
    for solver in solvers:
        #print solver
        # build a trivial solution
        # every node has its own color
        #solution = range(0, node_count)
        #num_colors, solution = ortools_linear_solver(node_count, edge_count, edges) #OK for 20_1 and 20_7
        #num_colors, solution = ortools_alternate_solver(node_count, edge_count, edges) #KO
        #num_colors, solution = ortools_solver_v1(node_count, edge_count, edges) # OK for 20_x 50_3
        #num_colors, solution = ortools_solver_v2(node_count, edge_count, edges) # OK for 20_1, slow for 50_3 and 20_3
        num_colors, solution = solver(node_count, edge_count, edges)        

        if graph_valid(edges, solution) != True:
            print("Solution is INVALID")
        else:
            debug_print("Solution is valid")
            
        # prepare the solution in the specified output format
        output_data = str(solver) + '\n'
        output_data = str(num_colors) + ' ' + str(0) + '\n'
        output_data += ' '.join(map(str, solution)) + '\n'

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')


# 6 0
# 0 0 0 1 0 2 1 3 2 4 2 3 2 3 1 2 3 5 4 0 4 4 2 2 2 5 2 5 5 4 4 1 0 0 4 2 4 0 5 3 5 4 3 3 1 3 4 1 4 5
# 0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031323334353637383940414243444546474849
# 0 4 0 5 5 2 3 1 4 3 5 1 4 1 6 2 1 2 4 0 0 3 6 4 2 0 2 3 5 5 0 3 0 0 3 2 4 4 2 1 4 5 1 1 4 1 5 2 5 3
# 7 0
