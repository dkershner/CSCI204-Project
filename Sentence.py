''' Dan Kershner
    This file has the sentence class with methods to get the individual characters
    or words out of a sentence.
'''

class Sentence:
    
    def __init__(self, sentence):
        self.sentence = self.parseSentence(sentence)
        self.wordCount = len(self.parseWords())
        self.charCount = len(self.parseChar())
        self.punctuation = ''

    def __repr__(self):
        return(self.sentence)
        
    def parseWords(self):
        return self.sentence.split()
        
    def parseChar(self):
        return list(self.sentence)

    def parseSentence(self, sentence):
        punctuation = sentence[-1]
        if punctuation == '.' or punctuation == '?' or punctuation == '!' or punctuation == ';':
            self.punctuation = punctuation
            return sentence[:-1]
        else:
            return sentence
            
