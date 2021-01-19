#!/usr/bin/python
# -*- coding: utf-8 -*-
# P-Jo51xFEeauThLQfRQvyw
# Traveling Salesman
# YQL5Q, ./data/tsp_51_1, solver.py, Traveling Salesman Problem 1
# R9hfg, ./data/tsp_100_3, solver.py, Traveling Salesman Problem 2
# ZVrLp, ./data/tsp_200_2, solver.py, Traveling Salesman Problem 3
# 6tyFn, ./data/tsp_574_1, solver.py, Traveling Salesman Problem 4
# tSpoY, ./data/tsp_1889_1, solver.py, Traveling Salesman Problem 5
# YOVlV, ./data/tsp_33810_1, solver.py, Traveling Salesman Problem 6
# 0
# YQL5Q,      482,      430
# R9hfg,    23433,    20800
# ZVrLp,    35985,    30000
# 6tyFn,    40000,    37600
# tSpoY,   378069,   323000
# YOVlV, 78478868, 67700000

import math
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)

def build_distance_matrix_from_input(input_data):
    matrix=[]
    # print(input_data)
    for src in input_data:
        # print(src)
        # print("src.x",src.x)
        a = []
        for dst in input_data:
            # print("dst.x",dst.x)
            if src.x == dst.x and src.y == dst.y:
                a.append(0)
            else:
                a.append(length(src, dst))

        matrix.append(a)
    # print(matrix)
    return matrix

# def solve_with_ortools(input_data):
def solve_it(input_data):
    """Simple travelling salesman problem between cities."""

    """Stores the data for the problem."""
    lines = input_data.split('\n')
            
    nodeCount = int(lines[0])
            
    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    data = {}
    data['distance_matrix'] = build_distance_matrix_from_input(points)
    # [
    #     [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
    #     [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
    #     [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
    #     [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
    #     [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
    #     [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
    #     [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
    #     [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
    #     [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
    #     [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
    #     [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
    #     [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
    #     [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    # ]  # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])
    
    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)
    

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    
    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    # if solution:
    #     print_solution(manager, routing, solution)

    # print(solution)
    value = 0
    index = routing.Start(0)
    while not routing.IsEnd(index):
        newindex = solution.Value(routing.NextVar(index))
        value += length(points[manager.IndexToNode(index)],points[manager.IndexToNode(newindex)])
        index = newindex
    # print("value",value)
    
    # output_data = '%.2f' % solution.ObjectiveValue() + ' ' + str(0) + '\n'
    output_data = '%.2f' % value + ' ' + str(0) + '\n'
    index = routing.Start(0)
    route_distance = 0
    while not routing.IsEnd(index):
        sol = manager.IndexToNode(index)
        output_data += " " + str(sol)
        index = solution.Value(routing.NextVar(index))
    # output_data += ' '.join(map(str, solution))
    return output_data

# def solve_it(input_data):
#     # Modify this code to run your optimization algorithm

#     lines = input_data.split('\n')
#     nodeCount = int(lines[0])
#     # build a trivial solution
#     # visit the nodes in the order they appear in the file
#     solution = range(0, nodeCount)

#     # calculate the length of the tour
#     obj = length(points[solution[-1]], points[solution[0]])
#     for index in range(0, nodeCount-1):
#         obj += length(points[solution[index]], points[solution[index+1]])

#     # prepare the solution in the specified output format
#     output_data = '%.2f' % obj + ' ' + str(0) + '\n'
#     output_data += ' '.join(map(str, solution))

#     return output_data

import sys

def main():
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
            # parse the input
            print(solve_it(input_data))
            # print(solve_with_ortools(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')
        
if __name__ == '__main__':
    main()
    
