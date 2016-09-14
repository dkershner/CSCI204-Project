class Document:
  
  def __init__(self, sentences, id, wordcount, linecount, charcount):
    self.sentences = sentences
    self.id = id
    self.wordcount = getWordCount()
    self.linecount = linecount
    self.charcount = charcount
    
  def generateWhole():
    #TODO
  
  def getWordCount():
    if self.wordCount != 0:
      return self.wordCount
      
    wordCount = 0
    currentState = 'WHITESPACE'
    
    for sentence in self.sentences:
      for char in sentence:
        if currentState == 'WHITESPACE':
          if not char.isspace():
            wordCount += 1
            currentState = 'WORD'
        else:   #current state is WORD
            if char.isspace():
              currentState = 'WHITESPACE'
    return wordCount
    
  def getLineCount():
    if self.lineCount != 0:
      return self.lineCount
      
    lineCount = 0
    
    for sentence in self.sentences:
      lineCount += 1
    
    return lineCount
