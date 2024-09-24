# Check the Number is Positive Or Negative

def Positive_Negative_Number(number):
    if number>0:
        print(f"{number} is a Posive Number.")
    elif number<0:
        print(f"{number} is a Negative Number.")
    else:
        print(f"The Number : {number} is Zero.")

number = int(input("Enter the Number: "))
Positive_Negative_Number(number)

