from Document import *
from Sentence import *

class TextFilter:
    def __init__(self, document, filters):
        self.document = document
        self.filters = filters

    def apply(self):
        for x in self.filters:
            if x == 'Normalize whitespace':
                self.normalizeWhitespace()
            elif x == 'Normalize case':
                self.normalizeCase()
            elif x == 'Strip null characters':
                self.stripNullCharacters()
            elif x == 'Strip numbers':
                self.stripNumbers()
            elif x == 'Filter words':
                self.filterWords()
            else:
                print('Invalid filter: ', x)

    def normalizeWhitespace(self):
        sentences = []
        for sentence in self.document.getSentences():
            state = 'WORD'
            newSentence = ''
            for char in range(len(sentence.sentence)):
                if sentence.sentence[char].isspace():
                    state = 'SPACE'
                else:
                    newSentence += sentence.sentence[char]
                    state = 'WORD'
                    
                if state == 'SPACE':
                    if char == len(sentence.sentence)-1 or not sentence.sentence[char+1].isspace():
                        newSentence += sentence.sentence[char]
            if newSentence != '':
                toAppend = Sentence(newSentence)
                sentences.append(toAppend)

        self.document.setSentences(sentences)

    def normalizeCase(self):
        sentences = []
        for sentence in self.document.getSentences():
            if sentence != '':
                toAppend = Sentence(sentence.sentence.lower())
                sentences.append(toAppend)

        self.document.setSentences(sentences)

    def stripNullCharacters(self):
        sentences = []
        for sentence in self.document.getSentences():
            newSentence = ''
            for char in sentence.parseChar():
                num = ord(char)
                if char.isspace() or not (num < 48 or (num > 57 and num < 65) or (num > 90 and num < 97) or num > 122):
                    newSentence += char
            if newSentence != '':
                toAppend = Sentence(newSentence)
                sentences.append(toAppend)
        self.document.setSentences(sentences)

    def stripNumbers(self):
        sentences = []
        for sentence in self.document.getSentences():
            newSentence = ''
            for char in sentence.parseChar():
                num = ord(char)
                if not (num > 47 and num < 58):
                    newSentence += char
            if newSentence != '':
                toAppend = Sentence(newSentence)
                sentences.append(toAppend)
        self.document.setSentences(sentences)

    def filterWords(self)
        file = file.open('filterwords.txt', 'r')
        words = file.readLines()
        for sentence in self.document.getSentences():
            newSentence = ''
            for word in sentence.parseWords():
                if word not in words:
                    newSentence += word
            if newSentence != '':
                toAppend = Sentence(newSentence)
                sentences.append(toAppend)
        self.document.setSentences(sentences)
