# gasket.py
#
# By: Peyton Wiecking
# Date: 5/2/19
# CSCI 112 02
#
# This program draws a Sierpinski Gasket using ezgraphics and recursion 

# import ezgraphics
from ezgraphics import *

# given helper class 
# stores x and y coordinates
class Vertex:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

# set constants/change canvas size and amount of triangles here
width = 500
heigth = 500
subdiv = 8

# define main
def main():
    
    # creates the graphics window and gives the gasket its name
    win = GraphicsWindow(width, heigth) 
    win.setTitle("Sierpinski's Gasket")
    
    # set up the vertices 
    vertex1 = Vertex(width / 2, 0)
    vertex2 = Vertex(0, heigth)
    vertex3 = Vertex(width, heigth)
    
    # gives the gasket its color
    canvas = win.canvas()
    canvas.setColor("blue")
    gasket(subdiv, canvas, vertex1, vertex2, vertex3)
    win.wait()

# creates the gasket through recursion with a maximum of 8 subdivisons
def gasket (subdiv, canvas, vertex1, vertex2, vertex3):
    # divides the tringles into smaller triangles 
    if subdiv > 0:        
        vertexA = midPoint(vertex1, vertex2)
        vertexB = midPoint(vertex2, vertex3)
        vertexC = midPoint(vertex3, vertex1)
        # base case
        subdiv = subdiv - 1
        # call to self
        gasket(subdiv, canvas, vertex1, vertexA, vertexC)
        gasket(subdiv, canvas, vertexA, vertex2, vertexB)
        gasket(subdiv, canvas, vertexC, vertexB, vertex3)
    # otherwise draws a triangle   
    else:
        canvas.drawPolygon (vertex1.x, vertex1.y, vertex2.x, vertex2.y, \
                            vertex3.x, vertex3.y)

# helper method used to find the midpoint between two vertices
def midPoint(vertex1, vertex2):
    pointA = vertex1.x
    pointB = vertex1.y
    pointC = vertex2.x
    pointD = vertex2.y
    midpointA = (pointA + pointC) // 2
    midpointB = (pointB + pointD) // 2
    # returns a new vertex
    return Vertex(midpointA, midpointB)

# call main
main()