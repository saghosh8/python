# Check if the Number exists in list

number = int(input("Enter the Number:"))
list = [10,20,30,40,50]

for i in list:
    if number == i:
        print('Found the number in list')
        break
else:
    print('Number Not in List')