import streamlit as st
import random

# Function to generate a random 3-digit secret number
def generate_secret_number():
    return str(random.randint(100, 999))

# Function to provide feedback for the guess
def check_guess(secret, guess):
    feedback = []
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("👌")  # Correct digit in the correct place
        elif guess[i] in secret:
            feedback.append("👍")  # Correct digit in the wrong place
        else:
            feedback.append("❌")  # No correct digits
    return feedback

# Main Streamlit app
def main():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .title {
            font-size: 40px;
            color: #FF4B4B;
            text-align: center;
            margin-bottom: 20px;
        }
        .feedback {
            font-size: 30px;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .attempts {
            font-size: 20px;
            color: #1F77B4;
            text-align: center;
        }
        .success {
            font-size: 30px;
            color: #2ECC71;
            text-align: center;
        }
        .error {
            font-size: 30px;
            color: #E74C3C;
            text-align: center;
        }
        .reset-button {
            text-align: center;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="title">🎮 Deductive Logic Game - Guess the Secret Number 🎮</div>', unsafe_allow_html=True)

    # Initialize session state for secret number and attempts
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = generate_secret_number()
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    st.write("### Rules:")
    st.write("1. Guess a 3-digit number.")
    st.write("2. You have 10 attempts to guess the secret number.")
    st.write("3. After each guess, you'll get feedback:")
    st.write("   - 👌 or 'Correct': A correct digit in the correct place.")
    st.write("   - 👍 or 'Ok': A correct digit in the wrong place.")
    st.write("   - ❌ or 'Wrong': No correct digits.")

    # Input for the user's guess
    guess = st.text_input("Enter your 3-digit guess:", max_chars=3, key="guess_input")

    # Button to submit the guess
    if st.button("Submit Guess"):
        if len(guess) != 3 or not guess.isdigit():
            st.error("Please enter a valid 3-digit number.")
        else:
            st.session_state.attempts += 1
            feedback = check_guess(st.session_state.secret_number, guess)

            # Display feedback
            st.markdown(f'<div class="feedback">{" ".join(feedback)}</div>', unsafe_allow_html=True)

            # Check if the guess is correct
            if guess == st.session_state.secret_number:
                st.markdown('<div class="success">🎉 You Got It! 🎉</div>', unsafe_allow_html=True)
                st.session_state.game_over = True
            elif st.session_state.attempts >= 10:
                st.markdown(
                    f'<div class="error">Game Over! The secret number was {st.session_state.secret_number}.</div>',
                    unsafe_allow_html=True,
                )
                st.session_state.game_over = True

    # Display remaining attempts
    st.markdown(
        f'<div class="attempts">Attempts left: {10 - st.session_state.attempts}</div>',
        unsafe_allow_html=True,
    )

    # Reset the game
    if st.session_state.game_over:
        st.markdown('<div class="reset-button">', unsafe_allow_html=True)
        if st.button("Play Again"):
            st.session_state.secret_number = generate_secret_number()
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()