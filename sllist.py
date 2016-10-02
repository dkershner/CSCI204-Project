class Node:
    next = None
    data = None

class sllist:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        return self.size


    def add(self, value):
        if(len(self.elist) > 0):
            newNode = Node()
            newNode.data = value
            newNode.next = self.head
            self.head = newNode
            self.size += 1

    def remove(self, value):
        prevNode = None 
        curNode = self.head
        while curNode != None and curNode.data != value:
            prevNode = curNode
            curNode = curNode.next
        
        if curNode == None:
            return -1

        if curNode == self.head:
            self.head = curNode.next
        else:
            prevNode.next = curNode.next

    
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
            self.runner = self.runner.next
            return item
