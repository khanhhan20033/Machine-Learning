def sapxep(lst1,lst2):
    if lst1[0]==lst2[0]:
        if lst1[1]==lst2[2]:
            return lst1[2]>lst2[2]
        else:
            return lst1[1]>lst2[1]
    else:
        return lst1[0]>lst2[0]
lst=[]
n=int(input("Hay nhap so luong nguoi can do:"))
for i in range(n):
    print("Nguoi thu "+str(i+1)+":")
    name=input("Ten:")
    tuoi=int(input("Tuoi:"))
    score=int(input("Score:"))
    lst.append((name,tuoi,score))
lst.sort()
for i in range(len(lst)):
    tupl=list(lst[i])
    tupl[1]=str(tupl[1])
    tupl[2] = str(tupl[2])
    lst[i]=tuple(tupl)
print(lst)