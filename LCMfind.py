def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
n1 = 64
n2 = 34
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("The L.C.M. of", n1,"and", n2,"is", lcm(n1, n2))
