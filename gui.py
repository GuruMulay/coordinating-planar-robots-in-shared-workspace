import numpy as np
from Tkinter import *
import Tkinter as tk
import csv
from matplotlib import pyplot as plt
import math as m
import clossestpair as cl
import sys
import numpy as np
import math as m
from math import sqrt
import time


class gui(tk.Tk):
	
    def __init__(self, parent = None):
        tk.Tk.__init__(self)
        height = 600
        width = 500
        canvas = Canvas(width=width, height=height, bg='#ccf5f5')
        
        canvas.pack()
        
        #canvas.bind('<ButtonPress-1>', self.mouseStart)
        #canvas.bind('<B1-Motion>',     self.mouseDrag)
        #canvas.bind('<Double-1>',      self.mouseStop)
        #canvas.bind('<ButtonPress-3>', self.mouseMove)
        
        self.canvas = canvas
        self.drawn  = None

        with open('angles_r1') as anglesR1:
            r1theta = [[float(x) for x in line.split()] for line in anglesR1]
            print r1theta
      
        self.r1theta = r1theta

        r1t1 = [row[0] for row in r1theta]
        r1t2 = [row[1] for row in r1theta]
        r1t3 = [row[2] for row in r1theta]

        self.r1t1 = r1t1
        self.r1t2 = r1t2
        self.r1t3 = r1t3
        print 'self.r1t1----------------------', self.r1t1
        print 'self.r1t2----------------------', self.r1t2
        print 'self.r1t3----------------------', self.r1t3


        with open('angles_r2') as anglesR2:
            r2theta = [[float(x) for x in line.split()] for line in anglesR2]
            print r2theta
      
        self.r2theta = r2theta

        r2t1 = [row[0] for row in r2theta]
        r2t2 = [row[1] for row in r2theta]
        r2t3 = [row[2] for row in r2theta]

        self.r2t1 = r2t1
        self.r2t2 = r2t2
        self.r2t3 = r2t3
        print 'self.r1t1----------------------', self.r2t1
        print 'self.r1t2----------------------', self.r2t2
        print 'self.r1t3----------------------', self.r2t3

        with open('rectangle_coordinates.txt') as rect:
            #w, h = [int(x) for x in next(f).split()]
            rect_xy = [[float(x) for x in line.split()] for line in rect]
            print rect_xy
        self.rect_xy = rect_xy
        
        c1 = [0 , 300]
        l11 = 100
        l12 = 100
        l13 = 100
        c2 = [500, 300]
        l21 = 100
        l22 = 100
        l23 = 100
            
        print len(r1t1)
        print len(r2t1)
        iterations_min = min(len(r1t1),len(r2t1))
        iterations_max = max(len(r1t1),len(r2t1))
        
        print 'iter_min-------', iterations_min
        print 'iter_max-------', iterations_max
        canvas.pack()
        
        for i in range(0, iterations_min):
                                        
            canvas.delete("all")
            time.sleep(0.05)

            self.displayR1(canvas,c1,l11,l12,l13,r1t1,r1t2,r1t3,i)
            #canvas.create_line(tooltip_old1,tooltip1, fill='#CCCEEF', width= 3, capstyle= 'round')
            self.displayR2(canvas,c2,l21,l22,l23,r2t1,r2t2,r2t3,i)
      
            self.displayObject(canvas)
            time.sleep(0.05)
            canvas.update()

        canvas.pack()
        for i in range(iterations_min, iterations_max):                    
                       
            canvas.delete("all")
            
            if iterations_min == len(r2t1):
                time.sleep(0.05)
                self.displayObject(canvas)
                self.displayR1(canvas,c1,l11,l12,l13,r1t1,r1t2,r1t3,i)
                self.displayR2(canvas,c2,l21,l22,l23,r2t1,r2t2,r2t3,iterations_min-1)
                
                time.sleep(0.05)
                canvas.update()

            else :
                time.sleep(0.05)
                self.displayObject(canvas)
                self.displayR1(canvas,c1,l11,l12,l13,r1t1,r1t2,r1t3,iterations_min-1)
                self.displayR2(canvas,c2,l21,l22,l23,r2t1,r2t2,r2t3,i)
                
                time.sleep(0.05)
                canvas.update()           
        
##        canvas.create_line(c1, 100, 300, fill='#CCCECF', width= 21, capstyle= 'round')
##        canvas.create_line(100, 300, 200, 300, fill='#ACBEDF', width= 15, capstyle= 'round')
##        canvas.create_line(200, 300, 300, 300, fill='#CCCEEF', 
##                           width= 10, arrow= 'last', arrowshape= "1 20 1", capstyle= 'round')
##        #xy = 0, 0, 0, 600
##        #canvas.create_arc(xy, start=0, extent=360, fill="red")
##        canvas.create_oval(-300, 0 , 300, 600, dash= (2,2))
##        canvas.create_oval(200, 0 , 800, 600, dash= (1,1))

