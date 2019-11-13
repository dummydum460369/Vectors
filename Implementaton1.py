from Vectors2d import *

f1 = Vector2d(x=5.6, y=6.2)
f2 = Vector2d(x=1, y=1)

print(f1.sum(x=7).math_form(), '+', f2.math_form())
print('='+f1.resultant(f2).math_form())
