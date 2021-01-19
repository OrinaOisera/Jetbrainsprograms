deposit = "DEPOSIT"
withdraw = "WITHDRAW"
display = "DISPLAY"

# card_pin and card_balance are read from the database
card_pin = 3451
card_balance = 100

def deposit_money(amount, card_balance):
    card_balance += amount
    print(card_balance)
    return card_balance


def withdraw_money(amount, card_balance):
    card_balance -= amount
    return card_balance

def log_transactions(action, amount, card_balance):
    if action in (deposit, withdraw):
        print(action + "$" + amount)
        print("Your current card balance is:" + card_balance)

def move_money(action, amount, card_balance) :
  if action == deposit:
    return deposit_money(amount, card_balance)
  elif action == withdraw:
      return withdraw_money(amount, card_balance)
  elif action == display:
      return card_balance

def get_amount_of_money(action):
    if action == display:
        return 0.0
    amount = input("Enter the sum of money to " + action + ": ")
    return float(amount)



def make_transaction(action, card_balance):
    money = get_amount_of_money(action)
    card_balance = move_money(action, money, card_balance)
    log_transactions(action, money, card_balance)

card_number = input("Enter card number: ")
input_pin = int(input("Enter PIN: "))

# card_pin and card_balance are read from the database

if card_pin == input_pin:
    action = input("Enter desired action: ")
    make_transaction(action, card_balance)
else:
    print("Incorrect pin!")




