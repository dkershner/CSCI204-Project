class Document:
  
  def __init__(self, sentences):
    self.sentences = sentences
    self.id = #something here
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
