# Project Euler - 81
# Date: 22/06/2022

# This dijkstra alg is shit, a better one is demonstrated in problem 83

from queue import PriorityQueue
from time import time
start = time()
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = set()

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 4445

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.add(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

array = []
with open("C:\\Temp\\working_directory\\matrix.txt") as matrix:
    for row in matrix:
        röð = row.split(",")
        röð = [int(stak) for stak in röð]
        array.append(röð)

def get_index_from_pos(i,j):
    return i*80+j

graph = Graph(80**2)
for i in range(79):
    for j in range(79):
        index = get_index_from_pos(i,j)
        graph.add_edge(index, index+1, array[i][j+1])
        graph.add_edge(index, index+80, array[i+1][j])

for i in range(79):
    graph.add_edge(79+i*80,(i+1)*80+79, array[i][79])

for i in range(80**2-80,80**2-1):
    graph.add_edge(i,i+1,array[79][i-80**2+80+1])

D = dijkstra(graph,0)
print(D[80**2-1])
print(time)