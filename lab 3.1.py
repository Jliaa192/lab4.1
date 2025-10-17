x = input( ).split(' ')
print(x)
a=0
for i in x:
    if int(i) % 2 != 0:
         a += int(i)
print("a", a)
