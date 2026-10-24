import numpy as np

a=b=c=d=e=f=0

for i in range(1000):
    x=np.random.randint(1,7)
    if x==1:
        a+=1
    if x==2:
        b+=1
    if x==3:
        c+=1
    if x==4:
        d+=1
    if x==5:
        e+=1
    if x==6:
        f+=1

print(a,b,c,d,e,f)
