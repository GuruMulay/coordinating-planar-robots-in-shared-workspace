from Tkinter import *
import Tkinter as tk
import csv
import sys
import numpy as np
import math as m
from math import sqrt
import discretize as dis
import division as div
import subprocess, os


trace = 0 #avoids overlap and multiple images 

class drawObject(tk.Tk):
	
    def __init__(self, userInput, parent = None):
        tk.Tk.__init__(self)
        height = 600
        width = 500
        canvas = Canvas(width=width, height=height, bg='#ccf5f5')
        #'beige') 
        canvas.pack()
        
        canvas.bind('<ButtonPress-1>', self.mouseStart)  
        canvas.bind('<B1-Motion>',     self.mouseDrag)
        #canvas.bind('<Double-1>',      self.mouseStop)
        #canvas.bind('<ButtonPress-3>', self.mouseMove)
        
        self.canvas = canvas
        self.drawn  = None

        #################################################################
        centerline_x = height/2
        #################################################################
##        user_input = input("Enter 1 for a rectangle and 2 for a Circle:")
##        if type(user_input) == int:
##            print("Is a number")
##        else:
##            print("Not a number")
        c1 = [0 , 300]
        l11 = 100
        l12 = 100
        l13 = 100

        c2 = [500, 300]
        l21 = 100
        l22 = 100
        l23 = 100
        
        self.displayR1(canvas,c1,l11,l12,l13,(m.radians(-35)),(m.radians(35)),(m.radians(-15)))
        self.displayR2(canvas,c2,l21,l22,l23,(m.radians(135)),(m.radians(25)),(m.radians(35)))
                
##        canvas.create_line(c1, 100, 300, fill='#CCCECF', width= 21, capstyle= 'round')
##        canvas.create_line(100, 300, 200, 300, fill='#ACBEDF', width= 15, capstyle= 'round')
##        canvas.create_line(200, 300, 300, 300, fill='#CCCEEF', 
##                           width= 10, arrow= 'last', arrowshape= "1 20 1", capstyle= 'round')
        #xy = 0, 0, 0, 600
        #canvas.create_arc(xy, start=0, extent=360, fill="red")
        canvas.create_oval(-300, 0 , 300, 600, dash= (2,2))
        canvas.create_oval(200, 0 , 800, 600, dash= (1,1))

        canvas.create_text(35,200, font=("Helvetica", 12, 'bold'), text = 'Robot 1')
        canvas.create_text(465,200, font=("Helvetica", 12, 'bold'), text = 'Robot 2')
        canvas.create_text(75,30, font=("Helvetica", 12), text = 'Workspace \nboundary 1')
        canvas.create_text(425,30, font=("Helvetica", 12), text = 'Workspace \nboundary 2')
               
