import math
#pip3 install sympy
import sympy as sym


def chebyshev(n, start, end):
    #list of x positions from chebyshev spacing
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
def freudstien(listx, maxx,minx, funct, gmin, gmax, bmin, bmax):
    #turn xs into 3 sets of thetas
    #gamma=105-165 beta= 240-330 angles

    #find gamma=ax+b
    #t2=a, b2=b
    t2,b2= sym.symbols('t2,b2')
    t21= sym.Eq(minx*t2+b2,gmin)
    t22= sym.Eq(maxx*t2+b2,gmax)
    tb2= sym.solve([t21,t22],(t2,b2))
    #[A,B]
    #print(tb2)
    #find beta=cy+d
    #t4=c, b4=d
    t4,b4= sym.symbols('t4,b4')
    t41= sym.Eq(funct(minx)*t4+b4,bmin)
    t42= sym.Eq(funct(maxx)*t4+b4,bmax)
    tb4= sym.solve([t41,t42],(t4,b4))
    #print(tb4)

    # theta21=tb2['t2']*listx[0]+tb2['b2']
    # theta41=tb4['t4']*listx[0]+tb4['b4']
    # theta22=tb2['t2']*listx[1]+tb2['b2']
    # theta42=tb4['t4']*listx[1]+tb4['b4']
    # theta23=tb2['t2']*listx[2]+tb2['b2']
    # theta43=tb4['t4']*listx[2]+tb4['b4']
    #use values of a,b,c,d to find theta 2,4 values at chebyshev spacing points
    theta21=math.radians(tb2[t2]*listx[0]+tb2[b2])
    theta41=math.radians(tb4[t4]*funct(listx[0])+tb4[b4])
    theta22=math.radians(tb2[t2]*listx[1]+tb2[b2])
    theta42=math.radians(tb4[t4]*funct(listx[1])+tb4[b4])
    theta23=math.radians(tb2[t2]*listx[2]+tb2[b2])
    theta43=math.radians(tb4[t4]*funct(listx[2])+tb4[b4])
    #
    #simultaneous with three freudenstiens
    k1,k2,k3 = sym.symbols('k1,k2,k3')
    Eq1= sym.Eq(k1*math.cos(theta21)+k2*math.cos(theta41)+k3, math.cos(theta21-theta41))
    Eq2= sym.Eq(k1*math.cos(theta22)+k2*math.cos(theta42)+k3, math.cos(theta22-theta42))
    Eq3= sym.Eq(k1*math.cos(theta23)+k2*math.cos(theta43)+k3, math.cos(theta23-theta43))
    result = sym.solve([Eq1,Eq2,Eq3],(k1,k2,k3))
    #print(result)
    #convert k values  into lengths
    # set l1 to 1
    #result[0]=k1
    res= dict()
    res["l1"]=1
    res["l4"]=res["l1"]/result[k1]
    res["l2"]=res["l1"]/result[k2]
    l3 =sym.symbols('l3')
    eq4= sym.Eq((l3*l3-res["l1"]*res["l1"]-res["l2"]*res["l2"]-res["l4"]*res["l4"])/(2*res["l4"]*res["l2"]), result[k3])
    res["l3"]=sym.solve(eq4,l3)
    res["l3"]=res["l3"][1]
    #print(res)


    #l1=0
    return res  

def freudstienloop(listx, maxx,minx, funct):
    #solution to return
    sol= dict()
    sol["l1"]=-1
    sol["l2"]=-1
    sol["l3"]=-1
    sol["l4"]=-1
    #start at nice angles
    gmin =105
    gmax=165
    bmin=240
    bmax=330
    #repeat until all lengths are greater than 0
    while(sol["l1"]<0 or sol["l2"]<0 or sol["l3"]<0 or sol["l4"]<0):
        sol=freudstien(listx,maxx,minx,funct,gmin,gmax,bmin,bmax)
        gmax+=15
        bmax+=15
        gmax= gmax%360
        bmax= bmax%360
    
    print(sol)
    return sol
