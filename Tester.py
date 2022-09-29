from cmath import log10
import math
from tkinter import *

from window import Window
from mathstuff import chebyshev, freudstienloop

# def chebyshev(n, start, end):
#     listx=[]
#     for j in range(n):
#         listx.append(0.5*(start+end)-0.5*(end-start)*math.cos((2*j)*math.pi/6))
#     print("Chebyshcev spacing is:")
#     print("in range-",start,":",end)
#     print(listx)
#     return listx

def main():
    #print (eval("x+5"))
    root=Tk()
    root.title("4-bar")
    w=1500
    h=1000
    root.minsize(w,h)
    window= Window(w,h)
    window.pack(pady=40,padx=40)
    #window.create_circle(250,250,50 ,"blue")
    #yV x>
    # 1st Example
    def functii(x):
        return log10(x).real

    window.graph(functii,1,2)
    listx=chebyshev(3,1,2)
    window.drawspacing(functii,listx,1,2)


    freudstienloop(listx,1,2,functii)

    #2nd example
    def functii(x):
        return math.sin(x)


    window.graph(functii,0,3)
    listx=chebyshev(3,0,3)
    window.drawspacing(functii,listx,0,3)
    freudstienloop(listx,0,3,functii)


    #must be last
    root.mainloop() 


if __name__=="__main__":
    main()


