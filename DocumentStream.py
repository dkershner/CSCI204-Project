from Sentence import *
from DocumentStreamError import *

class DocumentStream:
    
    def __init__(self, filename = None):
        self.filename = filename
        if filename == '':
            raise DocumentStreamError('No file name given')
    
    def readWhole(self):
        sentences = []
        file = open(self.filename, 'r', encoding='utf-8' )            
        lines = file.readlines()

        for line in lines:
            startIndex = 0
            end = len(line)
            for char in range(len(line)):
                if line[char] == '.':
                    sentence = Sentence(line[startIndex:char+1])
                    sentences.append(sentence)
                    startIndex = char + 1
                elif line[char] == '!':
                    sentence = Sentence(line[startIndex:char+1])
                    sentences.append(sentence)
                    startIndex = char + 1
                elif line[char] == '?':
                    sentence = Sentence(line[startIndex:char+1])
                    sentences.append(sentence)
                    startIndex = char + 1
                elif line[char] == ';':
                    sentence = Sentence(line[startIndex:char+1])
                    sentences.append(sentence)
                    startIndex = char + 1
                elif char + 2 < end and line[char] == ' ' and line[char + 1] == ' ' and line[char + 2]==' ':
                    if(startIndex < char):
                        sentence = Sentence(line[startIndex:char+1])
                        sentences.append(sentence)
                        space = char
                        while(line[space].isspace()):
                            space += 1
                        startIndex = space

        return sentences

    def writeWhole(self, sentences):
        file = open('output.txt', 'w', encoding='utf-8')
        for sentence in sentences:
            file.write(sentence.sentence + '\n')
