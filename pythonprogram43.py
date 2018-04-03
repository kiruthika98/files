a=input("\nEnter the string:")
b=int(input("\nEnter the number:"))
e=b
c=list(str(a))
d=len(c)
while e>0:
    print(c[d-b],end='')
    b=b-1
    e=e-1
