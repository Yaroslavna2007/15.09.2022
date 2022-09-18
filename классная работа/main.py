s = int(input())
def factorial(s):
    i = 1
    for d in range(1,s+1):
        i = i*d
    print(i)
    return i
factorial(s)