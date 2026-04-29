#Code by Logan Bauch


import random
#import statement for random module generater, so I can generate the random nums



# Difficulity
#all num ranges have different Difficulity

def play_game(difficulty):

    
    #a dict that stores the settings for each level 
    #key = diff name 
    #value = another dict that stores the max number the secret can be
    #attempts = how many guess the player actually gets

    levels = {
        "easy":   {"range": 50,  "attempts": 10},
        "medium": {"range": 100, "attempts": 7},
        "hard":   {"range": 200, "attempts": 5},
    }

    settings = levels[difficulty]
    max_num = settings["range"] # max secret num
    max_attempts = settings["attempts"] # max guesses

    #create random num 
    secret = random.randint(1, max_num)
    attempts = 0

    print(f"\nI picked a number between 1 and {max_num}. Try to guess it.")
    print(f"You have {max_attempts} guesses.\n")

    while attempts < max_attempts:

        # Get user input
        valid_guess = False #start with guess not being correct
        guess = None #placeholder so guess var exists before try 

        try:
            guess = int(input(f"Guess {attempts + 1}/{max_attempts} — Enter your guess: "))
            if guess >= 1 and guess <= max_num: #check if the number is inside the range
                valid_guess = True
            else:
                print(f"  That's out of range. Pick a number between 1 and {max_num}.\n")
        except ValueError:
            #error if the input is not a whole number
            print("  That's not a valid number. Try again.\n")

        if valid_guess:
            attempts += 1 #counts as attempt 

            #compare guess to secret 
            if guess == secret:
                print(f"\n  {secret} was correct!") #if correct prints correct statement
                print(f"  You got it in {attempts} attempts!\n")
                return True
            elif guess > secret:
                #guess above secret so tells user to go lower
                print(f"  Too high, guess lower.\n")
            else:
                #guess was to low, so tells user to go higher 
                print(f"  Too low, guess higher.\n")

    print(f"\n  Out of attempts, the secret was {secret}.\n")
    return False




def main():


    print("    Number Guessing Game    ")

    playing = True

    while playing:
        # Choose difficulty
        print("Pick a difficulty:")
        print("  1. Easy   (1–50,  10 attempts)")
        print("  2. Medium (1–100,  7 attempts)")
        print("  3. Hard   (1–200,  5 attempts)")

        choice = input("\nEnter 1, 2, or 3: ").strip() #read players choice and gets rid of extra spaces (strip)
        difficulty_map = {"1": "easy", "2": "medium", "3": "hard"}


        #checks if choice is a valid key
        if choice not in difficulty_map:
            print("Not a valid option, pick 1, 2, or 3.\n") #means they typed in something other than 1, 2, or 3
        else:
            play_game(difficulty_map[choice])

            # Replay
            #asks if they want to go again
            again = input("Play again? (yes/no): ").strip().lower()
            if again not in ("yes", "y"):
                print("\nThanks!!")
                playing = False
            else:
                print()


if __name__ == "__main__":
    main()