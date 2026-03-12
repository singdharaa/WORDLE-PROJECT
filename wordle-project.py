import random

# Constants
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

# Game Logic
print("="*50)
print("Welcome to Worlde!")
print("="*50)

