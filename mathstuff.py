import math
#pip3 install sympy
import sympy as sym


def chebyshev(n, start, end):
    listx=[]
    for j in range(n):
        listx.append(0.5*(start+end)-0.5*(end-start)*math.cos((2*j+1)*math.pi/6))
    print("Chebyshev spacing is:")
    print("in range-",start,":",end)
    print(listx)
    return listx

# express in terms of list of points from chebyshev
# k1cos(theta2)+k2cos(theta4)+k3= cos(theta2-theta4)
#k1=l1/l4
#k2=l1/l2
#k3= 
def freudstien(x1,x2,x3, funct):
    #turn xs into 3 sets of thetas
    theta21=3
    theta41=4
    theta22=5
    theta42=3
    theta23=2
    theta43=4
    #
    #simultaneous with three freudenstiens
    k1,k2,k3 = sym.symbols('k1,k2,k3')
    Eq1= sym.Eq(k1*math.cos(theta21)+k2*math.cos(theta41)+k3, math.cos(theta21-theta41))
    Eq2= sym.Eq(k1*math.cos(theta22)+k2*math.cos(theta42)+k3, math.cos(theta22-theta42))
    Eq3= sym.Eq(k1*math.cos(theta23)+k2*math.cos(theta43)+k3, math.cos(theta23-theta43))
    result = sym.solve([Eq1,Eq2,Eq3],(k1,k2,k3))
    print(result)
    #convert k into ls
    # set l1 to 1
    #result[0]=k1
    res= dict()
    res["l1"]=1
    res["l4"]=1/result[0]
    res["l2"]=1/result[1]
    l3 =sym.symbols('l3')
    eq4= sym.Eq((l3^2-res["l1"]^2-res["l2"]^2-res["l4"]^2)/(2*res["l4"]*res["l2"]), result[2])
    res["l3"]=sym.solve(eq4,l3)
    print(res)


    #l1=0
    return res