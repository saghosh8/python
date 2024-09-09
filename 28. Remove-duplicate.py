# 5. Write a program to remove duplicates from a list.

my_list = [10, 25, 30, 35, 50, 24, 36, 89, 25, 10, 35]


# Using For Loop
unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

# Using Set
# unique_list = list(set(my_list))
# print(unique_list)