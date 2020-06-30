import sys


class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.main()
        self.state = ''
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def communicate(self):
        if self.main():
            self.state = "choosing an action"
        elif self.buy_func():
            self.state = "choosing a coffee type"
        elif self.fill_func():
            self.state = "filling a coffee machine"
        elif self.remaining_func():
            self.state = "remaining"
        elif self.take_func():
            self.state = "taking money from coffee machine"


    def not_enough_resources(self):
        if self.water < 400:
            print("Sorry not enough water!")
        elif self.milk < 540:
            print("Sorry not enough water!")
        elif self.beans < 120:
            print("Sorry not enough beans!")
        elif self.cups < 9:
            print("Sorry not enough cups!")
        self.main()
    def buy_func(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        buy = input()
        if buy == '1':  # espresso
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
                self.main()
            else:
                self.not_enough_resources()
        elif buy == '2':  # latte
            if self.water >= 350 and self.beans >= 20 and self.milk >= 75 and self.cups >= 1:
                print("I have enough resources, making you coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
                self.main()
            else:
                self.not_enough_resources()
        elif buy == '3':  # cappuccino
            if self.water >= 200 and self.beans >= 12 and self.milk >= 100 and self.cups >= 1:
                print("I have enough resources, making you coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
                self.main()
            else:
                self.not_enough_resources()
        elif buy == 'back':
            self.main()
    def fill_func(self):
        print("Write how many ml of water do you want to add:")
        fill_water = input( )
        self.water += int(fill_water)
        print("Write how many ml of milk do you want to add:")
        fill_milk = input( )
        self.milk += int(fill_milk)
        print("Write how many grams of coffee beans do you want to add:")
        fill_beans = input( )
        self.beans += int(fill_beans)
        print("Write how many disposable cups do you want to add:")
        fill_cups = input( )
        self.cups += int(fill_cups)
        self.main()
    def take_func(self):
        print("I gave you " + "$" + str(self.money))
        self.money = 0
        self.main()
    def remaining_func(self):
        print("The coffee machine has:", str(self.water) + " of water", str(self.milk) + " of milk", str(self.beans) + " of coffee beans",
              str(self.cups) + " of disposable cups", sep="\n")
        print("$" + str(self.money) + " of money")
        self.main()
    def main(self):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        while True:
            if action == 'exit':
                sys.exit()
            elif action == 'buy':
                self.buy_func()
            elif action == 'fill':
                self.fill_func()
            elif action == 'take':
                self.take_func()
            elif action == 'remaining':
                self.remaining_func()


# coffee = CoffeeMachine("")
user = CoffeeMachine()