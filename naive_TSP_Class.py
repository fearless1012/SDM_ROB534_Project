# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:27:48 2021

@author: avelasq9
"""
import math
import numpy as np
import time
import tracemalloc
from itertools import permutations



class NaiveTSP:
    def __init__(self):
        
        # Metrics
        self.start_time = 0   
        self.end_time = 0 
        self.elapsed_time = 0
        self.memory = 0
        self.perm = 0
        
        
    def path(self, places, indexes):
        
        n = len(places)
        
        # Initialize metrics
        self.start_time = time.time()
        tracemalloc.start()
               
        
        # Get all the possible permutations
        reference = 1000
        self.perm = list(permutations(indexes))    
        #print ("The total amount of permutations is %.0i" % len(perm))
        
        for i in self.perm:  
                    
            total_cost = 0
            j=0  
            while j < (n-1):
                
                # Apple index from the combination
                start_apple_index = int(i[j])
                next_apple_index = int(i[j+1])
                   
                # Euclidean Distance       
                delta_x = abs(places[start_apple_index, 0] - places[next_apple_index, 0])    
                delta_y = abs(places[start_apple_index, 1] - places[next_apple_index, 1])
                delta_z = abs(places[start_apple_index, 2] - places[next_apple_index, 2])            
                e_dist = math.sqrt(delta_x ** 2 + delta_y ** 2 + delta_z ** 2)            
                total_cost = total_cost + e_dist
                            
                j += 1
                
            # Keep track of the lowest cost               
            if total_cost < reference:
                # Optimal path
                reference = total_cost        
                path = i
            current, peak = tracemalloc.get_traced_memory()
                      
                
        # Finish metrics
        self.end_time = time.time()
        tracemalloc.stop()
        self.memory = peak/10**6        
        self.elapsed_time = self.end_time - self.start_time
               
        
        return path, reference
        
        
    
                 
                 
                 


