import math

water = int(input("Write how many ml of water the coffee machine has:" + '\n'))
milk = int(input("Write how many ml of milk the coffee machine has:" + '\n'))
coffee_beans = int(input("Write how many grams of coffee the coffee machine has:" + '\n'))
requested_cups = int(input("Write how many cups of coffee you will need:" + '\n'))

water_portions = math.floor(water / 200)
milk_portions = math.floor(milk / 50)
beans_portions = math.floor(coffee_beans / 15)

# print(water_portions)
# print(milk_portions)
# print(beans_portions)

max_portions = min(list([water_portions, milk_portions, beans_portions]))

# print(max_portions)

if requested_cups == max_portions:
    print("Yes, I can make that amount of coffee")
elif requested_cups < max_portions:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(max_portions - requested_cups))
else:
    print("No, I can make only {} cups of coffee".format(max_portions))
