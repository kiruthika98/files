
val=int(input("Enter Value"))
if val == 0:print(1)
if val & (val - 1) == 0:print(val)
while val & (val - 1) > 0:val &= (val - 1)
print(val << 1)

