import matplotlib.pyplot as plt
import numpy as np
import sys
from itertools import product, combinations
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d

class Cube:
    def __init__(self):
        """
            UUU
            UUU
            UUU
        LLL FFF RRR BBB
        LLL FFF RRR BBB
        LLL FFF RRR BBB
            DDD
            DDD
            DDD

        F - front
        U - up
        L - left
        R - right
        B - back
        D - down


        """
        self.front = [None] * 9
        self.up = self.front.copy()
        self.left = self.front.copy()
        self.right = self.front.copy()
        self.back = self.front.copy()
        self.down = self.front.copy()
        self.default_face()
    
    def default_face(self):
        for i in range(9):
            self.front[i] = 'white'
            self.up[i] = 'red'
            self.left[i] = 'blue'
            self.right[i] = 'green'
            self.back[i] = 'yellow'
            self.down[i] = 'orange'
    
    def display(self, disp_time = 5):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        r = [-3, 3]

        # create a black cube outline
        for s, e in combinations(np.array(list(product(r,r,r))), 2):
            if np.sum(np.abs(s-e)) == r[1]-r[0]:
                ax.plot3D(*zip(s,e), color="black")
        
        # ***** Graphing the faces *****
        face_count = 0
        faces = [self.right, self.left, self.back, self.front, self.up, self.down]
        for dir in ['x','y','z']:
            for mult in [1,-1]:
                count = 0
                for i in range(3):
                    for j in range (3):
                        subface = Rectangle((-3 + j * 2, 1 - i * 2), 2,2, facecolor =  faces[face_count][count])
                        ax.add_patch(subface)
                        
                        art3d.pathpatch_2d_to_3d(subface, z=3*mult, zdir=dir)
                        count += 1
                
                face_count += 1



        timer = fig.canvas.new_timer(interval = disp_time*1000)
        timer.add_callback(plt.close)

        timer.start()

        plt.show()

        

    def rotate_top_cw(self):
        tempup = [None] * 9
        """
        123
        456  
        789

        741
        852
        963
        """
        numbering = [6,3,0,7,4,1,8,5,2]
        for i, j in enumerate(numbering):
            tempup[i] = self.up[j]

        tempfront = [None] * 9
        templeft = [None] * 9
        tempright = [None] * 9
        tempback = [None] * 9
        for i in range(9):
            if i < 3:
                tempfront[i] = self.right[i]
                templeft[i] = self.front[i]
                tempback[i] = self.left[i]
                tempright[i] = self.back[i]
            else:
                tempfront[i] = self.front[i]
                templeft[i] = self.left[i]
                tempback[i] = self.back[i]
                tempright[i] = self.right[i]
        
        self.up = tempup
        self.front = tempfront
        self.left = templeft
        self.back = tempback
        self.right = tempright

    def rotate_front_cw(self):
        tempfront = [None] * 9
        numbering = [6,3,0,7,4,1,8,5,2]
        for i, j in enumerate(numbering):
            tempfront[i] = self.front[j]

        tempup = self.up.copy()
        tempup[6] = self.left[6]
        tempup[7] = self.left[3]
        tempup[8] = self.left[0]
        templeft = self.left.copy()
        templeft[0] = self.down[6]
        templeft[3] = self.down[7]
        templeft[6] = self.down[8]
        tempright = self.right.copy()
        tempright[0] = self.up[6]
        tempright[3] = self.up[7]
        tempright[6] = self.up[8]
        tempdown = self.down.copy()
        tempdown[6] = self.right[6]
        tempdown[7] = self.right[3]
        tempdown[8] = self.right[0]

        self.front = tempfront
        self.up = tempup
        self.right = tempright
        self.down = tempdown
        self.left = templeft

    def rotate_right_cw(self):
        tempright = [None] * 9
        numbering = [6,3,0,7,4,1,8,5,2]
        for i, j in enumerate(numbering):
            tempright[i] = self.right[j]

        tempfront = self.front.copy()
        tempfront[2] = self.down[8] 
        tempfront[5] = self.down[5]
        tempfront[8] = self.down[2]

        tempup = self.up.copy()
        tempup[2] = self.front[2]
        tempup[5] = self.front[5]
        tempup[8] = self.front[8]

        tempback = self.back.copy()
        tempback[2] = self.up[8]
        tempback[5] = self.up[5]
        tempback[8] = self.up[2]

        tempdown = self.down.copy()
        tempdown[2] = self.back[2]
        tempdown[5] = self.back[5]
        tempdown[8] = self.back[8]

        self.right = tempright
        self.front = tempfront
        self.up = tempup
        self.back = tempback
        self.down = tempdown

    def rotate_left_cw(self):
        templeft = [None] * 9
        numbering = [6,3,0,7,4,1,8,5,2]
        for i, j in enumerate(numbering):
            templeft[i] = self.left[j]

        # 0 3 6
        tempup = self.up.copy()
        tempup[0] = self.front[0]
        tempup[3] = self.front[3]
        tempup[6] = self.front[6]
        tempback = self.back.copy()
        tempback[0] = self.up[6]
        tempback[3] = self.up[3]
        tempback[6] = self.up[0]
        tempdown = self.down.copy()
        tempdown[0] = self.back[0]
        tempdown[3] = self.back[3]
        tempdown[6] - self.back[6]
        tempfront = self.front.copy()
        tempfront[0] = self.down[6]
        tempfront[3] = self.down[3]
        tempfront[6] = self.down[0]

        self.left = templeft
        self.up = tempup
        self.back = tempback
        self.down = tempdown
        self.front = tempfront

    def rotate_back_cw(self):
        tempback = [None] * 9
        numbering = [6,3,0,7,4,1,8,5,2]
        for i, j in enumerate(numbering):
            tempback[i] = self.back[j]

        tempup = self.up.copy()
        tempup[0] = self.left[8]
        tempup[1] = self.left[5]
        tempup[2] = self.left[2]

        tempright = self.right.copy()
        tempright[2] = self.up[0]
        tempright[5] = self.up[1]
        tempright[8] = self.up[2]

        tempdown = self.down.copy()
        tempdown[0] = self.right[8] 
        tempdown[1] = self.right[5]
        tempdown[2] = self.right[2]

        templeft = self.left.copy()
        templeft[2] = self.down[0]
        templeft[5] = self.down[1]
        templeft[8] = self.down[2]

        self.back = tempback
        self.up = tempup
        self.right = tempright
        self.down = tempdown
        self.left = templeft

    def rotate_down_cw(self):
        tempdown = [None] * 9
        numbering = [6,3,0,7,4,1,8,5,2]
        for i, j in enumerate(numbering):
            tempdown[i] = self.down[j]

        tempfront = self.front.copy()
        templeft = self.left.copy()
        tempright = self.right.copy()
        tempback = self.back.copy()

        for i in [6,7,8]:
            tempfront[i] = self.right[i]
            templeft[i] = self.front[i]
            tempback[i] = self.left[i]
            tempright[i] = self.back[i]
        
        self.down = tempdown
        self.front = tempfront
        self.left = templeft
        self.back = tempback
        self.right = tempright


    def capture_front():
        pass
        return [[],[],[],[],[],[]]
    def capture_back():
        pass
        return [[],[],[],[],[],[]]

    def get_curr_state(self):
        for _ in range(4):
            front = self.capture_front()
            self.front[2] = front[0]
            self.front[5] = front[1]
            self.front[8] = front[2]
            self.right[0] = front[3]
            self.right[3] = front[4]
            self.right[6] = front[5]

            back = self.capture_back()
            self.back[0] = back[0]
            self.back[3] = back[1]
            self.back[6] = back[2]
            self.left[2] = back[3]
            self.left[5] = back[4]
            self.left[8] = back[5]

            self.rotate_front_cw()
            self.rotate_back_cw()

        for _ in range(4):
            front = self.capture_front()
            self.front[2] = front[0]
            self.front[5] = front[1]
            self.front[8] = front[2]
            self.right[0] = front[3]
            self.right[3] = front[4]
            self.right[6] = front[5]

            back = self.capture_back()
            self.back[0] = back[0]
            self.back[3] = back[1]
            self.back[6] = back[2]
            self.left[2] = back[3]
            self.left[5] = back[4]
            self.left[8] = back[5]

            self.rotate_right_cw()
            self.rotate_left_cw()



c = Cube()
c.display(disp_time = 100)
c.rotate_front_cw()
c.display(disp_time = 500)
c.rotate_top_cw()
c.display(disp_time = 500)
c.rotate_right_cw()
c.display(disp_time = 100)
c.rotate_left_cw()
c.display(disp_time = 100)
c.rotate_back_cw()
c.display(disp_time = 100)
c.rotate_down_cw()
c.display(disp_time = 100)