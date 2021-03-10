import math
import numpy as np
import randomMapClass
import time
import tracemalloc


def get_edge_weights(apple_locations):
    edge_weight = {}
    for i in range(len(apple_locations)):
        for j in range(i+1,len(apple_locations)):
            edge_weight[i,j] = math.sqrt((apple_locations[j][0]-apple_locations[i][0])**2 + (apple_locations[j][1]-apple_locations[i][1])**2 + (apple_locations[j][2]-apple_locations[i][2])**2)
    return edge_weight

def sort_edge_weights(edge_weight):
    edges_for_sorting = []
    for edge in edge_weight:
        edges_for_sorting.append(edge)
    sorted_edges = []
    while len(edges_for_sorting) > 0:
        min_edge = {}
        min_value = 1000
        for edge in edges_for_sorting:
            if edge_weight[edge] < min_value:
                min_value = edge_weight[edge]
                min_edge = edge
        sorted_edges.append(min_edge)
        edges_for_sorting.remove(min_edge)
    return sorted_edges

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent,parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def Kruskals(apple_locations, starting_location):
    # tracemalloc.start()
    forest = []
    traversed = []
    all_nodes = apple_locations
    all_nodes.append(starting_location)
    starting_location_index = len(all_nodes) - 1
    edge_weight = get_edge_weights(all_nodes)
    sorted_edges = sort_edge_weights(edge_weight)
    s_i = 0
    f_i = 0

    parent = []
    rank = []
    #create subsets with single elements
    for node in range(len(all_nodes)):
        parent.append(node)
        rank.append(0)
    minimumCost = 0
    path_unsorted_nodea = []
    path_unsorted_nodeb = []
    # path_trial = np.full(len(all_nodes), np.inf)
    # path_trial[0] = starting_location_index
    while f_i < len(all_nodes) - 1:
        u,v = sorted_edges[s_i]
        w = edge_weight[sorted_edges[s_i]]
        s_i = s_i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x!=y:
            if (u != starting_location_index and v != starting_location_index and traversed.count(u) < 2 and traversed.count(v) < 2) or ((u == starting_location_index or v == starting_location_index) and traversed.count(starting_location_index)<1 and traversed.count(u) < 2 and traversed.count(v) < 2):
                    traversed.append(u)
                    traversed.append(v)
                    f_i = f_i + 1
                    forest.append([u,v,w])
                    path_unsorted_nodea.append(u)
                    path_unsorted_nodeb.append(v)

                    # if u not in path_unsorted_nodea and v not in path_unsorted_nodeb:
                    #     path_unsorted_nodeb.append(v)
                    #     path_unsorted_nodea.append(u)
                    # elif u not in path_unsorted_nodeb and v not in path_unsorted_nodea:
                    #     path_unsorted_nodeb.append(u)
                    #     path_unsorted_nodea.append(v)
                    # elif u in path_unsorted_nodea:
                    #     index = path_unsorted_nodea.find(u)


                    minimumCost += w
                    union(parent, rank, x, y)

    path = []
    path.append(starting_location_index)
    while len(path) < len(all_nodes):
        if starting_location_index in path_unsorted_nodea:
            index = path_unsorted_nodea.index(starting_location_index)
            path.append(path_unsorted_nodeb[index])
            starting_location_index = path_unsorted_nodeb[index]
            path_unsorted_nodeb.pop(index)
            path_unsorted_nodea.pop(index)
        elif starting_location_index in path_unsorted_nodeb:
            index = path_unsorted_nodeb.index(starting_location_index)
            path.append(path_unsorted_nodea[index])
            starting_location_index = path_unsorted_nodea[index]
            path_unsorted_nodeb.pop(index)
            path_unsorted_nodea.pop(index)


    # while len(final_path) < len(apple_locations):

        # nodeb = path_unsorted_nodeb[i]
        # final_path.append(path_unsorted_nodea[i])
        # final_path.append(path_unsorted_nodeb[i])
        # path_unsorted_nodea.pop(i)
        # path_unsorted_nodeb.pop(i)
        # if nodeb in path_unsorted_nodea:
        #     j = find(path_unsorted_nodea, nodeb)
        #     if path_unsorted_nodea[j] not in final_path:
        #         i = j
        #         continue


    # for i in range(len(path_unsorted_nodea)):
    #     print(path_unsorted_nodea[i])
    # corner_nodes = []
    # for t in range(len(apple_locations)):
    #     if traversed.count(t) == 1:
    #         corner_nodes.append(t)

    # for t in corner_nodes:

    # while len(path) < len(forest):



    # for u,v, w in forest:
    #     # minimumCost += w
    #     print(u, v, w)
    t = time.time() - start_time
    c = minimumCost
    return t,c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple_locations = randomMapClass.coordinates(n_apples=5)
    # print(apple_locations)
    # input("wait")
# [[1, 98,  63],
#  [ 74, 10, 20],
#  [ 74, 72, 60],
#  [ 63, 40, 51],
#  [ 58,  3, 95],
#  [ 58, 10, 35],
#  [ 25, 6, 43],
#  [ 21, 59, 14],
#  [ 97, 84, 29],
#  [  4,100, 97],
#  [ 28, 20, 61]]
# [1,1,1],[1,1,0],[1,1,2],[1,0,1],[1,2,1],[0,5,6],[1,5,5]]
    starting_position = [58,3,95]
    stime = []
    cost = []
    memory = []
    for i in range(5):
        start_time = time.time()
        tracemalloc.start()
        t,c= Kruskals(apple_locations, starting_position)
        m = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memory.append(m[1])
        stime.append(t)
        cost.append(c)

    print("Time :", sum(stime)/5)
    print("Cost :", sum(cost)/5)
    print("Memory :", sum(memory)/500000)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
