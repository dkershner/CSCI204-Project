class Sentence:
    
    def __init__(self, sentence):
        self.sentence = sentence[0:len(sentence)-1]
        self.wordCount = len(self.parseWords())
        self.charCount = len(self.parseChar())
        self.punctuation = sentence[-1]

    def __repr__(self):
        return(self.sentence)
        
    def parseWords(self):
        return self.sentence.split()
        
    def parseChar(self):
        return list(self.sentence)
