import re    
s = "hello       world  loL"
tokens = re.findall('\s+', s)

for i in range(0, len(tokens)) :
    print(len(tokens[i]))
