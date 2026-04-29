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

