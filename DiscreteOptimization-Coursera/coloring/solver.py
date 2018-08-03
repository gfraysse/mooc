#!/usr/bin/python
# -*- coding: utf-8 -*-

from ortools.constraint_solver import pywrapcp

# https://github.com/google/or-tools/blob/master/examples/python/coloring_ip.py
def ortools_alternate_solver(node_count, edge_count, edges):
    solver = pywrapcp.Solver("coloring")
    # x[i,c] = 1 means that node i is assigned color c
    nc = 10
    x = {}

    for v in range(node_count):
        for j in range(nc):
            x[v, j] = solver.IntVar(0, 1, 'v[%i,%i]' % (v, j))

    # u[c] = 1 means that color c is used, i.e. assigned to some node
    u = [solver.IntVar(0, 1, 'u[%i]' % i) for i in range(nc)]

    # number of colors used, to minimize
    obj = solver.Sum(u)

    #
    # constraints
    #
    
    # each node must be assigned exactly one color
    for i in range(node_count - 1):
        solver.Add(solver.Sum([x[i, c] for c in range(nc)]) == 1)

    # adjacent nodes cannot be assigned the same color
    # (and adjust to 0-based)
    for i in range(edge_count - 1):
        for c in range(nc):
            a = x[edges[i][0], c]
            b = x[edges[i][1], c]
            solver.Add(a + b <= u[c])

    # objective
    objective = solver.Minimize(obj, 1)

    #
    # solution
    #
    solver.Solve()
    
    print 'number of colors:', int(solver.Objective().Value())
    print 'colors used:', [int(u[i].SolutionValue()) for i in range(nc)]

    for v in range(node_count):
        print 'v%i' % v, ' color '
        for c in range(nc):
            if int(x[v, c].SolutionValue()) == 1:
                print(c)

    # # Iterates through the solutions, displaying each.
    # num_solutions = 0
    # num_colors = 0
    # solution = []
    # while solver.NextSolution():
    #     solution = []

    #     # Displays the solution just computed.
    #     for i in range(node_count):
    #         #print(node_color[i].Value())
    #         #if num_solutions == 0:
    #         solution.append(node_color[i].Value())

    #     num_colors = max(solution)+1
    #     num_solutions += 1
    #     #print num_colors, solution

    # solver.EndSearch()
    # print "Solutions found:", num_solutions
    # print "Time:", solver.WallTime(), "ms"
    
    return num_colors, solution

def ortools_solver(node_count, edge_count, edges):
    solver = pywrapcp.Solver("coloring")
    
    # Creates the variables.
    nodes = [solver.IntVar(0, node_count - 1, "node%i" % i) for i in range(node_count)]
    neighbours = [[] for _ in range(node_count)]
    node_color = [solver.IntVar(0, 20, "node_color%i" % i) for i in range(node_count)]

    # Creates the constraints.    
    # All rows must be different.
    for edge in edges:
        solver.Add(node_color[edge[0]] != node_color[edge[1]])
        neighbours[edge[0]].append(node_color[edge[1]]) #solver.IntVar(edge[1],edge[1]))
        neighbours[edge[1]].append(node_color[edge[0]]) #solver.IntVar(edge[0],edge[0]))

    # Absurd neighbors of a node can be of the same color...
    # for n in neighbours:
    #     print n
        #solver.Add(solver.AllDifferent(n))
    # Trying to break symmetries
    #solver.Add(node_color[edge[0]] <= node_color[edge[1]])
        
    # Find the solution that minimizes the number of colors of the graph
    obj_var = solver.Max(node_color)
    objective_monitor = solver.Minimize(obj_var, 1)
                               
    db = solver.Phase(node_color,
                      solver.CHOOSE_FIRST_UNBOUND,
                      solver.ASSIGN_RANDOM_VALUE)
    
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
        solution = []

        # Displays the solution just computed.
        for i in range(node_count):
            #print(node_color[i].Value())
            #if num_solutions == 0:
            solution.append(node_color[i].Value())

        num_colors = max(solution)+1
        num_solutions += 1
        #print num_colors, solution

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

    # build a trivial solution
    # every node has its own color
    #solution = range(0, node_count)
    num_colors, solution = ortools_alternate_solver(node_count, edge_count, edges)


    # prepare the solution in the specified output format
    output_data = str(num_colors) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

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

