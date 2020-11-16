acceptable_chars = ('X', 'O', '_')
symbols = list()

for x in str(input("Enter cells: ")):
    symbols.append(x if x in acceptable_chars else '')

print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*symbols))
