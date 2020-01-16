
import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from tkinter import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
import csv
from math import sin



#reading file
#/Users/veer/helloPython

data = pd.read_csv("/Users/veer/helloPython/DigitRecognition/data/train.csv").values
clf = DecisionTreeClassifier()

#training
xtrain = data[0:21000,1:]
xtrain_label = data[0:21000,0]
clf.fit(xtrain,xtrain_label)


#UI
class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        white = (255, 255, 255)
        self.image1 = Image.new("RGB", (600, 600), white)
        self.draw = ImageDraw.Draw(self.image1)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 10
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        
    def use_pen(self):
        self.activate_button(self.pen_button)
   
    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
        
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = 10
        paint_color = 'white' if self.eraser_on else self.color
        
        if self.old_x and self.old_y:
            
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)

            self.draw.line([self.old_x, self.old_y, event.x, event.y], width=6, fill= 0)
                                                    
        self.old_x = event.x
        self.old_y = event.y
   
        filename = "userDrawing.jpg"
        self.image1.save(filename)
    

    def reset(self, event):
        self.old_x, self.old_y = None, None



if __name__ == '__main__':
    Paint()



#UI tester 

'''
userData = pd.read_csv("userDrawing.jpg").values

detectImage = userData
detectImage.shape=(28,28)
print(f"Your Number:{clf.predict(detectImage)}")
'''

#testing
'''
xtest=data[21000:,1:]
d = xtest[9]
d.shape=(28,28)
pt.imshow(255-d, cmap = 'gray')
print(f"That number is:{clf.predict([xtest[9]])}")

pt.show()
'''
