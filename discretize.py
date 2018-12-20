import numpy as np
from Tkinter import *
import Tkinter as tk
from math import sqrt
#from bigfloat import *

class discretize(tk.Tk):
    
    def __init__(self, resolution, parent = None):
        
        tk.Tk.__init__(self)
        self.resolution = resolution
               
    def distance(self,p0,p1):
        return sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

    def discretizer(self,p0,p1,u,square_xy_coordinates):
        s0 = p0
        s1 = p1

        with open('rectangle_coordinates.txt') as f:
            sq4 = [[float(x) for x in line.split()] for line in f]
            print 'sq4', sq4
        
        h = self.distance(sq4[0], sq4[1])
        w = self.distance(sq4[1], sq4[2])
        print 'h,w', h, w
        
##        resolution = 20
        print 's0, s1', s0, s1
        d = self.distance(s0,s1)
        print 'd', d
        step_h = h/self.resolution
        
        resolution_w = int(round((w/h)*self.resolution))
        print 'resolution_w ', resolution_w
        step_w = w/resolution_w
        
        print 'step_h, step_w', step_h, step_w
        print 'u', u
        x_i = []
        y_i = []

        if (d == h):
            for i in range(1, self.resolution+1):
                     
                s0[0] = s0[0] + step_h * u[0,0]
                s0[1] = s0[1] + step_h * u[0,1]
                #print 'u', u[0,0], u[0,1]
            
                x_i = np.append(x_i, s0[0])
                y_i = np.append(y_i, s0[1])
                i = i+1
        else :
            for i in range(1, resolution_w+1):
                     
                s0[0] = s0[0] + step_w * u[0,0]
                s0[1] = s0[1] + step_w * u[0,1]
                #print 'u', u[0,0], u[0,1]
            
                x_i = np.append(x_i, s0[0])
                y_i = np.append(y_i, s0[1])
                i = i+1
                
        print 'x_i, y_i', x_i, y_i
        
        return x_i, y_i

    def squareDiscretizer(self, square_xy_coordinates):
               
        u = np.zeros(shape=(1, 4, 2))
        square_xy = square_xy_coordinates
        n = 4
        for i in range(0, n):
            u[:,i,:] = self.unitVector(square_xy[i][0],square_xy[i][1],square_xy[(i+1)][0],square_xy[(i+1)][1])
            print 'square_xy[(i+1)%n', square_xy[(i+1)]
    ##        u01 = unitVector(s0[0],s0[1],s1[0],s1[1])
    ##        u12 = unitVector(s1[0],s1[1],s2[0],s2[1])
    ##        u23 = unitVector(s2[0],s2[1],s3[0],s3[1])
    ##        u30 = unitVector(s3[0],s3[1],s0[0],s0[1])
    ##u[:,3,:] = unitVector(square_xy[3][0],square_xy[3][1],square_xy[0][0],square_xy[0][1])
        print u   

        x = np.array([square_xy[0][0]])
        y = np.array([square_xy[0][1]])
        print 'xy', x, y
        print 'square_xy----->' , square_xy
        for i in range(0, n):
            print 'i', i
            #print 'square_xy[i]+++', square_xy[i], square_xy[(i+1)%n]
            #x_i, y_i = self.discretizer(square_xy[i], square_xy[(i+1)%n], u[:,i,:])
            x_i, y_i = self.discretizer(square_xy[i], square_xy[(i+1)], u[:,i,:], square_xy)
            square_xy = square_xy_coordinates
            print 'square_xy[i]+++', square_xy[i], square_xy[(i+1)]
            i = i+1
            
            x = np.append([x], [x_i])
            y = np.append([y], [y_i])
            
        xiyi = np.array([x, y])
        xiyi = xiyi.T
        print 'xiwyi_1',xiyi
        xiyi = xiyi[:-1]
        print 'xiwyi_2',xiyi
        text_file = open("discrete_rectangle.txt", "w")
        np.savetxt(text_file, xiyi, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
        text_file.close()
        
        return u
            
    def unitVector(self, x0,y0,x1,y1):
        
        distance = [x1 - x0, y1 - y0]
        norm = sqrt(distance[0] ** 2 + distance[1] ** 2)
        unit_vector = [distance[0] / norm, distance[1] / norm]
        return unit_vector
            
if __name__ == '__main__':

    draw = discretize(resolution)   
             
    with open('rectangle_coordinates.txt') as f:
        #w, h = [int(x) for x in next(f).split()]
        square_xy_coordinates = [[float(x) for x in line.split()] for line in f]
        print square_xy_coordinates
    
    u = draw.squareDiscretizer(square_xy_coordinates)
    
