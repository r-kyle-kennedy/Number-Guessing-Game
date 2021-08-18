import random

def start_game(high_score, high_score_player, last_number, play_again):
    if high_score_player:
        print(f"The current high score is {high_score}, held by {high_score_player}!") 
    else:
        print("Welcome to the Number Guessing Game!!!")

    current_player = input("What is your name?  ")
    current_number = random.randrange(1, 11)
    while current_number == last_number:
        current_number = random.randrange(1, 11)

    current_guess = input(f"{current_player}, guess a number between 1 and 10. Try to get the number in as few tries as you can to beat the high score!  ")

    #check if given a digit
    def coherce_current_guess(guess):
        try:
            return int(guess)
        except ValueError:
            return int(coherce_current_guess(input(f"{guess} is not a number, please input a digit between 1 and 10.  ")))

    current_guess = coherce_current_guess(current_guess)
    current_score = 1

    while current_guess != current_number:
        while current_guess < 1 or current_guess > 10:
            current_guess = coherce_current_guess(input(f"{current_guess} is not a digit between 1 and 10, please try again   "))
        if current_guess < current_number:
            new_guess = input(f"{current_guess} is too low, guess a higher number...  ")
            current_guess = coherce_current_guess(new_guess)
            current_score += 1
        else:
            new_guess = input(f"{current_guess} is too high, guess a lower number...  ")
            current_guess = coherce_current_guess(new_guess)
            current_score += 1

    print(f"{current_player}, you got it! {current_guess} was the correct number")
    print(f"Your score was: {current_score}")

    if current_score < high_score:
        high_score = current_score
        high_score_player = current_player
        print(f"Congratulations {current_player}! Your score of {current_score} is now the high score!")

    play_again = input("Would you like to play again??? (Y/N)   ").lower()
    return [high_score, high_score_player, current_number, play_again]

last_game = start_game(1000, "", 0, "y")

while last_game[3] == "y":
    last_game = start_game(last_game[0], last_game[1], last_game[2], last_game[3])

print("GAME OVER!")
