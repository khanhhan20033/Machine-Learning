a = int(input("nhap so can nhap:"))
sum1=""
for i in range(4):
    so=0
    for j in range(i+1):
        so+=1
    sum1+=str(so)
sum1=int(sum1)*a
print(sum1)