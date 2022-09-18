m = -1234
k = 1
x = int(input())
while x!=0:
    if x>m:
        m=x
    elif x==m:
        k = k+1
    x = int(input())
print(k)