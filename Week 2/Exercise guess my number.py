print("Please think of a number between 0 and 100!")

ans = ""
low = 0
high = 100
while ans != 'c':
    guess = (low + high) // 2
    print("Is your secret number " + str(guess) + "?")
    while True:
        userIn = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                       "Enter 'c' to indicate I guessed correctly.")
        if userIn in "clh":
            break
        else:
            print("Sorry, I did not understand your input.")
            print("Is your secret number " + str(guess) + "?")

    if userIn == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    elif userIn == 'h':
        high = guess
    else:
        low = guess
