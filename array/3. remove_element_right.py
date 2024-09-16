# 3. Write a program to remove the array element present immidiately to the right of the element entered by the user

def remove_element(A, element):
    if element in A:
        index = A.index(element)  # Find the index of the element
        if index < len(A) - 1:    # Ensure the element has a right neighbor
            A.pop(index + 1)      # Remove the element to the right
    return A

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    element = 2
    print(remove_element(A, element))

