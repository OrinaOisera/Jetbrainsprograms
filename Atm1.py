# operation

deposit = "DEPOSIT"
withdraw = "WITHDRAW"
display = "DISPLAY"
card_pin = 3451

# read the data
card_number = input("Enter the card number: ")
input_pin = int(input("Enter card pin: "))

# card_pin and card_balance are read from the database
card_pin = 3451
card_balance = 100

if card_pin != input_pin:
    print("The pin is incorrect")
# check if the pin is correct
else:
    action = input("Enter desired action")
    if action == deposit:
        money = float(input("Enter the sum of money to DEPOSIT:"))
        card_balance += money
        print("You have deposited: $", money)
        print("Your card balance :", card_balance)
    elif action == withdraw:
        money = float(input("Enter the sum of money to withdraw:"))
        card_balance -= money
        print("You have withdrawn $", money)
        print("Your card balance :", card_balance)
    elif action == display:
        print("Current balance:", card_balance)



