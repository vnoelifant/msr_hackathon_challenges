#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:26:43 2018

@author: vnoelifant

 Implement the RRT algorithm using a domain D=[0,100]×[0,100], an initial configuration qinit=(50,50), and a
 stepsize Δq=1. Use the Euclidean metric for evaluating distance.
 This is a Python script that constructs and plots an RRT using these conditions

 The RRT algorith is summarized as follows:

  Input: Initial configuration qinit, number of vertices in RRT K, incremental distance Δq
  Output: RRT graph G

  G.init(qinit)
  for k=1 to K
    qrand ← RAND_CONF()
    qnear ← NEAREST_VERTEX(qrand, G)
    qnew ← NEW_CONF(qnear, qrand, Δq)
    G.add_vertex(qnew)
    G.add_edge(qnear, qnew)
  return G

"""
import numpy as np
import matplotlib.pyplot as mp
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy.spatial import distance
import random

# Set up the constants

# Create the space dimensions
xDim = 100
yDim = 100

# Create the number of nodes (iterations)
numNodes = 40

# Create the incrememntal distance
deltaQ = 1

def getEuclidDistance(pt1,pt2):
    euclidDist = distance.euclidean(pt1, pt2)
    #dist = [(a - b)**2 for a, b in zip(pt1, pt2)]
    #dist = math.sqrt(sum(dist))
    return euclidDist

# function to get point nearest to qRand
def nearestPoint(qRand, nodes):
    minDistance = 0
    #print(nodes)
    print(nodes)
    print("qRand: ", qRand)
    for pt in nodes:
        dist = getEuclidDistance(qRand,pt)
        if (dist < minDistance) or minDistance == 0:
            minDistance = dist
            qNear = pt
    print("qNear: ",qNear)
    return qNear

            
def getSteeringDistance(qRand, qNear):
    print(getEuclidDistance(qRand,qNear))
    #if getEuclidDistance(qRand,qNear) < deltaQ:
        #return qRand
    #else:
        
        #vect = (qRand - qNear)/getEuclidDistance(qRand,qNear)
        #print(vect)
        #print(qNear + vect*deltaQ)
        #return qNear + vect*deltaQ 
    vect = (qRand - qNear)/getEuclidDistance(qRand,qNear)
    print(vect)
    print(qNear + (vect)* deltaQ * getEuclidDistance(qRand,qNear)) 
    return qNear + (vect)* deltaQ * getEuclidDistance(qRand,qNear) 

def main():
    # Create list of graph points (vertices)
    nodes = []
    # initialise qInit
    qInit = np.array([xDim/2.0,yDim/2.0])
    #Create list of  initial congiruation point qNear
    nodes.append(qInit) 
    
    # let's plot the trees:
    verts = []
    codes = []
    
    for node in range(numNodes):
        qRand = np.array([random.randint(0, xDim), random.randint(0, yDim)])
        #print(qRand)
        # get qNear from a the nodes list
        qNear = nearestPoint(qRand, nodes)
        #print(qNear)
        #print(qNear)
        #print(qRand)
        qNew =  getSteeringDistance(qRand,qNear)
        #print(qNew)
        nodes.append(qNew)
        #print(nodes)
        verts.append(qNear)
        verts.append(qNew)
        codes.append(Path.MOVETO)
        codes.append(Path.LINETO)
    fig = mp.figure()
    path = Path(verts, codes)
    patch = patches.PathPatch(path)
    ax = fig.add_subplot(111)
    ax.add_patch(patch)
    ax.set_xlim([0,xDim])
    ax.set_ylim([0,yDim])
    mp.show()
    #print(qNew)
    print(nodes)

if __name__ == '__main__':
    main()


