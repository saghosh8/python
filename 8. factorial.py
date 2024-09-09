# Factorial Number

number=int(input('Enter the Number to find Factorial: '))
fact=1
i=1

while(i<=number):
    fact=fact*i
    i+=1
print(fact)