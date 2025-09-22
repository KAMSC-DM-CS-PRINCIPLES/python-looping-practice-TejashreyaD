def guessing_game():
    target=15
    while True:
        guess = int(input("Enter your guess: "))
        if guess == target:
            return "Congratulations! You guessed it!"
        elif guess < target:
            return" Too low! Try again."
        else:
            return"Too high! Try again."