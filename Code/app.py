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
   # root=Tk()
   # root.title("4-bar")
   # w=1500
   # h=1000
   # root.minsize(w,h)
    #window= Window(w,h)
    #window.pack(pady=40,padx=40)

    #prompts start
    print("Project")
    #get input function
    fun=input("type the function you want to use (use x)\n")

    #define function
    # pretty weak
    def functii(xv):
        x=xv
        #filter sin
        t=fun
        s=0
        l=0
        if "sin" in fun:
            s=math.sin(xv)
            t=t.replace("sin(x)","s")
        #filter log
        if "log" in fun:
            l=math.log10(xv)
            t=t.replace("log(x)","l")
        #will evaluate polynomial with a set value of x
        return eval(t)

    #find min and max x value
    min=input("what is the minimum value of x?\n")
    max=input("what is the maximum value of x?\n")
    pi= math.pi
    rangemin= eval(min)
    rangemax =eval(max)

    #math to do
    #graph function
    #window.graph(functii,int(rangemin),int(rangemax)+1)
    #find chebyshev spacing and put in a list of x values
    listx=chebyshev(3,rangemin,rangemax)
    #draw points on graph for points of chebyshev spacing
    #window.drawspacing(functii,listx,int(rangemin),int(rangemax)+1)
    # finds the 4 lengths
    res=freudstienloop(listx,rangemin,rangemax,functii)
    print("l1:"+str(res["l1"]))
    print("l2:"+str(res["l2"]))
    print("l3:"+str(res["l3"]))
    print("l4:"+str(res["l4"]))
    #window.draw4bar(res,2,functii,int(rangemin),int(rangemax)+1)

    #for the window must be last
   # root.mainloop()




if __name__=="__main__":
    main()