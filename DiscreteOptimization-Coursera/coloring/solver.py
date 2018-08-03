#!/usr/bin/python
# -*- coding: utf-8 -*-

from ortools.constraint_solver import pywrapcp

def ortools_solver(node_count, edge_count, edges):
    solver = pywrapcp.Solver("coloring")
    # Creates the variables.
    # The array index is the column, and the value is the row.
    nodes = [solver.IntVar(0, node_count - 1, "node%i" % i) for i in range(node_count)]
    node_color = [solver.IntVar(0, node_count / 3, "node_color%i" % i) for i in range(node_count)]
    #edges_solver = []
    # for edge in edges:
    #     edge_node_1 = solver.IntVar(0, node_count - 1, "edge%i_i" % edge[0])
    #     edge_node_2 = solver.IntVar(0, node_count - 1, "edge%i_j" % edge[1])
    #     edges_solver.append([edge_node_1, edge_node_2])
    # Creates the constraints.    
    # All rows must be different.
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
    # print "Solutions found:", num_solutions
    # print "Time:", solver.WallTime(), "ms"
    
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
    num_colors, solution = ortools_solver(node_count, edge_count, edges)


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

