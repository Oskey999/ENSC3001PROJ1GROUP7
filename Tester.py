from cmath import log10
import math
from tkinter import *

from window import Window

def chebyshev(n, start, end):
    listx=[]
    for j in range(n):
        listx.append(0.5*(start+end)-0.5*(end-start)*math.cos((2*j)*math.pi/6))
    print(listx)
    return listx

def main():
    root=Tk()
    root.title("4-bar")
    w=500
    h=500
    root.minsize(w,h)
    window= Window(w,h)
    window.pack(pady=40,padx=40)
    #window.create_circle(250,250,50 ,"blue")
    #yV x>
    # 1st Example
    def functii(x):
        return log10(x).real

    window.graph(functii,1,2)
    #chebyshev(3,1,2)
    window.drawspacing(functii,chebyshev(3,1,2),1,2)

    #2nd example
    # def functii(x):
    #     return math.sin(x)

    # window.graph(functii,0,3)

    #must be last
    root.mainloop() 


if __name__=="__main__":
    main()


