str = "count a character occurance"

List = list(str)
print (List)
Uniq = set(List)
print (Uniq)

for key in Uniq:
    print (key, str.count(key))

