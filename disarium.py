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
            
        
'''a=int(input())
c=str(a)
l1=[]
st=''
count=0
k=len(c)
for i in str(a):
    
for j in range(1,k+1):
        
        if j==1:
            m=pow(int(i),j) 
            st=''+str(m)
            print(st)'''


'''l1=[1,2,3,4]
l2=[1,2,3,4]
l3=[]
for i in range(0,len(l1)):
    m=l1[i]**l2[i]
    print(m)'''

            















        
