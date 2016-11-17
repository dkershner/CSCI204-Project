from sllist import *
from SStack import *
from Heap import *

class BasicStats:

    @staticmethod
    def createFreqMap(aList):
        dictionary = {}
        for x in aList:
            x.lower()
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

        return dictionary

    def topN(self, dictionary, num):
        output = {}
        for x in range(num):
            values = list(dictionary.values())
            keys = list(dictionary.keys())
            maximum = max(values)
            index = values.index(maximum)
            key = keys[index]
            output[key] = maximum
            dictionary.pop(key)

        return output

    def bottomN(self, dictionary, num):
        output = {}
        for x in range(num):
            values = list(dictionary.values())
            keys = list(dictionary.keys())
            minimum = min(values)
            index = values.index(minimum)
            key = keys[index]
            output[key] = minimum
            dictionary.pop(key)

        return output

    @staticmethod
    def slinkFreq(aList):
        ''' This will run in O(n^2) since it has to go through each word and the
            entire linked list for each word.
        '''
        myList = sllist()
        for x in aList:
            x.lower()
            runner = myList.head
            inserted = False
            while runner != None:
                if x == runner.data[0]:
                    runner.data[1] += 1
                    inserted = True
                    break
                runner = runner.next[0]
            if not inserted:
                node = Node()
                node.data.append(x)
                node.data.append(1)
                node.next[0] = myList.head
                myList.head = node                

        return myList

    def slinkTopN(self, head, num):
        output = SStack()
        for x in range(num):
            runner = head
            prevRunner = None
            curMax = head
            prevMax = None
            if runner == None:
                return output
            while runner != None:
                if runner.data > curMax.data:
                    curMax = runner
                    prevMax = prevRunner
                runner = runner.next
                prevRunner = prevRunner.next

            prevMax.next = curMax.next            
            output.push(curMax.data)            

        return output
        
    @staticmethod
    def topNHeap(dictionary, num):
        heap = MaxHeap()
        myHeap = []
        for x in dictionary:
            node = HeapNode(x, dictionary[x])
            heap.heapAdd(myHeap, node)
        output = {}
        for i in range(num):
            output += heap.heapRemove(myHeap)

    @staticmethod
    def bottomNHeap(dictionary, num):
        heap = MinHeap()
        myHeap = []
        for x in dictionary:
            node = HeapNode(x, dictionary[x])
            heap.heapAdd(myHeap, node)
        output = {}
        for i in range(num):
            output += heap.heapRemove(myHeap)
