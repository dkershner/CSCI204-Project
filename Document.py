from DocumentStream import *
from Sentence import *

class Document:
  
  def __init__(self, filename):
    documentStream = DocumentStream(filename)
    self.sentences = documentStream.readWhole()
    self.id = none #something here
    self.wordcount = getWordCount()
    self.linecount = getLineCount()
    self.charcount = charcount
    
  def generateWhole():
    #TODO
  
  def getWordCount():
    if self.wordCount != 0:
      return self.wordCount
      
    wordCount = 0
    
    for sentence in self.sentences:
    	wordCount += sentence.wordCount
            
    return wordCount
    
  def getLineCount():
    if self.lineCount != 0:
      return self.lineCount
      
    return len(self.sentences)
