# 1. Problem: Write a Python function that copies the contents of array a to array b.
#    - Create an array b and copy all elements from array a into b.
#    - Key Concepts: Array manipulation, Copying elements.

def copy_array(a):

    # Setting 'b' with same length as 'a' 
    b = [None] * len(a)

    # copying elements of 'a' to 'b'
    for i in range(len(a)):
       b[i] = a[i]
    
    #Returning the Elements of B
    return b
    

a = [1, 2, 3, 4]
print(f'The elements in b are {copy_array(a)}')
