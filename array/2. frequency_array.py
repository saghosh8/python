# 2. Write a program to find the frequency of each element in Array A


def find_frequency(A):
    frequency_dict = {}
    
    # Calculate frequency of each element
    for element in A:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    return frequency_dict

if __name__ == '__main__':
    # Define array A
    A = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    
    # Get the frequency of elements in A
    frequency = find_frequency(A)
    print(frequency)

    # Output the frequency of each element
    print("Element Frequency:")
    for element, count in frequency.items():
        print(f"{element}: {count}")
