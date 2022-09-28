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
def freudstien(listx,listt, maxx,minx, funct):
    #turn xs into 3 sets of thetas
    #theta2min,theta2max, theta4min, theta4max
    t2,b2= sym.symbols('t2,b2')
    t21= sym.Eq(minx*t2+b2,listt[0])#theta2
    t22= sym.Eq(maxx*t2+b2,listt[1])#theta4
    tb2= sym.solve([t21,t22],(t2,b2))

    t4,b4= sym.symbols('t4,b4')
    t41= sym.Eq(minx*t4+b4,listt[2])#theta2
    t42= sym.Eq(maxx*t4+b4,listt[3])#theta4
    tb4= sym.solve([t21,t22],(t4,b4))

    theta21=tb2[0]*listx[0]+tb2[1]
    theta41=tb4[0]*listx[0]+tb4[1]
    theta22=tb2[0]*listx[1]+tb2[1]
    theta42=tb4[0]*listx[1]+tb4[1]
    theta23=tb2[0]*listx[2]+tb2[1]
    theta43=tb4[0]*listx[2]+tb4[1]
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
    res["l4"]=res["l1"]/result[0]
    res["l2"]=res["l1"]/result[1]
    l3 =sym.symbols('l3')
    eq4= sym.Eq((l3^2-res["l1"]^2-res["l2"]^2-res["l4"]^2)/(2*res["l4"]*res["l2"]), result[2])
    res["l3"]=sym.solve(eq4,l3)
    print(res)


    #l1=0
    return res