"""
1. User inputs the lower bound and upper bound of the range
2. The computer generates  a random integer between the range and store it in a variable for future references
3. For repetitive guessing, a while loop will be initialized
4. If the user guessed a number which is greater than a randomly selected number, the user gets an output "Try Again! You guessed too high"
5. Else If the user guessed a number which is smaller than the randomly selected number, the user gets an output
" Try again! You guessed too low"
6. And if the user guessed in a minimum number of guesses, the user gets a "Congragulations!" output
Else if the user didn't guess the integer in the minimum number of guesses. He/she will get "Better Luck Next Time!"
"""

# Import libraries
import random
import math

def select_difficulty():
    """
    Prompt the user to select a difficulty level.
    Returns either: "easy", "medium", "hard"
    """
    choices = {1: "easy", 2: "medium", 3: "hard"}
    while True:
        print("\nChoose difficulty:")
        print(" 1) Easy (+3 attempts)")
        print(" 2) Medium (default)")
        print(" 3) Hard (-2 attempts)\n")
        choice = int(input("Enter 1, 2 or 3: "))
        if choice in choices:
            return choices[choice]
        print("Invalid choice. Please select 1,2 or 3")

def get_difficulty_multiplier(level):
    if level == "easy":
        return 3
    elif level == "hard":
        return -2
    else:
        return 0
    
def calculate_max_tries(lower, upper, difficulty):
    """
    Calculate the maximum number of tries permitted 
    """
    range_size = upper - lower + 1
    base_tries = math.ceil(math.log2(range_size))
    offset = get_difficulty_multiplier(difficulty)
    max_tries = base_tries + offset
    return max_tries

def calculate_score(max_tries, attempts):
    if attempts > max_tries:
        return 0
    return max(10, (max_tries - attempts) * 10)

def play_game():
    while True:
        try:
            # Define the range
            lower = int(input("Enter the lower bound: "))
            upper = int(input("Enter the higher bound: "))
            if lower >= upper:
                print("Lower bound must be less than upper bound. Try again!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter valid integers.")
    
    # Select difficulty level
    difficulty = select_difficulty()

    # Generate target number
    target = random.randint(lower, upper) 

    # Calculate number of tries
    max_tries = calculate_max_tries(lower, upper, difficulty)
    print(f"\nI have selected a number between {lower} and {upper}.\nYou have {max_tries} attempts to guess the number.\n")

    attempts = 0 # count tries

    # Repetitive guessing loop
    while attempts < max_tries:
        try:
            guess = int(input(f"{attempts+1}: What is the number? "))
        except ValueError:
            print("That's not an integer. Try again.")
            continue

        attempts += 1
        if guess == target:
            score = calculate_score(max_tries, attempts)
            print(f"🏆 Congratulations! You guessed the number in {attempts} attempt(s). You get {score} points")
            return score
        elif guess > target:
            print("Try again! You guessed too high\n")
        elif guess < target:
            print("Try again! You guessed too low\n")
    else:
        print(f"Better luck next time! The number was {target}.")
        return 0

def main():
    print("\n⚔️  Welcome to Number Ninja ⚔️")
    print("Guess the secret number... or be defeated!\n")

    high_score = 0

    while True:
        current_score = play_game()
        if current_score > high_score:
            high_score = current_score
            print("🔥 New High Score!! 🔥")

        play_again = input("Do you want to play again? (y/n: )").lower()
        if play_again != 'y':
            print("Thank you for playing Number Ninja! We will be awaiting your next arrival soldier 👋")
            break

if __name__ == "__main__":
    main()