
import sys
import time

from Graph import *


def printRoadHelper(stop, line, startTime):
    edge = stop.pEdge
    prev = stop.p
    if prev is None:
        print(f"Linia {line}: {stop.node.name} {timeToString(startTime)} - ", end="")
    else:
        if edge.line == line:
            printRoadHelper(prev, line, edge.startTime)
        else:
            printRoadHelper(prev, edge.line, edge.startTime)
            print(f"{timeToString(edge.endTime)} {stop.node.name}")
            print(f"Linia {line}: {stop.node.name} {timeToString(startTime)} - ", end="")


def printRoad(stop):
    edge = stop.pEdge
    if edge is not None:
        prev = stop.p
        printRoadHelper(prev, edge.line, edge.startTime)
        print(f"{timeToString(edge.endTime)} {stop.node.name}")
    else:
        print("Nie znaleziono trasy")


def printSolution(endNode, compileTime, start, stop, timeStart, method):
    print(f"{start} -> {stop}, godz: {timeStart}\n")
    printRoad(endNode)
    time.sleep(0.1)
    if method == 't':
        sys.stderr.write(f"Potrzebny czas to: {deltaTimeToString(endNode.g)}\n")
    if method == 'p':
        sys.stderr.write(f"Liczba przesiadek: {endNode.g // 1440 - 1}\n")
    sys.stderr.write(f"Czas obliczeń: {compileTime}s\n")


class A_starNode:
    def __init__(self, node):
        self.node = node
        self.g = 0
        self.g2 = 0
        self.h = 0
        self.p = None
        self.pEdge = None


class A_star:
    def __init__(self, graph):
        self.stops = {}
        for keys, value in graph.nodes.items():
            self.stops[keys] = A_starNode(value)

    def g(self, start, g, edge):
        return costT(start + g, edge.startTime, edge.endTime)

    def g2(self, prev, edge):
        if prev.pEdge is None:
            return 1440
        if prev.pEdge.line == edge.line and prev.pEdge.endTime == edge.startTime:
            return 0
        return 1440

    def h(self, node1, node2):
        x1 = node1.node.x
        y1 = node1.node.y
        x2 = node2.node.x
        y2 = node2.node.y
        deltaX = abs(x1 - x2)
        deltaY = abs(y1 - y2)
        # delta = math.sqrt(deltaX ** 2 + deltaY ** 2)
        delta = deltaX + deltaY
        return delta / 0.011117

    def h2(self):
        return 0

    def a_star(self, start, stop, method, timeStart, prevEdge=None):
        stopperStart = time.time()
        timeInt = timeToInt(timeStart)
        endNode = self.stops[stop]
        endNode.p = None
        endNode.pEdge = None
        startNode = self.stops[start]
        startNode.g = 0
        startNode.g2 = 0
        startNode.h = 0
        startNode.p = None
        startNode.pEdge = prevEdge
        opened = [startNode]
        closed = []
        while opened:
            node = None
            cost = float('inf')
            cost2 = float('inf')
            for testNode in opened:
                if testNode.g + testNode.h < cost or \
                        (testNode.g + testNode.h == cost and testNode.g2 + testNode.h < cost2):
                    node = testNode
                    cost = testNode.g + testNode.h
                    cost2 = testNode.g2 + testNode.h
            if node == endNode:
                opened.clear()
            else:
                opened.remove(node)
                closed.append(node)
                for nextEdge in node.node.stops:
                    nextNode = self.stops[nextEdge.endNode.name]
                    if method == 't':
                        curG = node.g + self.g(timeInt, node.g, nextEdge)
                        curG2 = node.g2 + self.g2(node, nextEdge)
                    else:
                        curG2 = node.g2 + self.g(timeInt, node.g2, nextEdge)
                        curG = node.g + self.g2(node, nextEdge)
                    if nextNode not in opened and nextNode not in closed:
                        opened.append(nextNode)
                        nextNode.h = self.h(nextNode, endNode)
                        nextNode.g = curG
                        nextNode.g2 = curG2
                        nextNode.p = node
                        nextNode.pEdge = nextEdge
                    elif nextNode.g > curG or (nextNode.g == curG and nextNode.g2 > curG2):
                        nextNode.g = curG
                        nextNode.g2 = curG2
                        nextNode.p = node
                        nextNode.pEdge = nextEdge
                        if nextNode in closed:
                            opened.append(nextNode)
                            closed.remove(nextNode)
        # print(endNode.g, endNode.g2)
        stopperEnd = time.time()
        return endNode, (stopperEnd - stopperStart), start, stop, timeStart, method

