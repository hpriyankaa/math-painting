
import numpy as np
from PIL import Image
class Canvas:
    def __init__(self,width,height,color):
        self.width=width
        self.color=color
        self.height=height

        self.data=np.zeros((self.height,self.width,3), dtype=np.uint8)

        self.data[:]=self.color
    def make(self,imagepath):
        img = Image.fromarray(self.data,'RGB')
        img.save(f'{imagepath}.png')
class Square:
    def __init__(self,x,y,side,color):
        self.x=x
        self.y=y
        self.side=side
        self.color=color
    def draw(self,canvas):
        canvas.data[self.x:self.x+self.side,self.y:self.y+self.side]=self.color
class Rectangle:
    def __init__(self,x,y,width, height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
    def draw(self,canvas):
        canvas.data[self.x:(self.x+self.height), self.y:(self.y+self.width)]=self.color
cw=int(input("enter canvas width: "))
ch=int(input("enter canvas height: "))
cr=int(input("enter r value for canvas: "))
cg=int(input("enter g value for canvas: "))
cb=int(input("enter b value for canvas: "))
sh=input("enter the shape to be drawn(square,rectangle,quit):  ").strip().lower()
cn=input("enter canvas filename: ")
canvas=Canvas(width=cw,height=ch,color=(cr,cg,cb))
if sh == 'square':
    x1 = int(input("enter x coordinates: "))
    y1 = int(input("enter y coordinates: "))
    s = int(input("enter side: "))
    sr = int(input("enter r value for canvas: "))
    sg = int(input("enter g value for canvas: "))
    sb = int(input("enter b value for canvas: "))
    s1 = Square(x=x1, y=y1, side=s, color=(sr, sg, sb))
    s1.draw(canvas)
elif sh == 'rectangle':
    x2 = int(input("enter x coordinates: "))
    y2 = int(input("enter y coordinates: "))
    w = int(input("enter width: "))
    h = int(input("enter height: "))
    rr = int(input("enter r value for canvas: "))
    rg = int(input("enter g value for canvas: "))
    rb = int(input("enter b value for canvas: "))
    r1 = Rectangle(x=x2, y=y2, width=w, height=h, color=(rr, rg, rb))
    r1.draw(canvas)

else:
    print("quit")
canvas.make(cn)









