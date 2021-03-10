# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:27:48 2021

@author: avelasq9
"""
import math
import numpy as np
import random


# class RandomMap:
#     def __init__(self):
#
#         # Parameters for the volume where the apples will grow
#
#         self.x_lim = 100
#         self.y_lim = 100
#         self.z_lim = 100
#         self.indexes = []
#
#
def coordinates (n_apples):

# ................. Step 1: Create a random map with n nodes ..............

    x_lim = 100
    y_lim = 100
    z_lim = 100
    indexes = []

    apples = []
    for i in range(n_apples):

        indexes.append(i)

        x = random.randint(0, x_lim)
        y = random.randint(0, y_lim)
        z = random.randint(0, z_lim)

        apples.append([x,y,z])

    return apples


        
    
                 
                 
                 


