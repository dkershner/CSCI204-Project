''' Dan Kershner
    This file has the Document class with functions to generate a document object
    from a given file.
'''
from DocumentStream import *
from Sentence import *

class Document:
    
    def __init__(self, filename):
        self.filename = filename
        self.title = ''
        self.author = None
        self.genre = ''
        self.year = ''
        self.topN = ''
        self.bottomN = ''
        self.__sentences = []
        self.__id = None #something here
        self.__wordCount = 0
        self.__lineCount = 0
        self.__charCount = 0

    def getSentences(self):
        return self.__sentences

    def setSentences(self, sentences):
        self.__sentences = sentences

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getCharCount(self):
        return self.__charCount

    def setCharCount(self):
        charCount = 0
    
        for sentence in self.__sentences:
            charCount += sentence.charCount
            
        self.__charCount = charCount

    def generateWhole(self):
        try:
            documentStream = DocumentStream(self.filename)
        except DocumentStreamError as E:
            print(E.data)
            
        self.setSentences(documentStream.readWhole())
        self.setWordCount()
        self.setLineCount()
        self.setCharCount()

    def getWordCount(self):
        return self.__wordCount

    def setWordCount(self):
        wordCount = 0
    
        for sentence in self.__sentences:
            wordCount += sentence.wordCount
            
        self.__wordCount = wordCount
    
    def getLineCount(self):
        return self.__lineCount

    def setLineCount(self):
        self.__lineCount = len(self.__sentences)

    def getWords(self):
        words = []
        for sentence in self.__sentences:
            words.extend(sentence.parseWords())

        return words
