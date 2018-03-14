a='IGADKYFHARGNYDAA'
b='KGADKYFHARGNYEAA'

u=zip(a,b)
d=dict(u)

x=[]
for i,j in d.items(): 
    if i==j:
        x.append('*') 
    else: 
        x.append(j)

print x

