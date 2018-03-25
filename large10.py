numList = []
for i in range(10):
    numList.append(random.randrange(0,11))
maxNum = -1
for i in numList:
    if i > maxNum:
        maxNum = i
print(maxNum)
