import time
import pandas as pd
from Graph import *
from Dijkstra import *
from A_star import *
from Tabu import *

print("Wczytywanie danych...")

df = pd.read_csv('connection_graph.csv')

graph = Graph()

for index, row in df.iterrows():
    graph.newEdge(row[3], row[4], row[5], row[6], row[8], row[9], row[7], row[10], row[11])

working = True
while working:
    time.sleep(1)
    print("\n\nWybierz operację:\n1 - dijkstra\n2 - A* z kryterium czasu\n3 - A* z kryterium przesiadek\n"
          "4 - tabu z kryterium czasu\n5 - tabu z ktyterium przesiadek\ninne - wyjście")
    option = input()
    match option:
        case "1":
            print("Podaj przystanek początkowy")
            start = input()
            print("Podaj przystanek końcowy")
            end = input()
            print("Podaj godzinę startową")
            startTime = input()
            dijkstra = Dijkstra(graph)
            dijkstra.dijkstra(start, end, startTime)
        case "2":
            print("Podaj przystanek początkowy")
            start = input()
            print("Podaj przystanek końcowy")
            end = input()
            print("Podaj godzinę startową")
            startTime = input()
            aStar = A_star(graph)
            endNode, compileTime, start, stop, timeStart, method = aStar.a_star(start, end, "t", startTime)
            printSolution(endNode, compileTime, start, stop, timeStart, method)
        case "3":
            print("Podaj przystanek początkowy")
            start = input()
            print("Podaj przystanek końcowy")
            end = input()
            print("Podaj godzinę startową")
            startTime = input()
            aStar = A_star(graph)
            endNode, compileTime, start, stop, timeStart, method = aStar.a_star(start, end, "p", startTime)
            printSolution(endNode, compileTime, start, stop, timeStart, method)
        case "4":
            print("Podaj przystanek początkowy")
            start = input()
            print("Podaj pośrednie przystanki oddzielone ;")
            stops = input()
            print("Podaj godzinę startową")
            startTime = input()
            tabu = Tabu(graph)
            tabu.tabu(start, stops, "t", startTime)
        case "5":
            print("Podaj przystanek początkowy")
            start = input()
            print("Podaj pośrednie przystanki oddzielone ;")
            stops = input()
            print("Podaj godzinę startową")
            startTime = input()
            tabu = Tabu(graph)
            tabu.tabu(start, stops, "p", startTime)
        case _:
            working = False
