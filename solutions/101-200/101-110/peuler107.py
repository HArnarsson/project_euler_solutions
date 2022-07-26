# Project Euler - 107
# Date: 26/07/2022

# We will simply implement prims algorithm for an adjacency matrix

# Pseudocode for Prim:
# 1: Make a list of visited nodes
# 2: Choose a starting node
# 3: Choose the cheapest edge conncted to the visited nodes and add it to the mst (minimum spanning tree)
# 4: Add that node to the visited list
# 5: Go back to 3 until all nodes are visited
# 6: The mst is the optimal graph (unique if no two edges have the same cost) -> we don't care since we are only looking for the maximum savings

with open("lib\\101-200\\peuler_resource107.txt","r") as file:
    adj_matrix = []
    for row in file:
        adj_matrix.append(row)

print(adj_matrix[0][:10])

def prims_alg(adj_matrix):
    nodes = [i for i in range(len(adj_matrix))]
    edges = {nodes[i]:adj_matrix[i] for i in range(len(adj_matrix))}
    # make visited a hashmap?
    visited = []
