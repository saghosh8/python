# Check if the Number is Even or Odd

def OddEvenNumber (number):
    if (number%2==0):
        print(f"The {number} is a Even Number.")
    else:
        print(f"The {number} is Odd Number.")


number = int(input("Enter the Number: "))
OddEvenNumber(number)