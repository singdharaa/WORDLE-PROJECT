# 📋 Project Statement
What you're building: A terminal version of the popular word-guessing game Wordle. The computer picks a secret 5-letter word, and you have 6 attempts to guess it. After each guess, you get color-coded feedback showing which letters are correct, misplaced, or absent.

## Rules:

- The secret word is always 5 letters
- You get exactly 6 attempts
- Each guess must be exactly 5 alphabetic characters
- After each guess, you see feedback for each letter:
    - 🟩 = Correct letter in the correct position
    - 🟨 = Correct letter but wrong position
    - ⬛ = Letter is not in the word at all
- Duplicate letters in the answer are handled correctly (a letter only shows 🟨/🟩 for as many times as it appears in the answer)

## Features to implement:

- Main menu — Play, view stats, see how-to-play instructions, quit
- Two-pass feedback algorithm — First mark exact matches (green), then mark present-but-misplaced (yellow). This correctly handles duplicate letters.
- Keyboard tracker — After each guess, show which letters are confirmed correct, present, or a    absent - across the full alphabet
- All guesses display — Show all previous guesses and feedback after each new guess
- Game statistics — Track games played, win %, current streak, max streak, and guess distribution (histogram)
- Share-style result — Show the emoji-only grid at the end (like the real Wordle share feature)

## Concepts used: 
Lists, dicts, sets, string methods, while/for loops, input validation, f-strings, nested data (list of tuples), None as sentinel value