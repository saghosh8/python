# Sum of Natural Numbers:

Sum = 0
N=int(input('Enter the Number: '))

for i in range(1, N+1):
    Sum += i                    #Sum = Sum + i
print(f'Sum Of First {N} Natural Number is: {Sum}')