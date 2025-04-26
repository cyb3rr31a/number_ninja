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

print("\n⚔️  Welcome to Number Ninja ⚔️")
print("Guess the secret number... or be defeated!\n")

def guess_the_number():
    while True:
        try:
            # Define the range
            lower = int(input("Enter the lower bound of the range: "))
            upper = int(input("Enter the higher bound of the range: "))
            if lower >= upper:
                print("Lower bound must be less than upper bound. Try again!")
                continue
            break
        except ValueError:
            print("Please enter valid integers.")
    
    # Generate target number
    target = random.randint(lower, upper) 

    # Maximum number of tries
    range_size = upper - lower + 1
    max_tries = math.ceil(math.log2(range_size))
    print(f"I have selcted a number between {lower} and {upper}.\nYou have {max_tries} attempts to guess the number.")

    attempts = 0 # count tries

    # Repetitive guessing loop
    while attempts < max_tries:
        try:
            guess = int(input(f"{attempts+1}: What is the number? "))
        except ValueError:
            print("That's not an integer. Try again.")
            continue

        attempts += 1
        if guess > target:
            print("Try again! You guessed too high\n")
        elif guess < target:
            print("Try again! You guessed too low\n")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
            break
    else:
        print(f"Better luck next time! The number was {target}.")

if __name__ == "__main__":
    guess_the_number()