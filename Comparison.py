# ---------------------OREGON STATE UNIVERSITY (OSU)--------------------------#
# School of Mechanical, Industrial and Manufacturing Engineering (MIME)
# Robotics Graduate Program
# ROB534 Winter'2021 - Final Project
# Students: Alejandro Velasquez (velasale@oregonstate.edu)
#           Ramya Jayaraman
#           Miranda Cravetz
# ----------------------------------------------------------------------------#
# Description: TSP Comparison
#
#
# ----------------------------------------------------------------------------#

from randomMapClass import RandomMap
from naive_TSP_Class import NaiveTSP
from printerClass import TSPfigures
from deadReckoningClass import deadReckoningTSP

Nodes = []
nv_Time = []
nv_Memory =[]
dr_Time = []
dr_Memory =[]

n = 3
while n < 11:

    # Step 1: Generate a Random Tree of Apples
    ap_map = RandomMap()
    ap_coord = ap_map.coordinates(n)
    indexes = ap_map.indexes           
    
    
    # Step 2: Execute a Naive Algorithm
    naive_tsp = NaiveTSP()
    naive_path, naive_length = naive_tsp.path(ap_coord, indexes)
    # Get the Naive metrics
    nv_Time.append(naive_tsp.elapsed_time)
    nv_Memory.append(naive_tsp.memory)


    # Step 3: Execute a Dead Reckoning Algorithm
    d_reckon = deadReckoningTSP()
    d_reckon_path, d_reckon_length = d_reckon.path(ap_coord, indexes) 
    # Get the Dead Reckon metrics
    dr_Time.append(d_reckon.elapsed_time)
    dr_Memory.append(d_reckon.memory)
    
    Nodes.append(n)
    
    # Step 4: Print
    plots = TSPfigures()
    # Step 4.1: Print the apple Tree
    plots.points(ap_coord)    
    # Step 4.2: Print the Naive obtained path (optimal)
    plots.lines(naive_path, ap_coord, naive_length, 'Naive (optimal)')
    plots.lines(naive_path, ap_coord, naive_length, 'Naive (optimal)', 30, -90)
    # Step 4.3: Print the Dead Reckoning path
    plots.lines(d_reckon_path, ap_coord, d_reckon_length, 'Dead Reckon')
    plots.lines(d_reckon_path, ap_coord, d_reckon_length, 'Dead Reckon', 30, -90)
     
           
        
    # DEBUGGING prints    
    print(ap_coord)
    print(naive_path, naive_length)
    print(d_reckon_path, d_reckon_length)
    print(naive_tsp.elapsed_time)
    print('\n')
    
    n += 1
    
# Step 4.4: Print the metrics
plots.metrics(Nodes, nv_Time, nv_Memory)
plots.metrics(Nodes, dr_Time, dr_Memory)



