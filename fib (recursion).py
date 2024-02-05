n=int(input("enter a number"))

def fib(i):
    if i<=1:
        return i
    else:
        return fib(i-1)+fib(i-2)

for i in range (n):
    print(fib(i),end=" ")
