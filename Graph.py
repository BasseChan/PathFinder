from collections import deque
from datetime import datetime


def timeToInt(time):
    timeSplit = time.split(":")
    timeInt = int(timeSplit[0]) * 60 + int(timeSplit[1])
    return timeInt


def timeToString(time):
    timeString = ""
    h = (time // 60) % 24
    m = time % 60
    if h < 10:
        timeString += "0"
    timeString += str(h) + ":"
    if m < 10:
        timeString += "0"
    timeString += str(m)
    return timeString


def deltaTimeToString(delta):
    h = (delta // 60) % 24
    m = delta % 60
    return f"{h} godz {m} min"


def costT(start, rideStart, rideEnd):
    start2 = start % 1440
    rideStart2 = rideStart % 1440
    rideEnd2 = rideEnd % 1440
    if start2 <= rideStart2 and start2 < rideEnd2:
        return rideEnd2 - start2
    return rideEnd2 - start2 + 1440


class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.stops = []

    def addStop(self, endNode, line, startTime, endTime):
        self.stops.append(Edge(endNode, line, startTime, endTime))

    def __str__(self):
        s = f"{self.name}, {self.x}, {self.y}, ["
        for stop in self.stops:
            s += str(stop) + ", "
        return s + "]"
        # return self.name + " " + self.x + " " + self.y + " " + self.stops


class Edge:
    def __init__(self, endNode, line, startTime, endTime):
        self.endNode = endNode
        self.line = line
        self.startTime = timeToInt(startTime)
        self.endTime = timeToInt(endTime)

    def __str__(self):
        return f"{self.endNode.name} {self.line} {timeToString(self.startTime)} {timeToString(self.endTime)}"


class Graph:
    def __init__(self):
        self.nodes = {}

    def newEdge(self, line, startTime, endTime, name1, x1, y1, name2, x2, y2):
        self.nodes.setdefault(name1, Node(name1, x1, y1))
        self.nodes.setdefault(name2, Node(name2, x2, y2))
        self.nodes[name1].addStop(self.nodes[name2], line, startTime, endTime)

# class Graph:
#     def __init__(self, adjac_lis):
#         self.adjac_lis = adjac_lis
#
#     def get_neighbors(self, v):
#         return self.adjac_lis[v]
#
#     # This is heuristic function which is having equal values for all nodes
#     def h(self, n):
#         H = {
#             'A': 1,
#             'B': 1,
#             'C': 1,
#             'D': 1
#         }
#
#         return H[n]
#
#     def aStarAlgorythm(self, start, finish):
#         start.g = 0
#         start.h = 0
#         start.f = start.g + start.h
#
#         opened = set([start])
#         closed = set([])
#
#         while len(opened) > 0:
#             node = None
#             cost = float('inf')
#
#             for testNode in opened:
#                 if f(testNode) < cost:
#                     node = testNode
#
#     def a_star_algorithm(self, start, finish):
#         # In this opened is a lisy of nodes which have been visited, but who's
#         # neighbours haven't all been always inspected, It starts off with the start
#         # node
#         # And closed is a list of nodes which have been visited
#         # and who's neighbors have been always inspected
#         opened = set([start])
#         closed = set([])
#
#         # distance has present distances from start to all other nodes
#         # the default value is +infinity
#         distance = {}
#         distance[start] = 0
#
#         # par contains an adjac mapping of all nodes
#         par = {}
#         par[start] = start
#
#         while len(opened) > 0:
#             node = None
#
#             # it will find a node with the lowest value of f() -
#             for testNede in opened:
#                 if node == None or distance[testNede] + self.h(testNede) < distance[node] + self.h(node):
#                     node = testNede;
#
#             if node == None:
#                 print('Path does not exist!')
#                 return None
#
#             # if the current node is the stop
#             # then we start again from start
#             if node == finish:
#                 reconst_path = []
#
#                 while par[node] != node:
#                     reconst_path.append(node)
#                     node = par[node]
#
#                 reconst_path.append(start)
#
#                 reconst_path.reverse()
#
#                 print('Path found: {}'.format(reconst_path))
#                 return reconst_path
#
#             # for all the neighbors of the current node do
#             for (m, weight) in self.get_neighbors(node):
#                 # if the current node is not presentin both opened and closed
#                 # add it to opened and note n as it's par
#                 if m not in opened and m not in closed:
#                     opened.add(m)
#                     par[m] = node
#                     distance[m] = distance[node] + weight
#
#                 # otherwise, check if it's quicker to first visit n, then m
#                 # and if it is, update par data and distance data
#                 # and if the node was in the closed, move it to opened
#                 else:
#                     if distance[m] > distance[node] + weight:
#                         distance[m] = distance[node] + weight
#                         par[m] = node
#
#                         if m in closed:
#                             closed.remove(m)
#                             opened.add(m)
#
#             # remove n from the opened, and add it to closed
#             # because all of his neighbors were inspected
#             opened.remove(node)
#             closed.add(node)
#
#         print('Path does not exist!')
#         return None
#
#
# adjac_lis = {
#     'A': [('B', 1), ('C', 3), ('D', 7)],
#     'B': [('D', 5)],
#     'C': [('D', 12)]
# }
# graph1 = Graph(adjac_lis)
# graph1.a_star_algorithm('A', 'D')
