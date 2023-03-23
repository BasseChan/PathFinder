import pandas as pd
from Graph import *
from Dijkstra import *
from A_star import *
from Tabu import *

df = pd.read_csv('connection_graph.csv')

graph = Graph()

for index, row in df.iterrows():
    graph.newEdge(row[3], row[4], row[5], row[6], row[8], row[9], row[7], row[10], row[11])

# print(df.to_string())

# for index, row in df.iterrows():
#     if timeToInt(row[4]) < 60 * 3:
#         print(row)

# print(df.keys())
# for keys, value in graph.nodes.items():
#     print(value)dfh700sgp ol,

# dijkstra = Dijkstra(graph)
# print("dijkstra")
# dijkstra.dijkstra("TYNIECKA (pętla)", "Żórawina - skrzy. Niepodległości", "10:34")
# # dijkstra.dijkstra("Wyszyńskiego", "Złotnicka", "10:50")
# # dijkstra.dijkstra("Wiejska", "most Grunwaldzki", "10:50")
# print()
#

dijkstra = Dijkstra(graph)
print("dijkstra")
dijkstra.dijkstra("Bezpieczna", "PL. GRUNWALDZKI", "12:20")
a_star = A_star(graph)
print("A*")
endNode, compileTime, start, stop, timeStart, method = \
    a_star.a_star("Bezpieczna", "PL. GRUNWALDZKI", 't', "12:20")
printSolution(endNode, compileTime, start, stop, timeStart, method)
print("A*")
endNode, compileTime, start, stop, timeStart, method = \
    a_star.a_star("Bezpieczna", "PL. GRUNWALDZKI", 'p', "12:20")
# endNode, compileTime, start, stop, timeStart, method = \
#     a_star.a_star("Rogowska", "Psie Pole", 't', "10:34")
printSolution(endNode, compileTime, start, stop, timeStart, method)

# print("A*")
# endNode, compileTime, start, stop, timeStart, method = \
#     a_star.a_star("Bezpieczna", "PL. GRUNWALDZKI", 'p', "12:22")
# # endNode, compileTime, start, stop, timeStart, method = \
# #     a_star.a_star("Rogowska", "Psie Pole", 't', "10:34")
# printSolution(endNode, compileTime, start, stop, timeStart, method)
# # # a_star.a_star("Wyszyńskiego", "Złotnicka", "t", "10:50")
# # # a_star.a_star("Wiejska", "most Grunwaldzki", "t", "10:50")
# # print()
# #
# print("A*")
# # endNode, compileTime, start, stop, timeStart, method = \
# #     a_star.a_star("Bezpieczna", "PL. GRUNWALDZKI", 'p', "10:34")
# endNode, compileTime, start, stop, timeStart, method = \
#     a_star.a_star("Rogowska", "Psie Pole", 'p', "10:34")
# printSolution(endNode, compileTime, start, stop, timeStart, method)
# # a_star.a_star("Wiejska", "most Grunwaldzki", "p", "10:50")

# tabu = Tabu(graph)
#
# # tabu.tabu("Bezpieczna", "Kamienna;Bałtycka;most Grunwaldzki;PL. GRUNWALDZKI", "t", "15:10")
# tabu.tabu("Wiejska", "Bezpieczna;Nowy Dwór;PL. GRUNWALDZKI;Psie Pole;Morwowa", "t", "15:10")
# print('\n\n')
# tabu.tabu("Wiejska", "Bezpieczna;Nowy Dwór;PL. GRUNWALDZKI;Psie Pole;Morwowa", "p", "15:10")
