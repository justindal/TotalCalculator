print('Welcome to the TotalCalculator!')
itemsAmount = input('How many items will you have?\n')
itemsAmount = float(itemsAmount)
counter = 0
totalBT = 0
while True:
    counter = counter + 1
    cost = input('How much is your item?\n')
    cost = float(cost)
    totalBT = totalBT + cost
    print('Current cost before tax: ', totalBT, '\n')
    if itemsAmount == counter:
        break
tax = input("What is the tax percentage?")
tax = float(tax)
tax = tax / 100
tax = totalBT * tax
total = totalBT + tax
print('Your total with Tax is $', total)
