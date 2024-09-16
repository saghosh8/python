# 1. Write a program to copy the elements of array from A to B

def copyArray(A):
    B = []
    for i in A:
        B.append(i)
    return B

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = copyArray(A)

    print(f'This is the Original Array A: {A}')
    print(f'This is the Copied Array B: {B}')