##        r2arm2_base = [c2[0]- l21*m.cos(m.radians(45)), c2[1]- l21*m.sin(m.radians(45))]
##        r2arm3_base = [r1arm2_base[0]- l22*m.cos(m.radians(10)), r1arm2_base[1]- l22*m.sin(m.radians(10))]
##        tooltip2 = [r1arm3_base[0]- l23*m.cos(m.radians(-10)), r1arm3_base[1]- l23*m.sin(m.radians(-10))]

        
    def displayR1(self,canvas,c1,l11,l12,l13,r1t1,r1t2,r1t3,i):
##        canvas.pack()
        r1arm2_base = [c1[0]+ l11*m.cos(r1t1[i]), c1[1]- l11*m.sin(r1t1[i])]
        #print 'r1arm2base', r1arm2_base
        r1arm3_base = [r1arm2_base[0]+ l12*m.cos(r1t1[i]+r1t2[i]), r1arm2_base[1]- l12*m.sin(r1t2[i]+r1t1[i])]
        #print 'r1arm2base', r1arm3_base
        tooltip1 = [r1arm3_base[0]+ l13*m.cos(r1t1[i]+r1t2[i]+r1t3[i]), r1arm3_base[1]- l13*m.sin(r1t1[i]+r1t2[i]+r1t3[i])]
        #print 'tooltip', tooltip1

        arm11 = canvas.create_line(c1, r1arm2_base, fill='#CCCECF', width= 21, capstyle= 'round')
        arm12 = canvas.create_line(r1arm2_base, r1arm3_base, fill='#ACBEDF', width= 15, capstyle= 'round')
        arm13 = canvas.create_line(r1arm3_base,tooltip1, fill='#CCCEEF', 
                             width= 10, arrow= 'last', arrowshape= "1 20 1", capstyle= 'round')
        #canvas.create_text(tooltip1, text = '0')
##        time.sleep(0.1)
##        canvas.delete(arm11,arm12,arm13)
##        canvas.update()
##        
        return 0
    
    def displayR2(self,canvas,c2,l21,l22,l23,r2t1,r2t2,r2t3,i):
        r2arm2_base = [c2[0]+ l21*m.cos(r2t1[i]), c2[1]- l21*m.sin(r2t1[i])]
        #print 'r2arm2base', r2arm2_base
        r2arm3_base = [r2arm2_base[0]+ l22*m.cos(r2t1[i]+r2t2[i]), r2arm2_base[1]- l22*m.sin(r2t2[i]+r2t1[i])]
        #print 'r2arm2base', r2arm3_base
        tooltip2 = [r2arm3_base[0]+ l23*m.cos(r2t1[i]+r2t2[i]+r2t3[i]), r2arm3_base[1]- l23*m.sin(r2t1[i]+r2t2[i]+r2t3[i])]
        #print 'tooltip', tooltip1

        canvas.create_line(c2, r2arm2_base, fill='#CCCECF', width= 21, capstyle= 'round')
        canvas.create_line(r2arm2_base, r2arm3_base, fill='#ACBEDF', width= 15, capstyle= 'round')
        canvas.create_line(r2arm3_base,tooltip2, fill='#CCCEEF', 
                               width= 10, arrow= 'last', arrowshape= "1 20 1", capstyle= 'round')
    
        return 0

    def displayObject(self,canvas,):
        canvas.create_oval(-300, 0 , 300, 600, dash= (2,2))
        canvas.create_oval(200, 0 , 800, 600, dash= (1,1))
        canvas.create_line(self.rect_xy[0], self.rect_xy[1])
        canvas.create_line(self.rect_xy[1], self.rect_xy[2])
        canvas.create_line(self.rect_xy[2], self.rect_xy[3])
        canvas.create_line(self.rect_xy[3], self.rect_xy[0])
        canvas.create_text(35,200, font=("Helvetica", 12, 'bold'), text = 'Robot 1')
        canvas.create_text(465,200, font=("Helvetica", 12, 'bold'), text = 'Robot 2')
        canvas.create_text(75,30, font=("Helvetica", 12), text = 'Workspace \nboundary 1')
        canvas.create_text(425,30, font=("Helvetica", 12), text = 'Workspace \nboundary 2')

        return 0
    
if __name__=='__main__' :
    
    g = gui(1)
    g.mainloop()
    
    print '1' 
    