##        arm2_base = [c2[0]- l21*m.cos(m.radians(45)), c2[1]- l21*m.sin(m.radians(45))]
##        arm3_base = [arm2_base[0]- l22*m.cos(m.radians(10)), arm2_base[1]- l22*m.sin(m.radians(10))]
##        tooltip2 = [arm3_base[0]- l23*m.cos(m.radians(-10)), arm3_base[1]- l23*m.sin(m.radians(-10))]
##          
##        #print c2[0]- l21*m.cos(m.radians(45))
##        canvas.create_line(c2, arm2_base, fill='#CCCECF', width= 21, capstyle= 'round')
##        canvas.create_line(arm2_base, arm3_base, fill='#ACBEDF', width= 15, capstyle= 'round')
##        canvas.create_line(arm3_base,tooltip2, fill='#CCCEEF', 
##                           width= 10, arrow= 'last', arrowshape= "1 20 1", capstyle= 'round')
        
        if userInput == 1:
            print("1 Rectangle")
            self.objectShape = [canvas.create_rectangle]
        else:
            print("2 Circle")
            self.objectShape = [canvas.create_oval]
        #print len(self.objectShape)
        #, canvas.create_line]

    def displayR1(self,canvas,c1,l11,l12,l13,r1t1,r1t2,r1t3):
        r1arm2_base = [c1[0]+ l11*m.cos(r1t1), c1[1]- l11*m.sin(r1t1)]
        #print 'r1arm2base', r1arm2_base
        r1arm3_base = [r1arm2_base[0]+ l12*m.cos(r1t1+r1t2), r1arm2_base[1]- l12*m.sin(r1t2+r1t1)]
        #print 'r1arm2base', r1arm3_base
        tooltip1 = [r1arm3_base[0]+ l13*m.cos(r1t1+r1t2+r1t3), r1arm3_base[1]- l13*m.sin(r1t1+r1t2+r1t3)]
        #print 'tooltip', tooltip1

        canvas.create_line(c1, r1arm2_base, fill='#CCCECF', width= 21, capstyle= 'round')
        canvas.create_line(r1arm2_base, r1arm3_base, fill='#ACBEDF', width= 15, capstyle= 'round')
        canvas.create_line(r1arm3_base,tooltip1, fill='#CCCEEF', 
                             width= 10, arrow= 'last', arrowshape= "1 20 1", capstyle= 'round')

        return 0
    
    def displayR2(self,canvas,c2,l21,l22,l23,r2t1,r2t2,r2t3):
        r2arm2_base = [c2[0]+ l21*m.cos(r2t1), c2[1]- l21*m.sin(r2t1)]
        #print 'r2arm2base', r2arm2_base
        r2arm3_base = [r2arm2_base[0]+ l22*m.cos(r2t1+r2t2), r2arm2_base[1]- l22*m.sin(r2t2+r2t1)]
        #print 'r2arm2base', r2arm3_base
        tooltip2 = [r2arm3_base[0]+ l23*m.cos(r2t1+r2t2+r2t3), r2arm3_base[1]- l23*m.sin(r2t1+r2t2+r2t3)]
        #print 'tooltip', tooltip1

        canvas.create_line(c2, r2arm2_base, fill='#CCCECF', width= 21, capstyle= 'round')
        canvas.create_line(r2arm2_base, r2arm3_base, fill='#ACBEDF', width= 15, capstyle= 'round')
        canvas.create_line(r2arm3_base,tooltip2, fill='#CCCEEF', 
                               width= 10, arrow= 'last', arrowshape= "1 20 1", capstyle= 'round')
    
        return 0

    def mouseStart(self, event):
        self.shape = self.objectShape[0]
        print 'd2'
        self.objectShape =  self.objectShape[:1] #self.objectShape[1:] +
        
        self.start = event
        print 'start' , self.start.x, self.start.y
        self.drawn = None
        #self.canvas.delete(self.objectShape)
        #self.canvas.delete("all")
        return [self.start.x, self.start.y]
        
    def mouseDrag(self, event):                         
        canvas = event.widget
        #print 'd3'
        if self.drawn: canvas.delete(self.drawn)
        if userInput == 1:
            #print("Rectangle/Square")
            objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        else:
            #print("Circle")
            cx = (event.x + self.start.x)/2
            r = abs(cx - self.start.x)
            objectId = self.shape(self.start.x, self.start.y, event.x, (self.start.y+2*r))
        
        #print 'end', event.x, event.y
        #print objectId
        if trace: print objectId
        self.drawn = objectId
        #self.canvas.delete("all")
        print 'end', event.x, event.y
        self.stop = event
        return [self.stop.x, self.stop.y]
        
##    def mouseStop(self, event):
##        print 'd4'
##        
##        event.widget.delete('all')
##        
##    def mouseMove(self, event):
##        if self.drawn:
##            print 'd5'
##            if trace: print self.drawn
##            canvas = event.widget
##            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
##            print 'diffX,Y' , diffX, diffY 
##            canvas.move(self.drawn, diffX, diffY)
##            self.start = event

    def distance(self,p0,p1):
        return sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def askUserInput():
    userInput = 0
    while True:
      try:
         userInput = int(input("Enter: 1 for Rectangle | 2 for Circle: "))       
      except NameError:
         print("Not an integer!")
         continue
      if userInput == 1: 
         print("You have selected a rectangle!")
         break
      elif userInput == 2:
         print("You have selected a circle!")
         break
    return userInput

