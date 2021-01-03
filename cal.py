import math
print(      )
pi=math.pi
x=pi/4
print()
print()
print('tringonometric table for sin,cos,and tan for 0 to 2pie in multiples of pie/4')
print()

for i in range(5):
    angle=x*i
    print('sin','(',i,'*pi/4','',')','',round(math.sin(angle),3))
print('   ')
for i in range(5):
    angle=x*i
    print('cos','(',i,'*pi/4',')','',round(math.cos(angle),3))
print('    ')
for i in range(5):
    angle=x*i
    print('tan','(',i,'*pi/4',')','',round(math.tan(angle),3))
print('   ')