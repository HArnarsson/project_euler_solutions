# Project Euler - 107
# Date: 26/07/2022

from math import inf

# We will simply implement prims algorithm for an adjacency matrix

# Pseudocode for Prim:
# 1: Make a list of visited nodes
# 2: Choose a starting node
# 3: Choose the cheapest edge conncted to the visited nodes and add it to the mst (minimum spanning tree)
# 4: Add that node to the visited list
# 5: Go back to 3 until all nodes are visited
# 6: The mst is the optimal graph (unique if no two edges have the same cost) -> we don't care since we are only looking for the maximum savings

# Note that the adjacency matrix has duplicate vertex costs

with open("lib/100-200/peuler_resource107.txt","r") as file:
    adj_matrix = []
    for row in file:
        adj_matrix.append(row[:-1].split(","))
for i in range(len(adj_matrix)):
    adj_matrix[i] = [int(adj_matrix[i][j]) if adj_matrix[i][j] != "-" else 0 for j in range(len(adj_matrix[i]))]

# This alg was mostly from geeks for geeks with some tweaks 
# Link: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
class Graph():

    def __init__(self, vertices:int):
        self.vertices = vertices
        self.graph = [[0 for _column in range(vertices)] for _row in range(vertices)]

    def min_node(self, keys, mstSet):
        min = float(inf)

        for v in range(self.vertices):
            if keys[v] < min and not mstSet[v]:
                min = keys[v]
                min_index = v
        return min_index
    
    def get_weight_mst(self, parent):
        weight = 0
        for i in range(1,self.vertices):
            weight += self.graph[i][parent[i]]
        return weight

    
    def prims_alg(self):
        keys = [float(inf)]*self.vertices
        parent = [None]*self.vertices
        keys[0] = 0
        mstSet = [False]*self.vertices
        parent[0] = -1

        for smth in range(self.vertices):
            u = self.min_node(keys, mstSet)
            mstSet[u] = True

            for v in range(self.vertices):
                if self.graph[u][v]>0 and not mstSet[v] and keys[v] > self.graph[u][v]:
                    keys[v] = self.graph[u][v]
                    parent[v] = u

        return self.get_weight_mst(parent)

g = Graph(len(adj_matrix))
g.graph = adj_matrix

weight_adj_matrix = 0

for i in range(len(adj_matrix)):
    for j in range(i, len(adj_matrix)):
        weight_adj_matrix += adj_matrix[i][j]

weight_mst = g.prims_alg()

print(weight_adj_matrix-weight_mst)
