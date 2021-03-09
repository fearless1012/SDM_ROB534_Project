# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:05:15 2021

@author: Miranda
"""

import numpy as np
import itertools
from math import inf


def held_karp_apples(apple_locations, starting_location):
    #flag for path reconstruction
    path_found = False
    
    #empty array for the path
    path = []
    
    #get the number of apples
    n = len(apple_locations)
    
    #change from lists to numpy arrays
    apple_locations = np.array(apple_locations)
    
    #generate a matrix of the edge costs
    
    D = np.zeros([n,n])
    
    for apple1 in range(0, n):
        for apple2 in range(0,n):
            D[apple1, apple2] = np.linalg.norm(apple_locations[apple1] - apple_locations[apple2])
           
    #p is pointers for reconstructing path
    P = []
    #g is cost of getting to a node given a set ID
    G = []
    #S is subsets
    S = {}
    curr_set_index = 0
    
    end_apple = inf
    final_cost = inf
    final_pointer = []
    
    #for each set size
    for k in range(0,n):
        if (k==0):
            set_p = []
            set_g = []
            for apple in range(0,n):
                set_p.append(["start", "invalid"])
                set_g.append(np.linalg.norm(apple_locations[apple] - starting_location))
            P.append(set_p)
            G.append(set_g)
            S[str({0,})] = 0;
        else:
            #generate all combinations of nodes to visit
            #for each set
            for subset in itertools.combinations(range(0,n), k):
                # print("checking subset: {}".format(subset))
                curr_set_index += 1
                S[str(subset)] = curr_set_index
                set_p =  []
                set_g = []
                #for each apple
                for apple in range(0,n):
                    # print("checking apple: {}".format(apple))
                    if apple not in subset:
                        [cost, pointer] = get_path(apple, subset, D, S, G)
                        set_p.append(pointer)
                        set_g.append(cost)
                        if (k == n-1) and (cost < final_cost):
                            final_cost = cost
                            end_apple = apple
                            final_pointer = pointer
                    else:
                        set_g.append(0)
                        set_p.append(["invalid", "invalid"])
                P.append(set_p)
                G.append(set_g)
                print("All apples visited for this subset")
    print("Final Apple: {} from {}".format(end_apple, final_pointer[0]))
    curr_pointer = final_pointer
    path.append(apple_locations[end_apple].tolist())
    while not path_found:
        path.append(apple_locations[curr_pointer[0]].tolist())
        if (curr_pointer[1] == 0):
            path.append(starting_location)
            path_found = True
        else:
            curr_pointer = P[curr_pointer[1]][curr_pointer[0]]
    path.reverse()             
    return(path)

def get_path(apple,subset,distances,set_dict, costs):
    for apple_from in subset:
        cost = inf
        prev = "something went wrong"
        for sub_subset in itertools.combinations(subset, len(subset)-1):
            index_to_check = "invalid"
            if apple_from not in sub_subset:                
                if len(sub_subset) >= 1:
                    index_to_check = set_dict[str(sub_subset)]
                    sub_subpath_cost = costs[index_to_check][apple_from]
                    subpath_cost = distances[apple][apple_from] + sub_subpath_cost
                else:
                    subpath_cost = distances[apple][apple_from]
                    index_to_check = 0
                if subpath_cost < cost:
                    prev = [apple_from, index_to_check]
                    cost = subpath_cost
    print("optimal cost of going to apple {} visiting {} is {}".format(apple,subset,cost))
    return(cost, prev)

if __name__ == '__main__':
    apple_locations = [[0,1,1],[2,2,2],[3,2,4],[3,3,5],[2,4,5],[0,5,6],[1,5,5]]
    starting_position = [0,0,0]
    held_karp_apples(apple_locations, starting_position)