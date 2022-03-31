import random

def generateRandom(upper):

    r = random.randint(1, upper)
    return r

def main():
    run = True
    num1 = generateRandom(10)
    num2 = generateRandom(10)
    result = num1 * num2

    while run:
        ans = input("What is " + str(num1) + " x " + str(num2) + "? ")

        if ans.isdigit():
            if int(ans) == result:
                print("Correct!")
                run = False
            else:
                print("Incorrect! Try again")
        else:
            print("Answer must be a positive number, try again")

# Global vars
times = 10
for x in range(times):
    main()