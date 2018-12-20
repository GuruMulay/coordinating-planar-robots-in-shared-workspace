import numpy as np
from matplotlib import pyplot as plt
import math as m
import clossestpair as cl

class division() :

    """An implementation of the division algorithm.
    """

    def __init__(self, height=600, width=500) :

        self.height = height
        self.width = width

        with open('rectangle_coordinates.txt') as sq1:
            sq_xy = [[float(x) for x in line.split()] for line in sq1]
            print sq_xy
        self.sq_xy = sq_xy

        with open('discrete_rectangle.txt') as rect:
            Dxy = [[float(x) for x in line.split()] for line in rect]
            print Dxy
        self.Dxy = Dxy

        dx = [row[0] for row in Dxy]
        dy = [row[1] for row in Dxy]
        self.dx = dx
        self.dy = dy
        n = len(dx)
        self.n = n

    def read(self, ) :
        
        print self.sq_xy
        
        cx = (self.sq_xy[0][0] + self.sq_xy[2][0])/2
        cy = (self.sq_xy[0][1] + self.sq_xy[2][1])/2
        
        """
        
        """

        return cx, cy

    def find_nearest_xy(self, x_array, y_array, x_point, y_point):
        
        distancex = (np.asarray(x_array)-x_point)**2
        distancey = (np.asarray(y_array)-y_point)**2
        print 'dis', distancex, distancey
        idx = np.where(distancex==distancex.min())
        idy = np.where(distancey==distancey.min())
        return idx,idy

    def compare(self, cx, cy) :
        print 'cx', cx
        print 'cy', cy
        #check if center is approximately within the crescent frame
        if (225<cx<275 and 225<cy<400):
            print 'inside the arcs----------------------'
            #if (134.1687<sq_xy[0][1]<465.8312):
            if (140<self.sq_xy[0][1]<460):
                self.center(cx, cy)
                print 'center ---------------------'
                return 0
                
        if cx < (self.width/2):
            print 'r1'
            r = 1
            square_check = self.checkR1(r)
            print square_check
            op2 = self.methodR1(square_check)
            print op2
            
        elif cx > (self.width/2):
            print 'r2'
            r = 2
            square_check = self.checkR2(r)
            print square_check
            op2 = self.methodR2(square_check)
            
        else :
            print 'mid'
            r = 0

        return r

    def center(self, cx, cy):

        a1 = cx
        b1 = self.sq_xy[0][1]
        a2 = cx
        b2 = self.sq_xy[2][1]

        print 'app', self.Dxy + [[a1,b1]]
        pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
        print 'pair index up', pair_id_up

        pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
        print 'pair index down', pair_id_down

        print 'print r2', self.Dxy[pair_id_down: pair_id_up+1]
        print 'For center case ----------------------------------------------------------'
        text_file = open("r2.txt", "w")
        np.savetxt(text_file, self.Dxy[pair_id_down: pair_id_up+1], fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
        text_file.close()

        print 'print r1', self.Dxy[0:pair_id_down]
        print 'print r1', self.Dxy[pair_id_up+1:self.n]

        print 'r1 final', self.Dxy[0:pair_id_down] + self.Dxy[pair_id_up+1:self.n]

        Dr1 = self.Dxy[pair_id_up+1:self.n] + self.Dxy[0:pair_id_down]
        text_file = open("r1.txt", "w")
        np.savetxt(text_file,Dr1, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
        text_file.close()

    def check_if_in_workspace_r1(self, r1xy):

        r1xy_workspace = []
        length_r1 = len(r1xy)
        print 'length_r1', length_r1
        
        for i in range(0, length_r1):

            if self.evalCircle1(r1xy[i][0],r1xy[i][1]) == -1:
                r1xy_workspace = r1xy_workspace + [r1xy[i]]

        print 'r1xy++++++++++++++++++++++++++++++++++++++++', r1xy, len(r1xy)
        print 'r1xy_workspace++++++++++++++++++++++++++++++', r1xy_workspace, len(r1xy_workspace)

        return r1xy_workspace


    def check_if_in_workspace_r2(self, r2xy):

        r2xy_workspace = []
        length_r2 = len(r2xy)
        print 'length_r2', length_r2
        
        for i in range(0, length_r2):

            if self.evalCircle2(r2xy[i][0],r2xy[i][1]) == -1:
                r2xy_workspace = r2xy_workspace + [r2xy[i]]

        print 'r2xy++++++++++++++++++++++++++++++++++++++++', r2xy, len(r2xy)
        print 'r2xy_workspace++++++++++++++++++++++++++++++', r2xy_workspace,len(r2xy_workspace)

        return r2xy_workspace    


    def methodR1(self, sq_check):
        if (sq_check[0]<0 and sq_check[1]<0 and sq_check[2]<0 and sq_check[3]<0):
            print 'all in'
            b1 = self.sq_xy[0][1]
            print 'b1', b1
            a1 = -abs(m.sqrt(300*300 - (b1-300)*(b1-300))) + 500
            b2 = self.sq_xy[2][1]
            print b1
            a2 = -abs(m.sqrt(300*300 - (b2-300)*(b2-300))) + 500
            print 'ab', a1,b1,a2,b2

            ####################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            if ((self.Dxy[pair_id_up][0]-500)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'out' 
                pair_id_up = pair_id_up -1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                

            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            if ((self.Dxy[pair_id_down][0]-500)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'out' 
                pair_id_down = pair_id_down +1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print 'print r2', self.Dxy[pair_id_down: pair_id_up+1]
            print 'For all in ----------------------------------------------------------'
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, self.Dxy[pair_id_down: pair_id_up+1], fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            print 'print r1', self.Dxy[0:pair_id_down]
            print 'print r1', self.Dxy[pair_id_up+1:self.n]

            print 'r1 final', self.Dxy[0:pair_id_down] + self.Dxy[pair_id_up+1:self.n]

            Dr1 = self.Dxy[pair_id_up+1:self.n] + self.Dxy[0:pair_id_down]
            text_file = open("r1.txt", "w")
            np.savetxt(text_file,Dr1, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close() 

            ###################
            
        elif (sq_check[0]<0 and sq_check[1]<0 and sq_check[2]>0 and sq_check[3]>0):
            print '2 in 2 out'
            b1 = self.sq_xy[0][1]
            print 'b1', b1
            a1 = abs(m.sqrt(300*300 - (b1-300)*(b1-300))) 
            b2 = self.sq_xy[2][1]
            print b1
            a2 = abs(m.sqrt(300*300 - (b2-300)*(b2-300)))
            print 'ab', a1,b1,a2,b2
            #points of intersection of r1 with rect

            ###################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            #(x*x + (y-300)*(y-300)-300*300)
            if ((self.Dxy[pair_id_up][0]-0)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'out' 
                pair_id_up = pair_id_up + 1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            if ((self.Dxy[pair_id_down][0]-0)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'out' 
                pair_id_down = pair_id_down - 1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            ###################################
            #r1 points are all in r1; but we have to check remaining points for r2:
            #check if they are in r2
            print 'print r2', self.Dxy[pair_id_down+1: pair_id_up]
            updated_r2xy = self.check_if_in_workspace_r2(self.Dxy[pair_id_down+1: pair_id_up])
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, updated_r2xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()
            ###################################

            print 'print r1', self.Dxy[0:pair_id_down+1]
            print 'print r1', self.Dxy[pair_id_up:self.n]

            print 'r1 final', self.Dxy[0:pair_id_down+1] + self.Dxy[pair_id_up:self.n]
            print 'For 2 in 2 out----------------------------------------------------------'
            
            Dr1 = self.Dxy[pair_id_up:self.n] + self.Dxy[0:pair_id_down+1]
            text_file = open("r1.txt", "w")
            np.savetxt(text_file,Dr1, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close() 
            ##############################

        #elif (sq_check[0]<0 or sq_check[1]<0 or (sq_check[0]>0 and sq_check[1]>0) and sq_check[2]>0 and sq_check[3]>0):
        
        elif (sq_check[0]>0 and sq_check[1]>0 and sq_check[2]>0 and sq_check[3]>0 ):
            print 'vertical in tersection R1 ||||||||||||||||||||||||||||'

            a1 = self.sq_xy[0][0]
            b1 = -abs(m.sqrt(300*300 - (a1)*(a1))) + 300
             
            print 'b1', b1
            a2 = self.sq_xy[1][0]
            print 'a2', a2
            
            b2 = abs(m.sqrt(300*300 - (a2)*(a2))) + 300
            print 'ab', a1,b1,a2,b2

            ####################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            if ((self.Dxy[pair_id_up][0]-0)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'out' 
                pair_id_up = pair_id_up +1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            if ((self.Dxy[pair_id_down][0]-0)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'out' 
                pair_id_down = pair_id_down -1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print '0 and 1 are out ----------------------------------------------------------'
            #check if they are in r2
            print 'print r2', self.Dxy[pair_id_down+1: self.n]
            updated_r2xy = self.check_if_in_workspace_r2(self.Dxy[pair_id_down+1: self.n])
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, updated_r2xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            print 'print r1', self.Dxy[pair_id_up:pair_id_down+1]
            Dr1 = self.Dxy[pair_id_up:pair_id_down+1]
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, Dr1, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()
            

        elif (sq_check[0]>0 and sq_check[1]<0 and sq_check[2]>0 and sq_check[3]>0):
            a1 = self.sq_xy[0][0]
            b1 = -abs(m.sqrt(300*300 - (a1)*(a1))) + 300
             
            print 'b1', b1
            b2 = self.sq_xy[1][1]
            print 'b2', b2
            
            a2 = abs(m.sqrt(300*300 - (b2-300)*(b2-300)))
            print 'ab', a1,b1,a2,b2

            ###################
            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            if ((self.Dxy[pair_id_up][0]-0)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'out' 
                pair_id_up = pair_id_up +1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            if ((self.Dxy[pair_id_down][0]-0)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'out' 
                pair_id_down = pair_id_down -1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print '0 out 1 in ---------------------------------------------------------'
            #check if they are in r2
            print 'print r2', self.Dxy[pair_id_down+1: self.n]
            updated_r2xy = self.check_if_in_workspace_r2(self.Dxy[pair_id_down+1: self.n])
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, updated_r2xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            print 'print r1', self.Dxy[pair_id_up:pair_id_down+1]
            Dr1 = self.Dxy[pair_id_up:pair_id_down+1]
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, Dr1, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

        elif (sq_check[0]<0 and sq_check[1]>0 and sq_check[2]>0 and sq_check[3]>0):

            b1 = self.sq_xy[0][1]
            a1 = abs(m.sqrt(300*300 - (b1-300)*(b1-300)))
            print 'b1', b1
            a2 = self.sq_xy[1][0]
            print 'a2', a2
            
            b2 = abs(m.sqrt(300*300 - (a2)*(a2))) + 300
            print 'ab', a1,b1,a2,b2

            ####################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            if ((self.Dxy[pair_id_up][0]-0)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'out' 
                pair_id_up = pair_id_up +1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            if ((self.Dxy[pair_id_down][0]-0)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'out' 
                pair_id_down = pair_id_down -1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print '0 in 1 out ----------------------------------------------------------'
            #check if they are in r2
            print 'print r2', self.Dxy[pair_id_down+1: pair_id_up]
            updated_r2xy = self.check_if_in_workspace_r2(self.Dxy[pair_id_down+1: pair_id_up])
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, updated_r2xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            Dr1 = self.Dxy[pair_id_up:self.n] + self.Dxy[0:pair_id_down+1]
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, Dr1, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()        

            
        else :
            print 'Please do again !! for R1'  

        return 0


    def methodR2(self, sq_check):
        if (sq_check[0]<0 and sq_check[1]<0 and sq_check[2]<0 and sq_check[3]<0):
            print 'all in for R2'
            b1 = self.sq_xy[0][1]
            print 'b1', b1
            a1 = abs(m.sqrt(300*300 - (b1-300)*(b1-300))) 
            b2 = self.sq_xy[2][1]
            print 'b1', b1
            a2 = abs(m.sqrt(300*300 - (b2-300)*(b2-300)))
            print 'ab', a1,b1,a2,b2

            ####################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            if ((self.Dxy[pair_id_up][0]-0)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'inside r1', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'outside r1' 
                pair_id_up = pair_id_up + 1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            if ((self.Dxy[pair_id_down][0]-0)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'inside r1', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'outside r1' 
                pair_id_down = pair_id_down - 1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]


            print 'print r2', self.Dxy[pair_id_down+1: pair_id_up]
            print 'For all in R2 ----------------------------------------------------------'
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, self.Dxy[pair_id_down+1: pair_id_up], fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            print 'print r1', self.Dxy[0:pair_id_down+1]
            print 'print r1', self.Dxy[pair_id_up:self.n] # we want till n-1 = 79

            print 'r1 final', self.Dxy[0:pair_id_down+1] + self.Dxy[pair_id_up:self.n]

            Dr1 = self.Dxy[pair_id_up:self.n] + self.Dxy[0:pair_id_down+1]
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, Dr1, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close() 

            ###################

                        
        elif (sq_check[0]>0 and sq_check[1]>0 and sq_check[2]<0 and sq_check[3]<0):
            print '2 out 2 in for r2'
            b1 = self.sq_xy[0][1]
            print 'b1', b1
            a1 = -abs(m.sqrt(300*300 - (b1-300)*(b1-300))) + 500
            b2 = self.sq_xy[2][1]
            print b1
            a2 = -abs(m.sqrt(300*300 - (b2-300)*(b2-300))) + 500
            print 'ab', a1,b1,a2,b2

            ###################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            # check if inside r2
            if ((self.Dxy[pair_id_up][0]-500)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'outside r2' 
                pair_id_up = pair_id_up - 1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            # check if inside r2
            if ((self.Dxy[pair_id_down][0]-500)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'outside r2' 
                pair_id_down = pair_id_down + 1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print 'print r2', self.Dxy[pair_id_down: pair_id_up+1]
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, self.Dxy[pair_id_down: pair_id_up+1], fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            ###################################
            #r2 points are all in r2; but we have to check remaining points for r1:
            #check if they are in r1
            print 'print r1', self.Dxy[0:pair_id_down]
            print 'print r1', self.Dxy[pair_id_up+1:self.n]

            print 'r1 final', self.Dxy[0:pair_id_down] + self.Dxy[pair_id_up+1:self.n]
            print 'For 2 in 2 out----------------------------------------------------------'
            Dr1 = self.Dxy[pair_id_up+1:self.n] + self.Dxy[0:pair_id_down]
            
            updated_r1xy = self.check_if_in_workspace_r1(Dr1)
            
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, updated_r1xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()
            ###################################
            

        elif (sq_check[0]>0 and sq_check[1]>0 and sq_check[2]>0 and sq_check[3]>0):
            print 'All out for r2 ----------------------------'
            a1 = self.sq_xy[3][0]
            print 'a1', a1
            b1 = -abs(m.sqrt(300*300 - (a1-500)**2)) + 300
            a2 = self.sq_xy[2][0]
            print 'b1', b1
            b2 = +abs(m.sqrt(300*300 - (a2-500)**2)) + 300
            print 'ab', a1,b1,a2,b2

            ###################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            # check if inside r2
            if ((self.Dxy[pair_id_up][0]-500)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'outside r2' 
                pair_id_up = pair_id_up - 1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            # check if inside r2
            if ((self.Dxy[pair_id_down][0]-500)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'outside r2' 
                pair_id_down = pair_id_down + 1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print 'print r2', self.Dxy[pair_id_down: pair_id_up+1]
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, self.Dxy[pair_id_down: pair_id_up+1], fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            ###################################
            #r2 points are all in r2; but we have to check remaining points for r1:
            #check if they are in r1
            print 'print r1', self.Dxy[0:pair_id_down]
            print 'print r1', self.Dxy[pair_id_up+1:self.n]

            print 'R1 ----------------------------------------------------------'
            Dr1 = self.Dxy[pair_id_up+1:self.n] + self.Dxy[0:pair_id_down]
            
            updated_r1xy = self.check_if_in_workspace_r1(Dr1)
            
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, updated_r1xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()
            ###################################

        elif (sq_check[0]>0 and sq_check[1]>0 and sq_check[2]>0 and sq_check[3]<0):
            print '2 out and 3 in for r2-------------------'
            b1 = self.sq_xy[3][1]
            print 'b1', b1
            a1 = -abs(m.sqrt(300*300 - (b1-300)*(b1-300))) + 500
            a2 = self.sq_xy[2][0]
            print b1
            b2 = abs(m.sqrt(300*300 - (a2-500)*(a2-500))) + 500
            print 'ab', a1,b1,a2,b2

            ###################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            # check if inside r2
            if ((self.Dxy[pair_id_up][0]-500)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'outside r2' 
                pair_id_up = pair_id_up - 1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            # check if inside r2
            if ((self.Dxy[pair_id_down][0]-500)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'outside r2' 
                pair_id_down = pair_id_down + 1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print 'print r2', self.Dxy[pair_id_down: pair_id_up+1]
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, self.Dxy[pair_id_down: pair_id_up+1], fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            ###################################
            #r2 points are all in r2; but we have to check remaining points for r1:
            #check if they are in r1
            print 'print r1', self.Dxy[0:pair_id_down]
            print 'print r1', self.Dxy[pair_id_up+1:self.n]

            print 'R1 ----------------------------------------------------------'
            Dr1 = self.Dxy[pair_id_up+1:self.n] + self.Dxy[0:pair_id_down]
            
            updated_r1xy = self.check_if_in_workspace_r1(Dr1)
            
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, updated_r1xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()
            ###################################

        elif (sq_check[0]>0 and sq_check[1]>0 and sq_check[2]<0 and sq_check[3]>0):
            print '2 in and 3 out for r2-------------------'
            a1 = self.sq_xy[3][0]
            print 'a1', a1
            b1 = -abs(m.sqrt(300*300 - (a1-500)*(a1-500))) + 300
            b2 = self.sq_xy[2][1]
            print 'b2', b2
            a2 = -abs(m.sqrt(300*300 - (b2-300)*(b2-300))) + 500
            print 'ab', a1,b1,a2,b2

            ###################
            print '1-',a1
            print '2-',b1

            print 'app', self.Dxy + [[a1,b1]]
            pair_id_up = cl.closestpair(self.Dxy + [[a1,b1]], self.Dxy)
            print 'pair index up', pair_id_up

            # check if inside r2
            if ((self.Dxy[pair_id_up][0]-500)**2 + (self.Dxy[pair_id_up][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]

            else:
                print 'outside r2' 
                pair_id_up = pair_id_up - 1
                print 'in', self.Dxy[pair_id_up][0], self.Dxy[pair_id_up][1]
                
            pair_id_down = cl.closestpair(self.Dxy + [[a2,b2]], self.Dxy)
            print 'pair index down', pair_id_down

            # check if inside r2
            if ((self.Dxy[pair_id_down][0]-500)**2 + (self.Dxy[pair_id_down][1]-300)**2 - 300*300)  < 0 :
                print 'inside r2', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            else:
                print 'outside r2' 
                pair_id_down = pair_id_down + 1
                print 'in', self.Dxy[pair_id_down][0], self.Dxy[pair_id_down][1]

            print 'print r2', self.Dxy[pair_id_down: pair_id_up+1]
            
            text_file = open("r2.txt", "w")
            np.savetxt(text_file, self.Dxy[pair_id_down: pair_id_up+1], fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()

            ###################################
            #r2 points are all in r2; but we have to check remaining points for r1:
            #check if they are in r1
            print 'print r1', self.Dxy[0:pair_id_down]
            print 'print r1', self.Dxy[pair_id_up+1:self.n]

            print 'R1 ----------------------------------------------------------'
            Dr1 = self.Dxy[pair_id_up+1:self.n] + self.Dxy[0:pair_id_down]
            
            updated_r1xy = self.check_if_in_workspace_r1(Dr1)
            
            text_file = open("r1.txt", "w")
            np.savetxt(text_file, updated_r1xy, fmt = ['%f','%f'])#, header='x_coordinate y_coordinate')
            text_file.close()
            ###################################
            
                        
        else :
            print 'Please do again!!! for R2'  

        return 7


    def evalCircle1(self, x, y):
        if (x*x + (y-300)*(y-300)-300*300)  < 0:
            print 'in' 
            val = -1 
        elif (x*x + (y-300)*(y-300)-300*300)  > 0:
            print 'out'
            val = 1
        else :
            print 'on'
            val = 0     

        return val

    def evalCircle2(self, x, y):
        if ((x-500)*(x-500) + (y-300)*(y-300)-300*300)  < 0:
            print 'in' 
            val = -1 
        elif ((x-500)*(x-500) + (y-300)*(y-300)-300*300)  > 0:
            print 'out'
            val = 1
        else :
            print 'on'
            val = 0     

        return val

    
    def checkR1(self, r) :

        square_check = 2*np.ones(4)
        print square_check 

        for i in range(0, 4):
            square_check[i] = self.evalCircle1(self.sq_xy[i][0],self.sq_xy[i][1])
        print 'square_check', square_check
    
        return square_check

    def checkR2(self, r) :

        square_check = 2*np.ones(4)
        print square_check 

        for i in range(0, 4):
            square_check[i] = self.evalCircle2(self.sq_xy[i][0],self.sq_xy[i][1])
        print 'square_check', square_check
    
        return square_check
    
if __name__=='__main__' :
    
    p = division()
    cx, cy = p.read()
    print 'cx cy------------------', cx, cy

    r = p.compare(cx, cy)
    
