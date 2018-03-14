import re

def anti_wovel(s):
    result = re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE)
    return result



