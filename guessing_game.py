def guessing_game():
    target=15
    while True:
        guess = int(input("Enter your guess: "))
        if guess == target:
            return "Congratulations! You guessed it!"
        elif guess < target:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")