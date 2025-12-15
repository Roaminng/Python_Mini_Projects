import random

def start_game():
    
    print("-------------------------------------------------")
    print("   Welcome to the Number Guessing Game!   ")
    print("-------------------------------------------------")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?\n")

    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 10 
    while True:
        try:
          
            user_guess = int(input(f"Enter your guess (Attempt {attempts + 1}): "))
            attempts += 1

            if user_guess < secret_number:
                print("Too Low! Try again.")
            elif user_guess > secret_number:
                print("Too High! Try again.")
            else:
                print(f"\n CONGRATULATIONS! You guessed the number {secret_number}!")
                print(f"It took you {attempts} attempts to win.")
                break

            if attempts >= max_attempts:
                print(f"\n Game Over! You ran out of attempts.")
                print(f"The number was: {secret_number}")
                break

        except ValueError:
            print(" Invalid input! Please enter a valid number.")

    print("\n-------------------------------------------------")
    print("Thank you for playing!")
    print("-------------------------------------------------")

if __name__ == "__main__":
    start_game()