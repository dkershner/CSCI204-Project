''' Dan Kershner
    This file has the Stack class which uses a singly linked list and has methods
    push and pop.
'''
from sllist import *

class SStack:
    def __init__(self):
        self.__myList = Sllist()
        self.size = 0

    def push(self, values):
        self.__myList.add(values)
        self.size += 1

    def pop(self):
        t = self.__myList.head.data
        self.__myList.head = self.__myList.head.next[0]
        return t
