from sllist import *

class SStack:
    def __init__(self):
        self.__myList = sllist()
        self.size = 0

    def push(self, values):
        self.__myList.add(values)
        self.size += 1

    def pop(self):
        t = self.__myList.head.data
        self.__myList.head = self.__myList.head.next[0]
        return t
