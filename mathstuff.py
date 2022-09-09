import math

def chebyshev(n, start, end):
    listx=[]
    for j in range(n):
        listx.append(0.5*(start+end)-0.5*(end-start)*math.cos((2*j)*math.pi/6))
    print("Chebyshev spacing is:")
    print("in range-",start,":",end)
    print(listx)
    return listx

# express in terms of list of points from chebyshev
# k1cos(theta2)+k2cos(theta4)+k3= cos(theta2-theta4)
def freudstien():
    return 0