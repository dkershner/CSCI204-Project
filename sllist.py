''' Dan Kershner
    This file has the linked list class (Sllist) with methods including add and remove.
'''
class Node:
    next = []
    data = []

class Sllist:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        return self.size


    def add(self, values):
        if(len(self.elist) > 0):
            newNode = Node()
            newNode.data = values
            newNode.next.append(self.head)
            self.head = newNode
            self.size += 1

    def remove(self, value):
        prevNode = None 
        curNode = self.head
        while curNode != None and curNode.data[0] != value:
            prevNode = curNode
            curNode = curNode.next[0]
        
        if curNode == None:
            return -1

        if curNode == self.head:
            self.head = curNode.next[0]
        else:
            prevNode.next[0] = curNode.next[0]

    
    def __iter__(self):
        return sllistIterator(self.head)


class sllistIterator:
    
    def __init__(self, head):
        self.runner = head

    
    def __iter__(self):
        return self


    def __next__(self):
        if self.runner == None:
            raise StopIteration
        else:
            item = self.runner.data
            self.runner = self.runner.next[0]
            return item
