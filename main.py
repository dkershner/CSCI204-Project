from Document import *
from CommandLinePlotter import *
from BasicStats import *

def main():

    filename = input('Please enter a filename')
    doc = Document(filename)
    doc.generateWhole()
    words = doc.getWords()
    stats = BasicStats()
    freqMap = stats.createFreqMap(words)
    topWords = stats.topN(freqMap, 10)
    highestFreq = list(topWords.values())
    plotter = CommandLinePloter(0, 10, 0, max(highestFreq))
    plotter.d2Scatter(highestFreq)
    print(plotter)

main()
