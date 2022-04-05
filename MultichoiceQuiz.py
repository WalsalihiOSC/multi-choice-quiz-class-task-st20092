#week 9 Multi-choice Quiz
from tkinter import *

class MultiQuizGUI:

    def __init__(self, parent):
        mainframe = Frame(parent)
        mainframe.grid()
        answersframe = Frame(mainframe)
        answersframe.grid(row = 1)

        questionlabel = Label(mainframe, text = "What is the capital of Mongolia?")
        questionlabel.grid(row = 0)

        answers = ["Vladivostok", "Astana", "Ulan Bator", "Lhasa"]
        self.a = StringVar()
        self.a.set('')

        for answer in answers:
            Radiobutton(answersframe, text = answer, value = answer, variable = self.a).grid(sticky = W)

            
root = Tk()
MultiQuizGUI(root)
root.mainloop()
