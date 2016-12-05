''' Dan Kershner
    This file has the Tree class along with the ID3 function (and associated helpers).
'''
import math

class Tree:
    def __init__(self):
        self.root = None

    def train(self, data, titles, maxDepth):
        self.root = ID3(self.root, data, titles, maxDepth)
        

    def evaluate(self, data, attributes, currentNode):
        if currentNode == None:
            print('There is not a node here.')
            return None
        if currentNode.children == []:
            return currentNode.attribute
        column = attributes.index(self.root.attribute)
        myAttribute = data[column]
        for child in currentNode.children:
            if child.attribute is int:
                year = child.attribute
                if myAttribute >= year-5 and myAttribute <= year+5:
                    self.evaluate(data, attributes, child)
            elif child.attribute == myAttribute:
                self.evaluate(data, attributes, child)
        self.evaluate(data, attributes, currentNode.children[0])

class TreeNode:
    def __init__(self, attribute):
        self.attribute = attribute
        self.children = []
        self.numDocs = 0

def ID3(root, data, attributes, depth):
    if data == [[]]:
        return False
    holder = data[0][0]
    condition = True
    for x in data:
        if holder != x[0]:
            condition = False
    if condition == True or depth == 0:
        return TreeNode(holder)
    if not atrributes:
        dictionary = {}
        for x in data:
            if x[0] in dictionary:
                dictionary[x[0]] += 1
            else:
                dictionary[x[0]] = 1

        values = list(dictionary.values())
        keys = list(dictionary.keys())
        maximum = max(values)
        index = values.index(maximum)
        author = keys[index]
        return TreeNode(author)
    ##compute gains
    gains = gain(data, attributes)
    ##select largest gain => which label (might be year)
    column = gains.index(max(gains)) + 1
    cList = splitData(data, attributes, column) #returns a list of 2DList partitioned by selected question
    node = TreeNode(attributes[column])
    newLabels = attributes[:column] + attributes[column + 1:]
    for x in cList:
        node.children[x] = id3(node, cList[x], newLabels, depth-1)

def gain(data, attributes):
    t_cert = certainty(data, 0)
    gains = []
    for i in range(1, len(attributes)):
        t = certainty(data, i)
        g = t_cert - t
        gains.append(g)
    return gains

def certainty(data, column):
    total = len(data)
    possibleAttributes = {}
    for row in data:
        if row[column] in dictionary:
            dictionary[row[column]] += 1
        else:
            dictionary[row[column]] = 1
    cert = 0
    possibilities = len(dictionary)
    for key in dictionary:
        fraction = dictionary[key]/possibilities
        cert -= (fraction)*math.log2(fraction)
    return cert

def splitData(data, attributes, column):
    children = {}
    for row in data:
        if row[column] in children:
            children[row[column]] += row[:column] + row[column + 1:]
        else:
            children[row[column]] = row[:column] + row[column + 1:]
            
    return children        
