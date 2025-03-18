🎮 Deductive Logic Game - Guess the Secret Number 🎮
A fun and interactive Streamlit app where you guess a secret 3-digit number using deductive logic. After each guess, you’ll receive real-time feedback to help you crack the code!

Features
Real-Time Feedback: Get instant feedback after each guess using emojis (👌, 👍, ❌) or text (Correct, Ok, Wrong).

Colorful Design: Modern and vibrant UI with custom styling.

Reset Button: Play again after winning or losing.

Progress Tracking: See how many attempts you have left.

How to Play
The app generates a random 3-digit secret number.

You have 10 attempts to guess the number.

After each guess, you’ll receive feedback:

👌 or Correct: A digit is in the correct place.

👍 or Ok: A digit is correct but in the wrong place.

❌ or Wrong: No correct digits.

If you guess the number correctly within 10 attempts, you win! Otherwise, the game ends, and the secret number is revealed.


Welcome Screen:

🎮 Deductive Logic Game - Guess the Secret Number 🎮
Rules:
1. Guess a 3-digit number.
2. You have 10 attempts to guess the secret number.
3. After each guess, you'll get feedback:
   - 👌 or 'Correct': A correct digit in the correct place.
   - 👍 or 'Ok': A correct digit in the wrong place.
   - ❌ or 'Wrong': No correct digits.



User Input:


Enter your 3-digit guess: 123
Feedback:


Feedback: ❌ 👍 👍
Attempts left: 9
Winning Scenario:


Feedback: 👌 👌 👌
🎉 You Got It! 🎉
Play Again
Losing Scenario:


Game Over! The secret number was 631.
Play Again
Customization
Change Emojis: Replace 👌, 👍, and ❌ with your preferred symbols or text.

Increase Attempts: Modify the attempts limit in the code.

Add More Digits: Extend the game to 4 or 5-digit numbers by updating the generate_secret_number and check_guess functions.


