# Write a program to print number till N, 
# which are not divisible by 3, 6 or 9

N=10

for i in range(1, N+1):
    if (i % 3 != 0 and i % 6 != 0 and i % 9 != 0):
        print(i)
        continue
    