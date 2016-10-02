from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from Document import *
from CommandLinePlotter import *
from BasicStats import *
from MatPlotPloter import *

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

        self.label = Label(master, text="Enter title here: ")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.generate_button = Button(master, text="Generate Plot", command=lambda: self.main())

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)

        self.entry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        self.generate_button.grid(row=2, column=0)

    def validate(self, new_text):
        self.entered_title = new_text
        return True

        
    def main(self):
        filename = self.entered_title
        doc = Document(filename)
        doc.generateWhole()
        words = doc.getWords()
        stats = BasicStats()
        freqMap = stats.createFreqMap(words)
        topWords = stats.topN(freqMap, 10)
        highestFreq = list(topWords.values())
        plotter = CommandLinePloter(0, len(highestFreq), 0, max(highestFreq))
        plotter.d2Scatter(highestFreq)
        

root = Tk()
my_gui = UserGUI(root)
root.mainloop()
