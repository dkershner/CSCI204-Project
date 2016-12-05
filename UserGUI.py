''' Dan Kershner
    This file has the UserGUI class with functions to enter documents and attributes,
    filter them, then build a decision tree and evaluate a document based on this.
'''
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from Document import *
from TextFilter import *
from Tree import *
from BasicStats import *
from SKTree import *

class UserGUI:

    ''' The tkinter library built into python uses event driven programming.
        With it you are able to create widgets, such as buttons, that activate
        events when clicked (or on other events that you may specify). These
        widgets can be bound to functions that activate upon events. Tkinter
        also provides layout features that allow you to position widgets where
        you want them.
    '''

    def __init__(self, master):
        self.master = master
        master.title("UserGUI")

        self.entered_filename = ''
        self.entered_title = ''
        self.entered_author = ''
        self.entered_year = ''
        self.entered_genre = ''
        self.documents = []

        ## All entry labels
        self.filenameLabel = Label(master, text="Enter filename here: ")
        self.authorLabel = Label(master, text="Enter author here: ")
        self.yearLabel = Label(master, text="Enter year here: ")
        self.genreLabel = Label(master, text="Enter genre here: ")
        self.titleLabel = Label(master, text="Enter title here: ")

        self.trainLabel = Label(master, text="Train and evaluate using: ")

        ## All entries
        vcmdFile = master.register(self.validateFile) # we have to wrap the command
        self.fileEntry = Entry(master, validate="key", validatecommand=(vcmdFile, '%P'))
        
        vcmdAuthor = master.register(self.validateAuthor) # we have to wrap the command
        self.authorEntry = Entry(master, validate="key", validatecommand=(vcmdAuthor, '%P'))

        vcmdYear = master.register(self.validateYear) # we have to wrap the command
        self.yearEntry = Entry(master, validate="key", validatecommand=(vcmdYear, '%P'))

        vcmdGenre = master.register(self.validateGenre) # we have to wrap the command
        self.genreEntry = Entry(master, validate="key", validatecommand=(vcmdGenre, '%P'))

        vcmdTitle = master.register(self.validateTitle) # we have to wrap the command
        self.titleEntry = Entry(master, validate="key", validatecommand=(vcmdTitle, '%P'))

        ## All buttons
        self.docButton = Button(master, text="Enter Document and Attributes", command=lambda: self.enterDoc())
        # filter buttons
        self.whitespaceButton = Button(master, text="Normalize Whitespace", command=lambda: self.applyFilter('Normalize whitespace'))
        self.caseButton = Button(master, text="Normalize Case", command=lambda: self.applyFilter('Normalize case'))
        self.nullButton = Button(master, text="Strip Null Characters", command=lambda: self.applyFilter('Strip null characters'))
        self.numbersButton = Button(master, text="Strip Numbers", command=lambda: self.applyFilter('Strip numbers'))
        self.wordsButton = Button(master, text="Filter Words", command=lambda: self.applyFilter('Filter words'))
        # train buttons
        self.ID3Button = Button(master, text="ID3", command=lambda: self.train('ID3'))
        self.SKLearnButton = Button(master, text="SKLearn", command=lambda: self.train('SKLearn'))
        self.PCAButton = Button(master, text="PCA", command=lambda: self.train('PCA'))
        
        
        ## REMOVE THIS LATER #####
        self.printDocs = Button(master, text="Print Docs", command=lambda: self.printDoc())
        
        # LAYOUT

        # All attribute labels
        self.filenameLabel.grid(row=0, column=0, sticky=W)
        self.titleLabel.grid(row=1, column=0, sticky=W)
        self.authorLabel.grid(row=2, column=0, sticky=W)
        self.yearLabel.grid(row=3, column=0, sticky=W)
        self.genreLabel.grid(row=4, column=0, sticky=W)

        self.trainLabel.grid(row=5, column=4, pady=3)

        # All attribute entry boxes
        self.fileEntry.grid(row=0, column=1, columnspan=3, pady=5, sticky=W+E)
        self.titleEntry.grid(row=1, column=1, columnspan=3, pady=5, sticky=W+E)
        self.authorEntry.grid(row=2, column=1, columnspan=3, pady=5, sticky=W+E)
        self.yearEntry.grid(row=3, column=1, columnspan=3, pady=5, sticky=W+E)
        self.genreEntry.grid(row=4, column=1, columnspan=3, pady=5, sticky=W+E)
        
        # All buttons
        self.docButton.grid(row=1, rowspan = 2, column=4, padx = 10)
        self.whitespaceButton.grid(row=5, column=0, pady=3)
        self.caseButton.grid(row=6, column=0, pady=3)
        self.nullButton.grid(row=7, column=0, pady=3)
        self.numbersButton.grid(row=8, column=0, pady=3)
        self.wordsButton.grid(row=9, column=0, pady=3)

        self.ID3Button.grid(row=6, column=4, pady=3)
        self.SKLearnButton.grid(row=7, column=4, pady=3)
        self.PCAButton.grid(row=8, column=4, pady=3)


    def validateFile(self, new_text):
        self.entered_filename = new_text
        return True

    def validateTitle(self, title):
        self.entered_title = title
        return True

    def validateAuthor(self, author):
        self.entered_author = author
        return True

    def validateYear(self, year):
        self.entered_year = year
        return True

    def validateGenre(self, genre):
        self.entered_genre = genre
        return True
        
    def enterDoc(self):
        ''' Adds a given document and attributes to the list of documents.
        '''
        filename = self.entered_filename
        doc = Document(filename)
        doc.generateWhole()
        doc.author = self.entered_author
        doc.year = self.entered_year
        doc.genre = self.entered_genre
        self.documents.append(doc)
        self.fileEntry.delete(0, 'end')
        self.titleEntry.delete(0, 'end')
        self.authorEntry.delete(0, 'end')
        self.genreEntry.delete(0, 'end')
        self.yearEntry.delete(0, 'end')
        
    def applyFilter(self, name):
        ''' Applies the selected filter to each document that was entered.
            Takes the name of the filter and returns nothing.
        '''
        for x in self.documents:
            myFilter = TextFilter(x, [name])
            myFilter.apply()

    def train(self, method):
        ''' Uses the given training method to train the decision tree based on
            all given training documents (docs with a given author), then
            evaluates the document given without an author.
            Takes the name of the training method and returns the document title and author.
        '''
        trainingDocs, evalDocs = self.separateDocs()

        trainingData, evalData = self.parseData(trainingDocs, evalDocs)

        attributes = ['Author', 'Genre', 'Year', 'AmountTopN', 'AmountBottomN']
                
        if method == 'ID3':
            tree = Tree()
            tree.train(trainingData, attributes, 10)
            for i in range(len(evalDocs)):
                author = tree.evaluate(evalData[i], attributes, tree.root)
                print(evalDocs[i].title, ' author is ', author)
            print('Done')
        elif method == 'SKLearn':
            newData = self.convertData(data)
            tree = SKTree()
            tree.train(data, attributes, 10)
