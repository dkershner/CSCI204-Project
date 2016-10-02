import os
import math
import random
import copy

class CommandLinePloter:

    def __init__(self, xMin, xMax, yMin, yMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.yFactor = self.getYFactor()
        self.xFactor = self.getXFactor()
        self.plane = self.generatePlane()

    def generatePlane(self):
        plane = []
        for i in range(math.ceil(self.yMax / self.yFactor), self.yMin - 2, -1):
            row = []
            ylabel = i * self.yFactor
            #add spacing along y-axis so they all line up
            shift = len(str(self.yMax)) - len(str(ylabel))
            row = [' '] * shift
            if i <= 0:
                row = [' '] * len(str(self.yMax))
            for j in range(self.xMin, math.ceil(self.xMax / self.xFactor) + 1):
                if(i < self.yMin):
                    row.append(j * self.xFactor)
                elif (i == self.yMin):
                    row.append('-')
                elif(j <= self.xMin):
                    row.extend(list(str(ylabel)))
                    row.append('|')
                else:
                    row.append(' ')
            plane.append(row)

        return plane

    def printOut(self, graph):
        output = ''
        for i in graph:
            for j in i:
                output += str(j)
            output += '\n'
        print(output)
        
            
    def getYFactor(self):
        try:
            lines = os.get_terminal_size().lines            
        except Exception:
            lines = 10
        factor = math.ceil(self.yMax / lines)
        return factor

    def getXFactor(self):
        try:
            lines = os.get_terminal_size().columns            
        except Exception:
            lines = 10
        factor = math.ceil(self.xMax / lines)
        return factor
        
    def d2Scatter(self, list1, list2 = None):
        if(list2):
            output = copy.deepcopy(self.plane)
            xCoordinates = list1
            yCoordinates = list2
            for i in range(len(xCoordinates)):
                x = xCoordinates[i]
                y = yCoordinates[i]
                realY = math.ceil((self.yMax - y)/self.yFactor)
                realX = math.ceil((abs(self.xMin - x))/self.xFactor)
                output[realY][realX + len(str(self.yMax))] = 'X'
                
            self.printOut(output)

        else:
            xCoordinates = list(range(1, len(list1) + 1))
            self.d2Scatter(xCoordinates, list1)

    def barGraph(self, list1, list2 = None):
        if(list2):
            output = copy.deepcopy(self.plane)
            xCoordinates = list1
            yCoordinates = list2
            for i in range(len(xCoordinates)):
                x = xCoordinates[i]
                y = yCoordinates[i]
                realY = math.ceil((self.yMax - y)/self.yFactor)
                realX = math.ceil((abs(self.xMin - x))/self.xFactor)
                for column in range(len(output[0])):
                    character = chr(random.randint(33, 126))
                    for row in range(len(output) - 2):                        
                        if row >= realY and column == realX:
                            output[row][column + len(str(self.yMax))] = character

            self.printOut(output)

        else:
            xCoordinates = list(range(1, len(list1) + 1))
            self.barGraph(xCoordinates, list1)
