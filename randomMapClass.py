# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:27:48 2021

@author: avelasq9
"""
import math
import numpy as np
import random


class RandomMap:
    def __init__(self):
        
        # Parameters for the volume where the apples will grow
        
        self.x_lim = 100
        self.y_lim = 100
        self.z_lim = 100
        self.indexes = []
        
                              
    def coordinates (self, n_apples):        
        
        # ................. Step 1: Create a random map with n nodes ..............
        
        apples = np.zeros((n_apples,3))        
        for i in range(n_apples):
            
            self.indexes.append(i)
        
            x = random.randint(0, self.x_lim)
            y = random.randint(0, self.y_lim)
            z = random.randint(0, self.z_lim)
                          
            apples [i,0] = x
            apples [i,1] = y
            apples [i,2] = z
        
        return apples
        
        
        
    
                 
                 
                 


