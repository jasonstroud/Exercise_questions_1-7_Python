import random

secretnum = random.randrange(1, 11)
print(secretnum)

# User input and split
guess = input("Enter comma-separated numbers to guess my secret number (1 - 10): ")
guess2 = guess.split(",")
for i in range(0, len(guess2)):
    guess2[i] = int(guess2[i])

# Loop through list and check for match
exist = guess2.count(secretnum)

for x in range(0, len(guess2)):
    if guess2[x] == secretnum:
        print("My secret number is ", secretnum)
        print("Congratulations you won!")
        print("Attempt number", x + 1, "in your list is my secret number")
        break
    elif exist == 0:
        print("My secret number is", secretnum)
        print("You lost!")
        break
