# Receive 2 lines of input
firstline = input("Enter 1st line: ")
secondline = input("Enter 2nd line: ")

# Split and convert from string to float
stringlist1 = firstline.split(",")
for i in range(0, len(stringlist1)):
    stringlist1[i] = float(stringlist1[i])

stringlist2 = secondline.split(",")
for x in range(0, len(stringlist2)):
    stringlist2[x] = float(stringlist2[x])

# Compare values and print overlapping
count = 0
for d in stringlist1:
    for s in stringlist2:
        if d == s:
            count = count + 1
print("Number of overlapping values: ",  count)
