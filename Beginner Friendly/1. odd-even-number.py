#Define the Function to check if a number is even or odd
def OddEvenNumber(number):
    #Check if the number is divisible by 2
    if number % 2 == 0:
        print(f"{number} is an Even Number.")
    else:
        print(f"{number} is an Odd Number.")

# Take a User Input
number = int(input("Enter the Number: "))
#Call The function
OddEvenNumber(number)