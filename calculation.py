choice = input("""
Please select the type of operation you want to perform:
    + for addition
    - for subtraction
    * for multiplication
    / for division
Select the operator: 
""")
               
num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))

#Addition 
if choice == "+":
    print("{} + {} = ".format(num_1, num_2))
    print(num_1 + num_2)

#Subtraction
elif choice == "-":
    print("{} - {} = ".format(num_1, num_2))
    print(num_1 - num_2)

#Multiplication
elif choice == "*":
    print("{} * {} = ".format(num_1, num_2))
    print(num_1 * num_2)

#Division
elif choice == "/":
    print("{} / {} = ".format(num_1, num_2))
    print(num_1 / num_2)

else:
    print("Please, Enter a valid operator and try again.")