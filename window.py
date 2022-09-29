from tkinter import *



class Window(Canvas):
    def __init__(self,width1,height1):
        super().__init__( width=width1, height=height1, bg="white")
        self.width=width1
        self.height= height1

    def create_circle(self,x, y, r, color): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.create_oval(x0, y0, x1, y1,fill=color)

    def graph(self,func,startx, endx):
        rangex=endx-startx
        
        x=startx
        xl=0
        maxy=max(func(value/10) for value in range(startx, (endx+1)*10-startx))+(self.height/20000)
        while x<endx:
            y=func(x)
            x+=rangex/self.width
            self.create_circle(xl,self.height*(1-y/maxy),3,"red")
            xl+=1

    def drawspacing(self,func,listx,startx, endx):
        
            rangex=endx-startx
            maxy=max(func(value/10) for value in range(startx, (endx+1)*10-startx))+(self.height/20000)
            for x in listx:
                y=func(x)
                self.create_circle((x-startx)*self.width/rangex,self.height*(1-y/maxy),6,"blue")
            

   
            
    
