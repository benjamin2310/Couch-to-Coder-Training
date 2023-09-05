# main task
# pin = 1365
# balance = 50000
# input_pin = int(input("Please enter your PIN: "))

# if input_pin == pin:
#     print(balance)
# else:
#     print("Please enter the correct PIN!")

# extensions

pin = 1234
balance = 20000
number_of_times = 3

input_pin = int(input("Please enter your PIN: "))

if (input_pin == pin):
    user_choice = input("Would you like to make deposit or withdraw cash?")
    if user_choice == "withdraw":
        amount = int(input("Please enter the chosen amount to withdraw: "))
        balance -= amount
        print("Your new balance after withdrawal is = ", str(balance))
    if user_choice == "deposit":
        amount = int(input("Please enter a chosen amount to deposit"))
        balance += amount
        print("Your new balance after deposit is = ", str(balance))
else:
    print("Incorrect PIN! Please try again!")
