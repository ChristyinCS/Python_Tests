initial_pin = "3467"

pin_count = 0

while pin_count < 3:
    user_pin = input("Enter your pin: ")

    if len(user_pin) == 4 or len(user_pin) == 6:
        if initial_pin == user_pin:
            print("Here's your money.")
            break

        else:
            print("Wrong pin! Please try again.")
        
    else:
        print("Pin should be 5 or 6 digits.")
    pin_count += 1

print("Good Bye!")
    