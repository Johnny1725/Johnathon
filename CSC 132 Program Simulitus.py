######################################################################################################################
# Name: Johnathon Terry
# Date: 4/19/2020
# Description: Program Simulitus
################################################################################################################
from Tkinter import *
import random 
import math


# the Circle class. All circles have an x and y coordinate for their
# centers, a rad value for their radius, and a color.
class Circle(object):
    # write your code for the circle class here and subsequently
    def __init__ (self, x = 0.0, y = 0.0, radius = 0, color = "black"):
        self.x = float(x)
        self.y = float(y)
        self.radius = float(radius)
        self.color = color

    #function that calculates the distance
    def dist_(self, circle):
        dista = ((self.x-circle.x)**2+(self.y-circle.y)**2)**0.5
        return dista

        
    #Accessors and Mutators, allows for x and y to change
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def color(self):
        return self._color
    @radius.setter
    def color(self, value):
        self._color = value
    #returns a string
    def __str__(self):
        return "({},{},{},{})".format(self.x, self.y, self.radius, self.color)


                
    

# the Diagram class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class Diagram(Canvas):
    def __init__ (self, parent):
        Canvas.__init__(self, parent, bg="white")

    #function that makes the circles, by giving them color, size and, etc
    def drawCircles(self, NUM_CIRCLES):
        for i in range(1):
            colors = ["red", "blue"]
            r_x = random.randint(0,700)
            r_y = random.randint(0,700)
            r_radius = random.randint(4,5)
            p = Circle(r_x, r_y, r_radius)
            self.create_oval(p.x-p.radius, p.y-p.radius, p.x+p.radius, p.y+p.radius, fill = "red")
            p.dy = 0
            p.dx = 2
            
        for i in range(99):
            colors = ["red", "blue"]
            r_x = random.randint(0,700)
            r_y = random.randint(0,700)
            r_radius = random.randint(4,5)
            p = Circle(r_x, r_y, r_radius)
            self.circle = self.create_oval(p.x-p.radius, p.y-p.radius, p.x+p.radius, p.y+p.radius, fill = "blue")
            
            p.dy = 0
            p.dx = 2
        person_list = []

        self.pack(fill = "both", expand = 1)
        self.canvas.move(self.circle, self.r_x, self.r_y)
        
        
        
               

                
        

    
    
    
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of circles to draw
NUM_CIRCLES = []

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Circles...drawn")
# create the Diagram as a Tkinter canvas inside the window
s = Diagram(window)
# draw some random circles
s.drawCircles(NUM_CIRCLES)



# wait for the window to close
window.mainloop()








