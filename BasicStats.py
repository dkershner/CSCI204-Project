''' Dan Kershner
    This file has the BasicStats class which includes functions createFreqMap,
    topN, and bottomN (along with different implementations of these).
'''
from sllist import *
from SStack import *
from Heap import *

class BasicStats:

    @staticmethod
    def createFreqMap(aList):
        ''' Returns a dictionary with each key being a unique word in the given
            list and each value being the number of times that word appears.
        '''
        dictionary = {}
        for x in aList:
            x.lower()
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

        return dictionary

    def topN(self, dictionary, num):
        ''' Returns a dictionary of the top N words and their frequencies.
        '''
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
        ''' Returns a dictionary of the bottom N words and their frequencies.
        '''
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
        myList = Sllist()
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
        ''' Uses a heap to return a dictionary of the top N words and their frequencies
        '''
        heap = MaxHeap(10000)
        ##print(dictionary)
        for x in dictionary:
            node = HeapNode(x, dictionary[x])
            heap.heapAdd(node)
        output = {}
        for i in range(num):
            node = heap.heapRemove()
            output[node.key] = node.value

        return output

    @staticmethod
    def bottomNHeap(dictionary, num):
        ''' Uses a heap to return a dictionary of the bottom N words and their frequencies
        '''
        heap = MinHeap(10000)
        myHeap = []
        for x in dictionary:
            node = HeapNode(x, dictionary[x])
            heap.heapAdd(node)
        output = {}
        for i in range(num):
            node = heap.heapRemove()
            output[node.key] = node.value

        return output
