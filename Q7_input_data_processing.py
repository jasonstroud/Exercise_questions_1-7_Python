# User input - receive number of stocks
while True:
    ans = int(input("How many stocks?: "))
    if ans > 0:
        break
    elif ans <= 0:
        print("Please enter a number higher than 0\n")
        continue

# User input - receive price for each stock
pricelist = []

for i in range(0, ans):
    print("Enter price for stock #", i + 1)
    price = input()
    # price = [input("Enter price for stock #", )]
    pricelist.append(price)
    if i == ans:
        break

# Convert from string list to float list
for a in range(0, len(pricelist)):
    pricelist[a] = float(pricelist[a])


# getAve function
def get_Ave(list):
    if len(list) == 0:
        print("List is empty")
    average = sum(list) / len(list)
    return average

# getMax function
def get_Max(list):
    if len(list) == 0:
        print("List is empty")
    maxnum = None
    for x in list:
        if maxnum is None or x > maxnum:
            maxnum = x
    return maxnum


# getRange function
def get_Range(list):
    if len(list) == 0:
        print("List is empty")
    count = 0
    for x in list:
        if 1.5 <= x <= 5.5:
            count = count + 1
    return count

# calculate
priceformat1 = "{:.2f}".format(get_Ave(pricelist))
priceformat2 = "{:.2f}".format(get_Max(pricelist))

print("Average price: $", priceformat1)
print("Maximum price: $", priceformat2)
print("Stocks priced between $1.5 and $5.5: ", get_Range(pricelist), " \n")

# Query stock number for price
while True:
    print("Enter stock number 1 -", ans)
    item = int(input())
    if 1 <= item <= ans:
        print("Price for stock", item, "is $", pricelist[item -1])
        break
    else:
        print("Stock doesn't exist. Enter again. \n")
