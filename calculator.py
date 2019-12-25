from tkinter import *

root = Tk()
root.title("Calculator")

class Application(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        ## Set root equal to master, doesnt realy need this
        self.master = master
        self.theButtons()

    ## Displays Text Onto Entry ##
    def displayText(self, text):
        ## Gets the Existing Text on Entry ##
        self.existingText = self.display.get()
        ## Gets the length of that text ##
        self.existingTextLength = len(self.existingText)

        ## If Entry is empty ##
        if self.existingTextLength == 0:
            self.display.insert(0, text)
        else:
        ## If Entry not empty append to end of string##
            self.display.insert(self.existingTextLength, text)

    ## Does math stuff to numbers ##
    def evaluateText(self):
        ## Get what string the display has ##
        self.textToEval = self.display.get()

        ## Delete the display ##
        self.display.delete(0, END)
        ## Evaluate the previous display ##
        self.evaluatedText = eval(self.textToEval)
        ## Insert the evaluation onto the display ##
        self.display.insert(0, self.evaluatedText)

    ## Clears the entry of text ##
    def clearText(self):
        self.display.delete(0, END)


    def theButtons(self):
        self.display = Entry(self.master, font="Times", justify=RIGHT)
        self.display.grid(column=0, row=0, columnspan=5)

        ## FIRST ROW ##

        self.oneButton = Button(self, text="1", height=1, width=3, command=lambda: self.displayText("1"))
        self.oneButton.grid(column=0, row=1)

        self.twoButton = Button(self, text="2", height=1, width=3, command=lambda: self.displayText("2"))
        self.twoButton.grid(column=1, row=1)

        self.threeButton = Button(self, text="3", height=1, width=3, command=lambda: self.displayText("3"))
        self.threeButton.grid(column=2, row=1)

        self.fourButton = Button(self, text="4", height=1, width=3, command=lambda: self.displayText("4"))
        self.fourButton.grid(column=3, row=1)

        self.timesButton = Button(self, text="*", height=1, width=3, command=lambda: self.displayText("*"))
        self.timesButton.grid(column=4, row=1)

        ## SECOND ROW ##

        self.fiveButton = Button(self, text="5", height=1, width=3, command=lambda: self.displayText("5"))
        self.fiveButton.grid(column=0, row=2)

        self.sixButton = Button(self, text="6", height=1, width=3, command=lambda: self.displayText("6"))
        self.sixButton.grid(column=1, row=2)

        self.sevenButton = Button(self, text="7", height=1, width=3, command=lambda: self.displayText("7"))
        self.sevenButton.grid(column=2, row=2)

        self.eightButton = Button(self, text="8", height=1, width=3, command=lambda: self.displayText("8"))
        self.eightButton.grid(column=3, row=2)

        self.divideButton = Button(self, text="/", height=1, width=3, command=lambda: self.displayText("/"))
        self.divideButton.grid(column=4, row=2)

        ## THIRD ROW ##

        self.nineButton = Button(self, text="9", height=1, width=3, command=lambda: self.displayText("9"))
        self.nineButton.grid(column=0, row=3)

        self.zeroButton = Button(self, text="0", height=1, width=3, command=lambda: self.displayText("0"))
        self.zeroButton.grid(column=1, row=3)

        self.dotButton = Button(self, text=".", height=1, width=3, command=lambda: self.displayText("."))
        self.dotButton.grid(column=2, row=3)

        self.plusButton = Button(self, text="+", height=1, width=3, command=lambda: self.displayText("+"))
        self.plusButton.grid(column=3, row=3)

        self.minusButton = Button(self, text="-", height=1, width=3, command=lambda: self.displayText("-"))
        self.minusButton.grid(column=4, row=3)

        ## FOURTH ROW ##

        self.clearButton = Button(self, text="A/C", height=1, width=3, command=lambda: self.clearText())
        self.clearButton.grid(column=1, row=4)

        self.equalButton = Button(self, text="=", height=1, width=3, command=lambda: self.evaluateText())
        self.equalButton.grid(column=3, row=4)

app = Application(root).grid()
root.mainloop()
