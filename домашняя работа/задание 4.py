x = input().split()
k = 0
for s in range(0,len(x)-1):
    x[s] = int(x[s])
    x[s + 1] = int(x[s+1])
    if x[s] != x[s+1]:
        k = k+1
print(k+1)