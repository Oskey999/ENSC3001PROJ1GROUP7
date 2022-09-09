import math

def chebyshev(n, start, end):
    listx=[]
    for j in range(n):
        listx.append(0.5*(start+end)-0.5*(end-start)*math.cos((2*j)*math.pi/6))
    print("Chebyshcev spacing is:")
    print("in range-",start,":",end)
    print(listx)
    return listx