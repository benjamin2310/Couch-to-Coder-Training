pin = 1365
balance = 50000
number_of_times

input_pin = int(input("Please enter your PIN: "))
while (number_of_times > 0):
    if (not input_pin.isdigit()):
        print("Inavlid input, please enter a valid PIN number!")
        break
    if (pin == int(input_pin)):
        print("Your balance is " + str(balance))
        break
    else:
        number_of_times -= 1
        # guard clause
        if (number_of_times == 0):
            break
        input_pin = input("Incorrect PIN! Please try again!")
# if input_pin == pin:
#     print(balance)
# else:
#     print("Please enter the correct PIN!")
