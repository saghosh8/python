arr = [1, 1, 2]

result = []
for num in arr:
    if num not in result:
        result.append(num)
print(result)
