radius = 42
p=3.1415926
s=round(p*radius**2,4)
print(s)
point = (23, 34)
x=point[0]
y=point[1]
h1=(x**2+y**2)**0.5
if h1<radius :
    print('True')
else:
    print('False')
point_2 = (30, 30)
x=point_2[0]
y=point_2[1]
h1=(x**2+y**2)**0.5
if h1<radius :
    print('True')
else:
    print('False')

# Пример вывода на консоль:
#
# 77777.7777
# False
# False