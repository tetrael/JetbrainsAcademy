class CoffeeMachine:
    blank = {'water': 0, 'milk': 0, 'beans': 0, 'money': 0}
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'money': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'money': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'money': 6}
    coffeeTypes = (blank, espresso, latte, cappuccino)

    def __init__(self, water=None, milk=None, beans=None, cups=None, money=None):
        self.water = water if water is not None else 400
        self.milk = milk if milk is not None else 540
        self.beans = beans if beans is not None else 120
        self.cups = cups if cups is not None else 9
        self.money = money if money is not None else 550

    def update_state(self, coffee_type):
        self.water -= self.coffeeTypes[coffee_type]['water']
        self.milk -= self.coffeeTypes[coffee_type]['milk']
        self.beans -= self.coffeeTypes[coffee_type]['beans']
        self.money += self.coffeeTypes[coffee_type]['money']
        self.cups -= 1

    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        print("I gave you {}".format(self.money))
        self.money = 0

    def print_state(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("{} of money".format(self.money))

    def choose_action(self, action):
        if action == "buy":
            coffee_type = int(input("What do want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:" + '\n'))
            self.update_state(coffee_type)
        elif action == "fill":
            water = int(input("Write how many ml of water do you want to add:" + '\n'))
            milk = int(input("Write how many ml of milk do you want to add:" + '\n'))
            beans = int(input("Write how many grams of coffee beans do you want to add:" + '\n'))
            cups = int(input("Write how many disposable cups of coffee do you want to add:" + '\n'))
            self.fill(water, milk, beans, cups)
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.print_state()

    def start(self):
        action = str(input("Write action (buy, fill, take, remaining, exit):" + '\n'))
        while action != "exit":
            action = str(input("Write action (buy, fill, take, remaining, exit):" + '\n'))
            self.choose_action(action)


coffeeMachine = CoffeeMachine()
coffeeMachine.start()
