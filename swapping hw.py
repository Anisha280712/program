def swap_three (a, b, c):
    a,b,c=c,a,b
    return a,b,c
x,y,z=10,20,30
print("before:",x,y,z)
x,y,z=swap_three(x,y,z)
print("After:",x,y,z)