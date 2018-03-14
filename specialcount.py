import re
x = "asdfklsdf#$&^#@!"
new = re.sub('[\w]+' ,'', x)
