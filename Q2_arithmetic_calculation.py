# User input
height = input("Enter a height: ")
string1 = height
myfloat1 = float(string1)

width = input("Enter a width: ")
string2 = width
myfloat2 = float(string2)

# calculations
area = myfloat1*myfloat2
perimeter = (myfloat1 + myfloat2)*2

# table header
myfmt1 = "{:<10}{:<10}{:<10}{:<10}"
print(myfmt1.format("Height", "Width", "Area", "Perimeter"))

spaceline = str.format("%40s" % " ")
dashline = spaceline.replace(" ", "-")
print(dashline)

# print results
myfmt2 = "{:<10.2f}{:<10.2f}{:<10.2f}{:<10.2f}"
print(myfmt2.format(myfloat1, myfloat2, area, perimeter))