water_per_cup = int(200)
milk_per_cup = int(50)
coffee_beans_per_cup = int(15)

coffee_cups = int(input("Write how many cups of coffee you will need:" + '\n'))
print("""For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans
""".format(coffee_cups,
           coffee_cups * water_per_cup,
           coffee_cups * milk_per_cup,
           coffee_cups * coffee_beans_per_cup))
