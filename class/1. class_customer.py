# 1. A Class Customer contains the following details: customer name, customer ID, customer account number. 
# Write a program  that initialize the data members and displays them.

class Customer:

    def __init__(self, name, id, actno):
        self.customerName = name
        self.customerID = id
        self.customerAccNo = actno

    def display(self):
        print('Customer Name: ', self.customerName)
        print('Customer ID:', self.customerID)
        print('Customer Account No:', self.customerAccNo)

name = input('Enter the Name: ')
id = input('Enter the ID: ')
actno = input('Enter the Account No: ')
customer_details = Customer(name, id, actno)
customer_details.display()