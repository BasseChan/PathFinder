import math
import random

from A_star import *


def getN(stops):
    neighbours = []
    for i in range(len(stops)):
        for j in range(i + 1, len(stops)):
            neighbour = stops.copy()
            neighbour[i] = stops[j]
            neighbour[j] = stops[i]
            neighbours.append(neighbour)
    return neighbours


class Tabu:
    def __init__(self, graph):
        self.graph = graph
        self.aStar = A_star(graph)

    def getCost(self, start, stops, method, startTime):
        prev = start
        curTime = startTime
        cost = 0
        prevEdge = None
        for stop in stops:
            endNode, _, _, _, _, _ = self.aStar.a_star(prev, stop, method, curTime, prevEdge)
            prevEdge = endNode.pEdge
            cost += endNode.g
            curTime = timeToString(endNode.pEdge.endTime)
            prev = stop
        endNode, _, _, _, _, _ = self.aStar.a_star(prev, start, method, curTime, prevEdge)
        cost += endNode.g
        return cost

    def printSolutionTabu(self, start, solution, cost, method, startTime, compileTime):
        prev = start
        curTime = startTime
        prevEdge = None
        for stop in solution:
            endNode, _, _, _, _, _ = self.aStar.a_star(prev, stop, method, curTime, prevEdge)
            prevEdge = endNode.pEdge
            printRoad(endNode)
            curTime = timeToString(endNode.pEdge.endTime)
            prev = stop
        endNode, _, _, _, _, _ = self.aStar.a_star(prev, start, method, curTime, prevEdge)
        printRoad(endNode)
        time.sleep(0.1)
        if method == 't':
            sys.stderr.write(f"Potrzebny czas to: {deltaTimeToString(cost)}\n")
        if method == 'p':
            sys.stderr.write(f"Liczba przesiadek: {cost // 1440 - 1}\n")
        sys.stderr.write(f"Czas obliczeń: {compileTime}s\n")

    def getDistance(self, stops):
        stopDict = {}
        for stop in stops:
            node = self.graph.nodes[stop]
            for stop2 in stops:
                node2 = self.graph.nodes[stop2]
                stopDict[(stop, stop2)] = math.sqrt((node.x - node2.x) ** 2 + (node.y - node2.y) ** 2)
        return stopDict

    def getTotalDistance(self, distance, solution):
        distanceSum = 0
        for i in range(len(solution) - 1):
            distanceSum += distance[(solution[i], solution[i + 1])]
        return distanceSum

    def tabu(self, start, stopsToVisitString, method, startTime):

        stopperStart = time.time()
        STEP_LIMIT = 5
        OP_LIMIT = 3
        T = []
        sBestLocal = stopsToVisitString.split(";")
        distance = self.getDistance(sBestLocal + [start])
        sBestLocalCost = self.getCost(start, sBestLocal, method, startTime)
        maxT = math.factorial(len(sBestLocal) - 1)
        random.shuffle(sBestLocal)
        sDistance = self.getTotalDistance(distance, sBestLocal)
        sBest = sBestLocal
        sBestCost = sBestLocalCost

        for k in range(STEP_LIMIT):
            for i in range(OP_LIMIT):
                N = getN(sBestLocal)
                # print('a', len(N))
                bestN = None
                bestNCost = float('inf')
                counterT = 0
                for n in N:
                    if n not in T:
                        curDistance = self.getTotalDistance(distance, n)
                        if curDistance < 1.2 * sDistance:
                            T.append(n)
                            if len(T) > maxT:
                                T.pop(0)
                                # print("usuwam")
                            nCost = self.getCost(start, n, method, startTime)
                            if nCost < bestNCost:
                                bestN = n
                                bestNCost = nCost
                        # else:
                        #     print("pomijam")
                    else:
                        counterT += 1

                # print(len(T))
                if bestNCost < sBestLocalCost:
                    sBestLocal = bestN
                    sDistance = self.getTotalDistance(distance, sBestLocal)
                    sBestLocalCost = bestNCost

                if counterT == len(N):
                    random.shuffle(sBestLocal)
                    sBestLocalCost = self.getCost(start, sBestLocal, method, startTime)
                    # print("mieszam")
            if sBestLocalCost < sBestCost:
                sBest = sBestLocal
                sBestCost = sBestLocalCost
        stopperEnd = time.time()
        self.printSolutionTabu(start, sBest, sBestCost, method, startTime, stopperEnd - stopperStart)
