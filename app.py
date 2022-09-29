#for the math
from cmath import log10
import math
#for the window
from tkinter import *
from window import Window
from mathstuff import chebyshev, freudstienloop
#for the evaluation
import re

def main():
    #make window
    root=Tk()
    root.title("4-bar")
    w=1500
    h=1000
    root.minsize(w,h)
    window= Window(w,h)
    window.pack(pady=40,padx=40)
    #prompts start
    print("Project")
    #get input function
    fun=input("type the function you want to use (use x)\n")
    #define function
    def functii(xv):
        x=xv
        #filter sin
        t=fun
        if "sin" in fun:
            x=math.sin(xv)
            t=fun.replace("sin","")
        #filter log
        elif "log" in fun:
            x=math.log10(xv)
            t=fun.replace("log","")
        #will evaluate polynomial with a set value of x
        return eval(t)
    #find min and max x value
    rangemin= eval(input("what is the minimum value of x?\n"))
    rangemax =eval(input("what is the maximum value of x?\n"))
    #math to do
    #graph function
    window.graph(functii,rangemin,rangemax)
    #find chebyshev spacing and put in a list of x values
    listx=chebyshev(3,1,2)
    #draw points on graph for points of chebyshev spacing
    window.drawspacing(functii,listx,rangemin,rangemax)
    freudstienloop(listx,rangemin,rangemax,functii)
    root.mainloop()




if __name__=="__main__":
    main()