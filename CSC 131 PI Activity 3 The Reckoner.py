from Tkinter import *

class MainGUI(Frame):
    #the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-topmost", True)
        self.setupGUI()

    #sets up the GUI
    def setupGUI(self):
        #the calculator uses the TexGyreAdventor font
        #sets font to 50 point, background to white, and height to 2 characters
        self.display = Label(self, text="", anchor=E, bg="white", height=2, font=("TexGyreAdventor", 50))

        #put it in the top row spanning all across
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

        #configure the rows columns and frames
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)

        #there are 4 columns (0 through 3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)

        #fetch and store the image
        #(
        img = PhotoImage(file="images/lpr.gif")
        #create the button
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("("))
        #set the button's image
        button.image = img
        #put the button in its proper row and column
        button.grid(row=1, column=0, sticky=N+S+E+W)

        #the same is done for the rest of the buttons
        #)
        img = PhotoImage(file="images/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N+S+E+W)

        #AC
        img = PhotoImage(file="images/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("AC"))
        button.image = img
        button.grid(row=1, column=2, sticky=N+S+E+W)

        #**
        img = PhotoImage(file="images/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("**"))
        button.image = img
        button.grid(row=6, column=2, sticky=N+S+E+W)

        #the second row
        #7
        img = PhotoImage(file="images/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N+S+E+W)

        #8
        img = PhotoImage(file="images/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N+S+E+W)

        #9
        img = PhotoImage(file="images/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N+S+E+W)

        #/
        img = PhotoImage(file="images/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N+S+E+W)

        #the third row
        #4
        img = PhotoImage(file="images/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N+S+E+W)

        #5
        img = PhotoImage(file="images/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N+S+E+W)

        #6
        img = PhotoImage(file="images/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N+S+E+W)

        #*
        img = PhotoImage(file="images/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("*"))
        button.image = img
        button.grid(row=3, column=3, sticky=N+S+E+W)

        #the fourth row
        #1
        img = PhotoImage(file="images/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N+S+E+W)

        #2
        img = PhotoImage(file="images/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N+S+E+W)

        #3
        img = PhotoImage(file="images/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N+S+E+W)

        #-
        img = PhotoImage(file="images/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N+S+E+W)

        #the fifth row
        #0
        img = PhotoImage(file="images/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N+S+E+W)

        #.
        img = PhotoImage(file="images/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N+S+E+W)

        #=
        img = PhotoImage(file="images/eql-wide.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("="))
        button.image = img
        button.grid(row=6, column=0, sticky=N+S+E+W, columnspan = 2)

        #+
        img = PhotoImage(file="images/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N+S+E+W)

        #%
        img = PhotoImage(file="images/mod.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("%"))
        button.image = img
        button.grid(row=6, column=3, sticky=N+S+E+W)

        #<-
        img = PhotoImage(file="images/bak.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("bak"))
        button.image = img
        button.grid(row=1, column=3, sticky=N+S+E+W)
        

        #pack the GUI
        self.pack(fill=BOTH, expand=1)

        
    #processes button presses
    def process(self, button):
        #AC clears the display
        if (button == "AC"):
            #clear the display
            self.display["text"] = ""
        # = starts an evaluation of whatever is on the display
        elif (button == "="):
            #get the expression in the display
            expr = self.display["text"]
            #the evaluation may return an error!
            try:
                #evaluate the expression
                result = eval(expr)   
                    
                       
                #store the result to the display
                self.display["text"] = str(result)
                
            #handle if an error in the display
            except:
                #note the error in the display
                self.display["text"] = "ERROR"
        #otherwise, just tack on the appropriate operand/operator
        else:
            self.display["text"] += button

        #bak takes off the character before and limits the character count to 14
        if (button == "bak"):
            self.display["text"] = self.display["text"][:(len(self.display["text"])-4)]
        if (len(self.display["text"]) > 14):
                    self.display["text"] = self.display["text"][:(len(self.display["text"])-4)]
##        if (len(self.display["text"]) > 11):
##            while (len(self.display["text"]) > 11):
##                [(len(self.display["text"])-4)]
##            result += "..."

####################################################
####The main part of the program
####################################################
#create the window
window = Tk()

#set the window
window.title("The Reckoner")

#generate the GUI
p = MainGUI(window)

#display the GUI and wait for user interaction
window.mainloop()
        