##        else:
##            # call the PCA train and eval methods


    def separateDocs(self):
        ''' Separates the given docs into training and eval based on if an author was given.
        '''
        trainingDocs = []
        evalDocs = []
        for x in self.documents:
            if x.author == '':
                evalDocs.append(x)
            else:
                trainingDocs.append(x)
        return trainingDocs, evalDocs

    def parseData(self, trainingDocs, evalDocs):
        ''' Creates the 2dList of data needed for ID3 from the given documents.
            Takes the training documents and returns the 2dList of data.
        '''
        myList = [[None]]*len(trainingDocs)
        evalData = [[None]]*len(evalDocs)
        totalWords = []
        for i in range(len(trainingDocs)):
            if myList[i] == None:
                myList[i] = trainingDocs[i].author
            else:
                myList[i].append(trainingDocs[i].author)
            myList[i].append(trainingDocs[i].genre)
            myList[i].append(trainingDocs[i].year)
            totalWords.extend(trainingDocs[i].getWords())
        stats = BasicStats()
        freqMap = stats.createFreqMap(totalWords)
        N = 10
        topWordsDict = stats.topNHeap(freqMap, N)
        topWords = list(topWordsDict.keys())
        bottomWordsDict = stats.bottomNHeap(freqMap, N)
        bottomWords = list(bottomWordsDict.keys())
        for j in range(len(trainingDocs)):
            self.addTopBottomN(trainingDocs[j], totalWords, topWords, bottomWords)
            myList[j].append(trainingDocs[j].topN)
            myList[j].append(trainingDocs[j].bottomN)
        for x in range(len(evalDocs)):
            if evalData[x] == None:
                evalData[x] = evalDocs[x].author
            else:
                evalData[x].append(evalDocs[x].author)
            evalData[x].append(evalDocs[x].genre)
            evalData[x].append(evalDocs[x].year)
            self.addTopBottomN(evalDocs[j], totalWords, topWords, bottomWords)
            evalData[x].append(evalDocs[x].topN)
            evalData[x].append(evalDocs[x].bottomN)
            
        return myList, evalData

    def addTopBottomN(self, doc, totalWords, topWords, bottomWords):
        ''' Adds the topN and bottomN attributes to the given document based on
            what percentage of those words it contains.
            Takes the document, total words across all docs, topN words and bottom
            N words across all documents. Returns nothing.
        '''
        numTop = 0
        numBottom = 0
        words = doc.getWords()
        N = len(topWords)
        for i in range(N):
            if topWords[i] in words:
                numTop += 1
            if bottomWords[i] in words:
                numBottom += 1
        fractionTop = numTop / N
        fractionBottom = numBottom / N
        if fractionTop < .4:
            doc.topN = 'Low'
        elif fractionTop < .7:
            doc.topN = 'Mid'
        else:
            doc.topN = 'High'
        if fractionBottom < .4:
            doc.bottomN = 'Low'
        elif fractionBottom < .7:
            doc.bottomN = 'Mid'
        else:
            doc.bottomN = 'High'

    def convertData(self, data):
        df = pd.DataFrame(data)

        #Need to setup maps to ordinal features
        #We could do this iwht a list/dist comp, I will learn the syntax to you
        genre_map = {'Fiction': 0, 'NonFiction': 1, 'Narrative': 2, 'Short Story': 3, 'Horror': 4}
        amountTopBottom_map = {'Low': 0, 'Mid': 1, 'High': 2}
        df['Genre'] = df['Genre'].map(genre_map)
        df['AmountTopN'] = df['AmountTopN'].map(amountTopBottom_map)
        df['AmountBottomN'] = df['AmountBottomN'].map(amountTopBottom_map)
        
        #Now we can convert to numpy arrays
        npv = df.as_matrix()
        return df
        

root = Tk()
my_gui = UserGUI(root)
root.mainloop()
