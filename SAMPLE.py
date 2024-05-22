a=[]
n=int(input("enter length of the list"))
for i in n:
    element=int(input("enter the values to be sorted"))
    a.append(element)
print(a)
for j in range(0,n-1):
    for k in range(i+1,n):
        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
print(a)            