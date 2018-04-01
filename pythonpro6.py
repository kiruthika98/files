x=input("enter the number:")
array=[]
for y in range(0,x):
    array.append(raw_input())
array.sort(key=len)
print array
