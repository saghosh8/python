# 4. Write a program to find the max frequency of the element in Array A and then delete it


def max_freq(A):
    hash_freq = {}
    for element in A:
        if element in hash_freq:
            hash_freq[element] += 1
        else:
            hash_freq[element] = 1
    return hash_freq

def remove_max_freq_element(A):
    # Get the frequency of each element
    frequency = max_freq(A)
    
    # Find the element with the highest frequency
    max_freq_element = max(frequency, key=frequency.get)
    
    # Remove all occurrences of the element with the highest frequency
    A = [element for element in A if element != max_freq_element]
    
    return A, max_freq_element

if __name__ == '__main__':
    A = [1, 2, 2, 12, 2, 12, 121]

    new_array, removed_element = remove_max_freq_element(A)

    print(f'Element with max frequency removed: {removed_element}')
    print(f'Array after removal: {new_array}')
