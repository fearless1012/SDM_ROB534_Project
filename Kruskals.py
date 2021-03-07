import math
import numpy as np


def get_edge_weights(apple_locations):
    a = len(apple_locations)
    edge_weight = {}
    edge_1 = apple_locations[0]
    for i in range(len(apple_locations)):
        for j in range(i+1,len(apple_locations)):
            edge_weight[i,j] = math.sqrt((apple_locations[j][0]-apple_locations[i][0])**2 + (apple_locations[j][1]-apple_locations[i][1])**2 + (apple_locations[j][0]-apple_locations[i][0])**2)

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
    forest = []
    edge_weight = get_edge_weights(apple_locations)
    sorted_edges = sort_edge_weights(edge_weight)
    s_i = 0
    f_i = 0

    parent = []
    rank = []
    #create subsets with single elements
    for node in range(len(apple_locations)):
        parent.append(node)
        rank.append(0)

    while f_i < len(apple_locations) - 1 :
        u,v = sorted_edges[s_i]
        w = edge_weight[sorted_edges[s_i]]
        s_i = s_i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x!=y:
            f_i = f_i + 1
            forest.append([u,v,w])
            union(parent, rank, x, y)

    minimumCost = 0
    print("Edges in the constructed MST")
    for u,v, w in forest:
        minimumCost += w
        print(u, v, w)
    print("Minimum cost : ", minimumCost)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple_locations = [[0,1,1],[2,2,2],[3,2,4],[3,3,5],[2,4,5],[0,5,6],[1,5,5]]
    starting_position = [0,0,0]
    Kruskals(apple_locations, starting_position)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
