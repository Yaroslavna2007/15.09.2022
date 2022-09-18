f1 = 1
f2 = 1
fs = 0
n = int(input())
for s in range (2,n):
    fs = f1+f2
    f1 = f2
    f2 = fs
print(fs)