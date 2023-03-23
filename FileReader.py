import pandas as pd
from Graph import *
from Dijkstra import *
from A_star import *
from Tabu import *

df = pd.read_csv('connection_graph.csv')

graph = Graph()

for index, row in df.iterrows():
    graph.newEdge(row[3], row[4], row[5], row[6], row[8], row[9], row[7], row[10], row[11])

dijkstra = Dijkstra(graph)
print("dijkstra")
dijkstra.dijkstra("C.H. Korona", "Na Ostatnim Groszu", "12:20")

a_star = A_star(graph)

print("A*")
endNode, compileTime, start, stop, timeStart, method = \
    a_star.a_star("C.H. Korona", "Na Ostatnim Groszu", 't', "12:20")
printSolution(endNode, compileTime, start, stop, timeStart, method)

print("A*")
endNode, compileTime, start, stop, timeStart, method = \
    a_star.a_star("C.H. Korona", "Na Ostatnim Groszu", 'p', "12:20")
printSolution(endNode, compileTime, start, stop, timeStart, method)

tabu = Tabu(graph)

print("Tabu")
tabu.tabu("Nowy Dwór", "Na Ostatnim Groszu;C.H. Korona;PL. GRUNWALDZKI;Psie Pole;Morwowa", "t", "15:10")
print('\n\n')
tabu.tabu("Nowy Dwór", "Na Ostatnim Groszu;C.H. Korona;PL. GRUNWALDZKI;Psie Pole;Morwowa", "p", "15:10")
