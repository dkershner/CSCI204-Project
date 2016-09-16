class CommandLinePloter:

    def __init__(self, xMin, xMax, yMin, yMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.plane = self.generatePlane()

    def generatePlane(self):
        plane = []
        for i in range(self.yMax, self.yMin - 1, -1):
            column = []
            for j in range(self.xMin, self.xMax + 1):
                if(i == 0):
                    column.append('-')
                elif(j == 0):
                    column.append('|')
                else:
                    column.append(' ')
            plane.append(column)

        return plane

    def __repr__(self):
        output = ''
        for i in self.plane:
            for j in i:
                output += j
            output += '\n'
        return output
        
            

    def d2Scatter(self, list1, list2 = None):
        if(list2):
            xCoordinates = list1
            yCoordinates = list2
            for i in range(len(xCoordinates)):
                x = xCoordinates[i]
                y = yCoordinates[i]
                self.plane[self.yMax - y][abs(self.xMin - x)] = 'X'
                    

        else:
            xCoordinates = list(range(1, len(list1) + 1))
            yCoordinates = list1
            for i in range(len(xCoordinates)):
                x = xCoordinates[i]
                y = yCoordinates[i]
                self.plane[self.yMax - y][abs(self.xMin - x)] = 'X'

