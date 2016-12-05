''' Dan Kershner
    This file has a Max and Min heap class with methods including fixUp, add,
    remove, and fixDown.
'''

def exchange(a, i , j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def parent_1(i):
    return i // 2

def left_1(i):
    return 2*i

def right_1(i):
    return 2*i+1

class MinHeap():
    def __init__(self, n, tree=None, end=0):
        self.n = n #Size of all storage space
        self.end = end #Current location in
        self.tree = tree
        if self.tree == None:
            self.tree = [None]*self.n
            
    def fixUp(self, a, i, n):
        while i > 1 and a[parent_1(i)].value > a[i].value:
            exchange(a,i,parent_1(i))
            i = parent_1(i)

    def heapAdd(self, item):
        self.end +=1
        if(self.end < self.n):
            self.tree[self.end] = item
            self.fixUp(self.tree, self.end, self.end+1)

    def fixDown(self, a,i, n):
        while left_1(i) < n:
            j = left_1(i)
            if (j+1 < n) and (a[j].value > a[j+1].value):
                j+=1
            if not (a[i].value > a[j].value):
                break
            exchange(a,i,j)
            i = j

    def heapRemove(self):
        if self.end == 0:
            return False
        t = self.tree[1]
        exchange(self.tree, 1, self.end)
        self.fixDown(self.tree, 1, self.end)
        self.end -= 1
        return t

class MaxHeap():
    def __init__(self, n, tree=None, end=0):
        self.n = n #Size of all storage space
        self.end = end #Current location in
        self.tree = tree
        if self.tree == None:
            self.tree = [None]*self.n
            
    def fixUp(self, a, i, n):
        while i > 1 and a[parent_1(i)].value < a[i].value:
            exchange(a,i,parent_1(i))
            i = parent_1(i)

    def heapAdd(self, item):
        self.end +=1
        if(self.end < self.n):
            self.tree[self.end] = item
            self.fixUp(self.tree, self.end, self.end+1)

    def fixDown(self, a,i, n):
        while left_1(i) < n:
            j = left_1(i)
            if (j+1 < n) and (a[j].value < a[j+1].value):
                j+=1
            if not (a[i].value < a[j].value):
                break
            exchange(a,i,j)
            i = j

    def heapRemove(self):
        if self.end == 0:
            return False
        t = self.tree[1]
        exchange(self.tree, 1, self.end)
        self.fixDown(self.tree, 1, self.end)
        self.end -= 1
        return t
    
class HeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