def squareDiscretizer():
    
    text_file = open("rectangle_coordinates.txt", "w")
    print text_file
    text_file.close()
        
if __name__ == '__main__':
     
    userInput = askUserInput()
    draw = drawObject(userInput)
    draw.mainloop()

    if userInput == 1: ##print rectangle coordinates
        x1 = draw.start.x
        y1 = draw.start.y
        x3 = draw.stop.x
        y3 = draw.stop.y
        x2 = x1
        y2 = y3
        x4 = x3
        y4 = y1
        x_i = np.array([x1, x2, x3, x4, x1])
        y_i = np.array([y1, y2, y3, y4, y1])
        xiyi = np.array([x_i, y_i])
        xiyi = xiyi.T
        print xiyi
            
        print 'Square is: (%d,%d), (%d,%d), (%d,%d), (%d,%d)' %(x1,y1,x2,y2,x3,y3,x4,y4)
        text_file = open("rectangle_coordinates.txt", "w")
        #text_file.write("x_coordinate y_coordinate %d " % x1)
        np.savetxt(text_file, xiyi, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
        text_file.close()
        
    elif userInput == 2: ##print circle coordinates
        x1 = draw.start.x
        y1 = draw.start.y
        x3 = draw.stop.x
        y3 = draw.stop.y
        x2 = x1
        y2 = y3
        cx = (x3 + x1)/ 2
        cy = y1 + abs(cx-x1)
        px = (x1 + x2)/2
        py = (y1 + y2)/2
        
        r = sqrt((cx-px)*(cx-px) + (cy-py)*(cy-py))
        print r
        r = (x3 - x2)/2
        print r
        print 'Center of Circle is: (%d,%d)' %(cx,cy)
        ri = np.array([r , r])
        ci = np.array([cx, cy])
        xiyi = np.array([ri, ci])
        
        text_file = open("circle_coordinates.txt", "w")
        #text_file.write("center and radius %d " % x1)
        np.savetxt(text_file, xiyi, fmt = ('%f','%f'))#,header='radius and center')
        
        text_file.close()

    print 'end-----'
    #######################################################################
    with open('rectangle_coordinates.txt') as f:
        #w, h = [int(x) for x in next(f).split()]
        square_xy_coordinates = [[float(x) for x in line.split()] for line in f]
        print square_xy_coordinates
        
    if (draw.distance(square_xy_coordinates[0],square_xy_coordinates[1]) > 350 or
        draw.distance(square_xy_coordinates[1],square_xy_coordinates[2]) > 350):
        resolution = 100
        print 'resolution 100 ------------------------------------------'
    elif (draw.distance(square_xy_coordinates[0],square_xy_coordinates[1]) > 250 or
        draw.distance(square_xy_coordinates[1],square_xy_coordinates[2]) > 250):
        resolution = 80
        print 'resolution 80 ------------------------------------------'
    else :
        resolution = 60

    draw1 = dis.discretize(resolution)
    u = draw1.squareDiscretizer(square_xy_coordinates)
    #######################################################################

    draw2 = div.division()
    #p = draw2.division()
    cx, cy = draw2.read()
    print 'cl______________________________________________________', cx, cy
    r = draw2.compare(cx,cy)
    #######################################################################

##    os.chdir(r'C:\Python27\ECE555 Project')
##    #subprocess.Popen(['matlab','kinematics_r1.m'])
##    
##    print os.listdir(os.curdir)
##    returnCode = subprocess.call("matlab -r kinematics_r1.m", shell=False)
##    print "Return Code: ", returnCode
