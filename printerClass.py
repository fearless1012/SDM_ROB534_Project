# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:27:48 2021

@author: avelasq9
"""

import matplotlib.pyplot as plt


class TSPfigures:
    def __init__(self):
        
        # Parameters for the volume where the apples will grow
        self.k = 1
                
                              
    def points (self, apples):    
        
        # ... Plot 3D apple distribution
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(apples[:,0], apples[:,1], apples[:,2]) 
        
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax.set_zlabel('z label')
        ax.set_title('Localization of %.i apples' % len(apples))
         
        plt.show()  
        
        
    def lines (self, path, apples, length, title = 'Default', elevation = 30, azimuth = -60):
        
        x_values = []
        y_values = []
        z_values = []
        
        n = len(apples)
        
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax.set_zlabel('z label')
        
        for i in range(n):
            start_point_index = int(path[i])
            
            x_values.append(apples[start_point_index, 0])
            y_values.append(apples[start_point_index, 1])
            z_values.append(apples[start_point_index, 2])        
                           
        ax.plot(x_values, y_values, z_values, 'o--')     
        ax.set_title('%s path for %.i apples,\n with a length of %.2f' % (title, n, length))   
        ax.view_init(elevation, azimuth)
        plt.show()
        
    
    def metrics (self, NODES, TIMES, MEMORY):
       
        fig, (ax1, ax2) = plt.subplots(2,1, sharex =True)
        ax1.plot(NODES, TIMES)
        ax2.plot(NODES, MEMORY)
        
        ax2.set_xlabel('apples')
        ax1.set_ylabel('Elapsed Time [sec]')
        ax2.set_ylabel('Memory allocated [MB]')
        
        plt.show()
        
        
        
        
        
       
        
        
        
    
                 
                 
                 


