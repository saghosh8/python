# Fibonacci Series:

a = 0
b = 1
Sum=0
N = int(input('Enter the Number: '))

print(a, end=' ')
print(b, end=' ')

for i in range(3, N+1):
    Sum = a+b
    print(Sum, end=' ')
    a = b
    b = Sum
    continue
