# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:27:48 2021

@author: avelasq9
"""
import math
import numpy as np
import random
import time
import tracemalloc
import matplotlib.pyplot as plt
from itertools import permutations



class deadReckoningTSP:
    def __init__(self):
        
        # Metrics
        self.start_time = 0   
        self.end_time = 0 
        self.elapsed_time = 0
        self.memory = 0
              
        
    def path(self, places,indexes):         
       
        
        n = len(indexes)
        self.start_time = time.time()
        tracemalloc.start()
            
        dr_path =[]
        dr_path_length = 0
        dr_path.append(0)    
        # The first apple from the list, is the first one to start with 
        next_apple = 0    
        indexes.pop(0)
        
        for i in range(n-1):
            x_ini = places[next_apple, 0]
            y_ini = places[next_apple, 1]
            z_ini = places[next_apple, 2]
           
            # DEBUGGING PRINT
            #print('The next apple is ', next_apple)
    
            dr_e_dist_min = 1000
            j = 0               
            while j < len(indexes):
                
                index  = indexes[j]
                
                # Euclidean Distance            
                x_end = places[index, 0]
                y_end = places[index, 1]
                z_end = places[index, 2]                
                dx = abs(x_ini - x_end)
                dy = abs(y_ini - y_end)
                dz = abs(z_ini - z_end)                
                dr_e_dist = math.sqrt(dx**2 + dy**2 + dz**2)
                
                # DEBUGGING PRINT
                #print(index, dr_e_dist)
                
                # Keep track of the closest apple
                if dr_e_dist < dr_e_dist_min:
                    dr_e_dist_min = dr_e_dist
                    next_apple = index
                    j_to_remove = j
                    
                current, peak = tracemalloc.get_traced_memory()
                
                j += 1
                
            dr_path_length = dr_path_length + dr_e_dist_min
                
            # Append the apple in the list of indexes    
            dr_path.append(next_apple)
            # Remove this one from the original list
            indexes.pop(j_to_remove)   
        
        # Finish metrics
        self.end_time = time.time()
        tracemalloc.stop()
        self.memory = peak/10**6        
        self.elapsed_time = self.end_time - self.start_time
        
        
        return dr_path, dr_path_length
    
                 
                 
                 


