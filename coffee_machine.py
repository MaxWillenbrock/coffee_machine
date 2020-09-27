# stage 5/6

# variables

# Storage information
water = 400  # ml
milk = 540  # ml
coffee_beans = 120  # g
money = 550  # $
disposable_cups = 9  # ps

# ingredients needs per one cup
# for espresso
espresso_water_one_cup = 250  # ml
espresso_milk_one_cup = 0  # ml
espresso_beans_one_cup = 16  # gram
espresso_money_one_cup = 4  # $

# for latte
latte_water_one_cup = 350  # ml
latte_milk_one_cup = 75  # ml
latte_beans_one_cup = 20  # gram
latte_money_one_cup = 7  # $

# for cappuccino
cappuccino_water_one_cup = 200  # ml
cappuccino_milk_one_cup = 100  # ml
cappuccino_beans_one_cup = 12  # gram
cappuccino_money_one_cup = 6  # $

action = ""

# functions


def start():
    global action
    action = input("Write action (buy, fill, take, remaining, exit): ")
    choose_action(action)


def choose_action(x):
    if x == "buy":
        return buying()
    if x == "fill":
        return filling()
    if x == "take":
        return taking()
    if x == "remaining":
        return remaining()
    if x == "exit":
        return exiting()


def print_storage():
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee_beans) + " of coffee beans")
    print(str(disposable_cups) + " of disposable cups")
    print(str(money) + " of money")
    start()


def buying():
    global water
    global milk
    global coffee_beans
    global money
    global disposable_cups
    x = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if x == "1":
        check_espresso()
        water -= espresso_water_one_cup
        milk -= espresso_milk_one_cup
        coffee_beans -= espresso_beans_one_cup
        money += espresso_money_one_cup
        disposable_cups -= 1
        print("I have enough resources, making you a coffee!")
    elif x == "2":
        check_latte()
        water -= latte_water_one_cup
        milk -= latte_milk_one_cup
        coffee_beans -= latte_beans_one_cup
        money += latte_money_one_cup
        disposable_cups -= 1
        print("I have enough resources, making you a coffee!")
    elif x == "3":
        check_cappuccino()
        water -= cappuccino_water_one_cup
        milk -= cappuccino_milk_one_cup
        coffee_beans -= cappuccino_beans_one_cup
        money += cappuccino_money_one_cup
        disposable_cups -= 1
        print("I have enough resources, making you a coffee!")
    elif x == 'back':
        start()
    start()


def filling():
    global water
    global milk
    global coffee_beans
    global money
    global disposable_cups
    watter_add = int(input("Write how many ml of water do you want to add: "))
    milk_add = int(input("Write how many ml of milk do you want to add: "))
    coffee_beans_add = int(input("Write how many grams of coffee beans do you want to add: "))
    disposable_cups_add = int(input("Write how many disposable caps of coffee do you want to add: "))
    water += watter_add
    milk += milk_add
    coffee_beans += coffee_beans_add
    disposable_cups += disposable_cups_add
    start()


def taking():
    global money
    print("I gave you $" + str(money))
    money -= money
    start()


def remaining():
    print_storage()
    start()


def exiting():
    exit()


def check_espresso():
    if water - espresso_water_one_cup < 0:
        print("Sorry, not enough water!")
        start()
    if milk - espresso_milk_one_cup < 0:
        print("Sorry, not enough milk!")
        start()
    if coffee_beans - espresso_beans_one_cup < 0:
        print("Sorry, not enough coffee beans!")
        start()
    if disposable_cups - 1 < 0:
        print("Sorry, not enough cups!")
        start()


def check_latte():
    if water - latte_water_one_cup < 0:
        print("Sorry, not enough water!")
        start()
    if milk - latte_milk_one_cup < 0:
        print("Sorry, not enough milk!")
        start()
    if coffee_beans - latte_beans_one_cup < 0:
        print("Sorry, not enough coffee beans!")
        start()
    if disposable_cups - 1 < 0:
        print("Sorry, not enough cups!")
        start()


def check_cappuccino():
    if water - cappuccino_water_one_cup < 0:
        print("Sorry, not enough water!")
        start()
    if milk - cappuccino_milk_one_cup < 0:
        print("Sorry, not enough milk!")
        start()
    if coffee_beans - cappuccino_beans_one_cup < 0:
        print("Sorry, not enough coffee beans!")
        start()
    if disposable_cups - 1 < 0:
        print("Sorry, not enough cups!")
        start()


# main body of program

start()


# action = input("Write action (buy, fill, take, remaining, exit): ")
# choose_action(action)
