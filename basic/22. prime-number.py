# check if the Number is prime

# Input number
N = int(input("Enter a number: "))

fact = []
for i in range(1, N+1):
    if N % i == 0:
        fact.append(i)

if len(fact) == 2:
    print('This is a Prime Number')
else:
    print('This is NOT a Prime Number')
