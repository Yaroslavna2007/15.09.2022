import math

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
def distance(x1, y1, x2, y2):
    xp = x2-x1
    yp = y2-y1
    p = (xp**2)+(yp**2)
    return p
d = math.sqrt(p)
print(d)
# ?