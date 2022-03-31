# START
while True:
    letter = input("Enter a card letter (j/q/k/a): ")
    if letter.casefold().startswith("j"):
        print("It's a Jack!")
        break
    elif letter.casefold().startswith("q"):
        print("It's a Queen!")
        break
    elif letter.casefold().startswith("k"):
        print("It's a King!")
        break
    elif letter.casefold().startswith('a'):
        print("It's an Ace!")
        break
    print("That entry is invalid. Try again")
    continue
