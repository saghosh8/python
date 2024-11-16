#Define a Function to check if a Number is Positive or Negative or Zero
def Positive_Negative_Number(number):
    #Check if the number is greater than zero
    if number > 0:
        print(f"{number} is a positive number.")
    #Check if the number is less than zero
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print(f"{number} is a Zero")

#Take User Input
number = int(input("Enter the Number:"))

#call the function
Positive_Negative_Number(number)