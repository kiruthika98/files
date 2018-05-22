
x1=int(input("Enter the x1 value:"))
print("Enter the Elements:")
a=[0]
sum=0
for x in range(x1):
	k=int(input())
	a.append(k)
for x in range(x1):
	sum=sum+a[x]
print(sum)

