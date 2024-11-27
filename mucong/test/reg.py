import re

num = '1.22.'
# print(isinstance(num,float))


n = re.match(r'(-?[0-9]+\.[0-9]*$)|(-?[0-9]+$)', num)
# print(r'\n')
# print(n.span()[1] == len(num))
print(n)
# print(float(num))
# print(n.group())

