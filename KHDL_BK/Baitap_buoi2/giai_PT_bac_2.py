import math

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
delta=math.pow(b,2)-4*a*c
if (delta<0):
    print("Phuong trinh vo nghiem")
elif delta==0:
    print("Phuong trinh co nghiem kep x="+str(-b/(2*a)))
else:
    print(f"x1 = {(-b+math.sqrt(delta))/(2*a)}")
    print(f"x2 = {(-b-math.sqrt(delta))/(2*a)}")