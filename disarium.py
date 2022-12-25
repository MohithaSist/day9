a=int(input())
c=str(a)
l1=[]
l2=[]
l3=[]
k=len(c)
for i in str(a):
    l1.append(int(i))
for j in range(1,k+1):
    l2.append(j)
for m in range(0,k):
    d=l1[m]**l2[m]
    l3.append(d)
n=sum(l3)
if n==a:
    print("True")
else:
    print("False")
            
        








        
