from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from Document import *
from CommandLinePlotter import *
from BasicStats import *
from MatPlotPloter import *
from TextFilter import *

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

        self.entered_title = ''
        self.documents = []

        self.label = Label(master, text="Enter title here: ")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.docButton = Button(master, text="Enter Document", command=lambda: self.enterDoc())
        self.whitespaceButton = Button(master, text="Normalize Whitespace", command=lambda: self.applyFilter('Normalize whitespace'))
        self.caseButton = Button(master, text="Normalize Case", command=lambda: self.applyFilter('Normalize case'))
        self.nullButton = Button(master, text="Strip Null Characters", command=lambda: self.applyFilter('Strip null characters'))
        self.numbersButton = Button(master, text="Strip Numbers", command=lambda: self.applyFilter('Strip numbers'))
        self.wordsButton = Button(master, text="Filter Words", command=lambda: self.applyFilter('Filter words'))
        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)

        self.entry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        self.docButton.grid(row=2, column=0)
        self.whitespaceButton.grid(row=3, column=0)
        self.caseButton.grid(row=4, column=0)
        self.nullButton.grid(row=5, column=0)
        self.numbersButton.grid(row=6, column=0)
        self.wordsButton.grid(row=7, column=0)

    def validate(self, new_text):
        self.entered_title = new_text
        return True

        
    def enterDoc(self):
        filename = self.entered_title
        doc = Document(filename)
        doc.generateWhole()
        self.documents.append(doc)

    def applyFilter(self, type):
        for x in self.documents:
            filter = TextFilter(x, type)
            filter.apply()
        

root = Tk()
my_gui = UserGUI(root)
root.mainloop()
