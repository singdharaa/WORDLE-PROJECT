import random

# ============================================================================================================
# Constants
# ============================================================================================================
WORDS = [
    "apple", "brain", "chair", "dance", "eagle",
    "flame", "ghost", "house", "image", "juice",
    "knife", "lemon", "money", "night", "ocean",
    "piano", "queen", "river", "stone", "train",
    "under", "vivid", "world", "xenon", "youth",
    "album", "beach", "cloud", "dream", "earth",
    "float", "grape", "heart", "input", "jazzy",
    "kiosk", "liver", "maple", "novel", "olive",
    "pride", "quest", "royal", "solar", "tower",
    "ultra", "value", "whale", "xylem", "zebra",
    "angel", "blank", "crane", "drift", "equal",
    "fresh", "grill", "honey", "index", "jewel",
]

ALL_LETTERS = set("abcdefghijklmnopqrstuvwxyz")

MAX_GUESSES = 6
WORD_LENGTH = 5 

instructions = '''
The secret word is always 5 letters
You get exactly 6 attempts
Each guess must be exactly 5 alphabetic characters
After each guess, you see feedback for each letter:
    🟩 = Correct letter in the correct position
    🟨 = Correct letter but wrong position
    ⬛ = Letter is not in the word at all
Duplicate letters in the answer are handled correctly (a letter only shows 🟨/🟩 for as many times as it appears in the answer)
'''

# ============================================================================================================
# Variables
# ============================================================================================================
stats_dict = {
    "played": 0, 
    "won": 0, 
    "streak": 0,
    "max-streak": 0,
    "guess-distribution": {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
}


# ============================================================================================================
# Game Logic
# ============================================================================================================
print("="*50)
print("Welcome to Worlde!")


# Main Loop
while(True):
    
    print("="*50)
    print("Main Menu")
    print("1. Start Game")
    print("2. Show Stats")
    print("3. How to play")
    print("4. Quit")
    print("="*50)
    
    menu = int(input("Enter Choice:"))
    
    # Start Game
    if(menu == 1):
        guess = 1
        answer = random.choice(WORDS)
        while(guess<=MAX_GUESSES):
            guess_word=""
            fb = []
            while(True):
                guess_word = (input(f"Attempt {guess} out of {MAX_GUESSES}: ").strip()).lower()
                if(len(guess_word)==5 and guess_word.isalpha()):
                    guess += 1
                    break
            for letter in guess_word:
                if letter in answer:
                    fb.append("🟨")
                else:
                    fb.append("⬛️")
            for guess_letter, ans_letter in zip(guess_word, answer):
                if guess_letter == ans_letter:
                    fb[answer.index(ans_letter)] = "🟩"
            # printing feedback of every letter in the guess_word
            for fb_letter,guess_letter in zip(fb,guess_word):
                print(fb_letter+guess_letter, end =" ") 
            print("\n")
            if fb.count('🟩') == 5:
                print(f"You guessed correctly in your {guess-1} attempt")
                break  
        else:
            print("You lost")   
                 
    # Showing Stats
    elif(menu == 2):
        print("The stats so far are as follows:")
        print(" "+"-"*49)
        for key, value in stats_dict.items():
            if key != "guess-distribution":
                print(f"| {key:<22} | {str(value):>22} |")      
        print(" "+"-"*49)
    
    # Game Instructions
    elif(menu == 3):
        print("="*50)
        print(f"Instructions of the game are as follows:- \n{instructions}")
        print("="*50)
    
    # Quitting Game
    elif(menu == 4):
        break
    else:
        print("😑 Enter a valid option")
    