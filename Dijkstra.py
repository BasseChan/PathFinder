import sys
import time

from Graph import *


class DijkstraNode:
    def __init__(self, node):
        self.node = node
        self.d = float('inf')
        self.p = None
        self.pEdge = None

    def resetNode(self):
        self.d = float('inf')
        self.p = None
        self.pEdge = None


class Dijkstra:
    def __init__(self, graph):
        self.stops = {}
        self.Q = []
        for keys, value in graph.nodes.items():
            self.stops[keys] = DijkstraNode(value)

    def reset(self):
        self.Q = []
        for keys, value in self.stops.items():
            value.resetNode()
            self.Q.append(value)

    def printRoadHelper(self, stop, line, startTime):
        edge = stop.pEdge
        prev = stop.p
        if edge is None:
            print(f"Linia {line}: {stop.node.name} {timeToString(startTime)} - ", end="")
        else:
            if edge.line == line:
                self.printRoadHelper(prev, line, edge.startTime)
            else:
                self.printRoadHelper(prev, edge.line, edge.startTime)
                print(f"{timeToString(edge.endTime)} {stop.node.name}")
                print(f"Linia {line}: {stop.node.name} {timeToString(startTime)} - ", end="")

    def printRoad(self, stop):
        edge = stop.pEdge
        prev = stop.p
        self.printRoadHelper(prev, edge.line, edge.startTime)
        print(f"{timeToString(edge.endTime)} {stop.node.name}")

    def dijkstra(self, start, stop, timeStart):
        stopperStart = time.time()
        self.reset()
        self.stops[start].d = 0
        timeInt = timeToInt(timeStart)

        while self.Q:
            uMin = self.Q[0]
            dMin = self.Q[0].d
            for u in self.Q:
                if u.d < dMin:
                    uMin = u
                    dMin = u.d
            self.Q.remove(uMin)
            for v in uMin.node.stops:
                vNode = self.stops[v.endNode.name]
                if vNode.d > uMin.d + costT(timeInt + uMin.d, v.startTime, v.endTime):
                    vNode.d = uMin.d + costT(timeInt + uMin.d, v.startTime, v.endTime)
                    vNode.p = uMin
                    vNode.pEdge = v
        stopperEnd = time.time()
        print(f"{start} -> {stop}, godz: {timeStart}")
        self.printRoad(self.stops[stop])
        sys.stderr.write(f"Potrzebny czas to: {deltaTimeToString(self.stops[stop].d)}\n")
        sys.stderr.write(f"Czas obliczeń: {stopperEnd - stopperStart}s\n")
