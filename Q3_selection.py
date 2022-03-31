# User input
month = input("Enter a number for months (1-12): ")
num = int(month)

while True:
    if 1 <= num <= 2:
        print("Wonderful Summer")
        break
    elif num == 12:
        print("Wonderful Summer")
        break
    elif 3 <= num <= 5:
        print("Colourful Autumn")
        break
    elif 6 <= num <= 8:
        print("Freezing cold Winter")
        break
    elif 9 <= num <= 11:
        print("Very warm Spring")
        break
    else:
        print(num, "is an invalid season number")
    break
