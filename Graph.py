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
