#!/usr/bin/python
# -*- coding: utf-8 -*-
# Graph Coloring
# fmYLC, ./data/gc_50_3, solver.py, Coloring Problem 1
# IkKpq, ./data/gc_70_7, solver.py, Coloring Problem 2
# pZOjO, ./data/gc_100_5, solver.py, Coloring Problem 3
# XDQ31, ./data/gc_250_9, solver.py, Coloring Problem 4
# w7hAO, ./data/gc_500_1, solver.py, Coloring Problem 5
# tthbm, ./data/gc_1000_5, solver.py, Coloring Problem 6


from ortools.constraint_solver import pywrapcp
from ortools.linear_solver import pywraplp
from operator import itemgetter

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
def ortools_solver_v1_diy_recursive(node_id, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution):
    global recursion_level, FOUND_SOLUTION
    recursion_level += 1
    
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
    
    for color in color_domain:
        debug_print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))
        #print(indentation_per_recursion_level*recursion_level+"testing color "+str(color)+" for node "+str(node_id))

        # break simetry
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
                node_color[node_id].RemoveValue(color)
                debug_print(indentation_per_recursion_level*recursion_level+str(color)+" is NOT a valid color for node "+str(node_id)+" due to "+str(ret)+" trying another color for node")
                continue
            except Exception, e:
                #print node_color_sol, node_color
                print "No more possible value for node_id", node_id
                return False

        # If we were in the last leaf we might have found a solution, let's check
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
            return FOUND_SOLUTION

        if reinit == True:
            for neighbour in neighbours[node_id]:
                node_color[neighbour] = node_color_init[neighbour]
            
        if neighbours[node_id] != []:
            for neighbour in neighbours[node_id]:
                if node_color_sol[neighbour] == -1:
                    debug_print(indentation_per_recursion_level*recursion_level+"considering neighbour "+str(neighbour)+" for node "+str(node_id))
                    result = ortools_solver_v1_diy_recursive(neighbour, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution)

                    # if result == FOUND_SOLUTION:
                    #     print "yeeeeeeeeeeeeeees"
                        
                    if result == False:
                        debug_print(indentation_per_recursion_level*recursion_level+"Invalid solution, trying another color for node"+str(node_id))
                        node_color[neighbour].RemoveValue(color)
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
                node_color[node_id].RemoveValue(color)
                break
                
        else:
            debug_print("node "+str(node_id)+" has no neighbour")
            recursion_level -= 1
            return True
        
        if result == True:
            #debug_print(color, "is a valid color for node", node_id)
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
    if -1 not in node_color_sol:
        print("solution is complete "+str(node_color_sol)+" recursion_level "+str(recursion_level)+" for node_id "+str(node_id))
        #print sol[-1]
        recursion_level -= 1
        return FOUND_SOLUTION

    recursion_level -= 1
    return True


def num_color_in_sol(node_solor_sol):
    return len(set(node_solor_sol))

def ortools_solver_v1_diy(node_count, edge_count, edges):
    solver = pywrapcp.Solver("coloring")

    # Creates the variables.
    #degree_nodes = [0 for _ in range(node_count)]
    neighbours = [[] for _ in range(node_count)]
    for e in range(edge_count):
        neighbours[edges[e][0]].append(edges[e][1]) #solver.IntVar(edge[1],edge[1]))
        #neighbours[edges[e][1]].append(edges[e][0]) #solver.IntVar(edge[0],edge[0]))
        
    for i in range(len(neighbours)):
        debug_print("neighbours of node #"+str(i)+" are "+str(neighbours[i]))
        #degree_nodes[i] += len(neighbours[i])

    #debug_print(neighbours)
    nc = 10
    if node_count <= 100:
        nc = 30
    else:
        if node_count == 250:
            nc = 100
        else:
            nc = 150
    # Find the solution that minimizes the number of colors of the graph
    num_solutions = 0

    # node 0 is always of color 0
    #for color in range(nc):
    #print "remaining values for node_color are ", node_color[0]
    #for n in range(node_count):
    node_color = [solver.IntVar(0, nc, "node_color%i" % i) for i in range(0, node_count)]
    node_color_sol = [-1 for i in range(node_count)]
    node_color_sol[0] = 0
    sol = []
    best_solution = [i for i in range(node_count)]

    n = -1
    while n < node_count - 1:
        n += 1
        #print "n=",n
        result = ortools_solver_v1_diy_recursive(n, node_count, edge_count, edges, node_color, node_color_sol, sol, best_solution)
        if result == FOUND_SOLUTION:
            #print "2* yessss"
            #if -1 not in node_color_sol:
            debug_print("solution is complete "+str(node_color_sol))
            sol.append(node_color_sol[:])
            #print "found new solution with", num_color_in_sol(sol[-1]), " colors"
            #print node_color_sol            
            #debug_print(sol[-1])

            if num_color_in_sol(sol[-1]) < num_color_in_sol(best_solution):
                best_solution = sol[-1]
                #print "best solution is now "+str(best_solution)+" with "+str(num_color_in_sol(sol[-1]))+" colors"
                debug_print("best solution is now "+str(best_solution)+" with "+str(num_color_in_sol(sol[-1]))+" colors")
                debug_print(sol)

            #reinit
            node_color = [solver.IntVar(0, nc, "node_color%i" % i) for i in range(0, node_count)]
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

    ret = graph_valid(edges, node_color_sol)
    if ret != True:
        print("Solution is INVALID due to "+str(ret))
    else:
        debug_print("Solution is valid")
        
    # print "Solutions found:", num_solutions
    # print "Time:", solver.WallTime(), "ms"
    
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
        print "Time:", solver.WallTime(), "ms"
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

