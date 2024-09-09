# 3. Write a program to count the number of even and odd numbers in a list.

my_list = [10, 25, 30, 35, 50]
count_even = 0
count_odd = 0

for i in my_list:
    if (i % 2 == 0):
        count_even +=1
    else:
        count_odd +=1
        
print(f'Total Number of Even number are: {count_even}')
print(f'Total Number of Odd number are: {count_odd}')