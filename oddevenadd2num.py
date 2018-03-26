num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
if (sum % 2) == 0:
   print("{0} is Even".format(sum))
else:
   print("{0} is Odd".format(sum))
