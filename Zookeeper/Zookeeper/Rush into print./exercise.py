natural_number = int(input())
counter = 1
sum_natural_numbers = 0

while counter <= natural_number:
    sum_natural_numbers += counter
    counter += 1

print(sum_natural_numbers)