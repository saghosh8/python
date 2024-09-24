# Write a Program to Print the Factors of a Number

N = int(input('Enter the Number: '))

for i in range(1, N+1):
    if(N % i == 0):
        print(i)
        continue