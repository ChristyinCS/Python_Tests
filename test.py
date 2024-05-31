miles = int(input("How far would you like to travel in miles?"))

if miles < 3:
    print("You should walk")
elif miles <= 300:
    print("You should take a car")
else:
    print("Take a flight")

print("Have a nice day. Bye Bye")
