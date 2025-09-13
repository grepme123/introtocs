import random
import os
import time

# Global variables (constants) for board dimensions and number of players
NUM_ROWS = 6
NUM_COLS = 6
NUM_PLAYERS = 2
SCORES = [ 0 ] * NUM_PLAYERS

# --- Board Creation Logic ---
# The number of pairs needed for a 6x6 board, excluding Jokes
num_pairs = (NUM_ROWS * NUM_COLS - 2) // 2

# Generate letter pairs (e.g., A and a)
cards = []
for i in range(num_pairs):
    upper = chr(ord('A') + i)
    lower = chr(ord('a') + i)
    cards.extend([upper, lower])

# Add two Joker cards
cards.extend(['*', '*'])

# Randomly shuffle the cards
random.shuffle(cards)

# Create the hidden and public boards
cards.sort()
hidden_board = [[cards.pop() for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
public_board = [['#' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

# --- Game Loop Logic ---
turn = random.randint(0, NUM_PLAYERS - 1)

while True:
    # Print the board!!
    os.system('clear')

    print(f"Player 2 score: {SCORES[1]}")
    print(f"Player 1 score: {SCORES[0]}")
    print("\n")

    # Printing column labels
    col_labels = "      " + " ".join([f" {chr(ord('A') + col)} " for col in range(NUM_COLS)])
    print(col_labels)

    # Show top border
    border_line = "    +" + "---+" * NUM_COLS
    print(border_line)

    # Print the board content with raw labels and borders
    for row in range(NUM_ROWS):
        row_str = f"  {row} |"
        for col in range(NUM_COLS):
            row_str += f" {public_board[row][col]} |"
        print(row_str)
        print(border_line)

    print("\n")

    # Check for game end condition
    remaining_cards = sum(row.count('#') for row in public_board)
    if remaining_cards <= 2:
        print("Only Jokers remain on the board!")
        SCORES[turn] += remaining_cards
        break

    print(f"Player {turn + 1}'s turn.")

    # --- Get and Validate First Input ---
    while True:
        try:
            coordinate_input = input(f"Player {turn + 1}: Enter a coordinate (e.g. B3): ").strip().upper()

            if not coordinate_input:
                print("Invalid input: Please enter a coordinate.")
                continue

            col_char = coordinate_input[0]
            row_str = coordinate_input[1:]

            if not 'A' <= col_char <= chr(ord('A') + NUM_COLS - 1):
                print("Invalid input: Column must be a letter from A to F.")
                continue

            if not row_str.isdigit():
                print("Invalid input: Row must be a number from 0 to 5.")
                continue

            col1 = ord(col_char)-ord('A')
            row1 = int(row_str)

            if not (0 <= row1 < NUM_ROWS and 0 <= col1 < NUM_COLS):
                print("Invalid input: Coordinates are out of bounds.")
                break

            if public_board[row1][col1] != '#':
                print("Invalid input: Card is already turned over.")
                continue

            break
        except (IndexError, ValueError):
            print("Invalid input: Please enter a coordinate in the format 'A0'.")
            continue

    public_board[row1][col1] = hidden_board[row1][col1]

    # Print the board after first card revealed
    os.system('clear')
    print(f"Player 2 score: {SCORES[1]}")
    print(f"Player 1 score: {SCORES[0]}")
    print(" \n ")

    col_labels = "      " + " ".join([f" {chr(ord('A') + col)} " for col in range(NUM_COLS)])
    print(col_labels)
    border_line = "    +" + "---+" * NUM_COLS
    print(border_line)
    for row in range(NUM_ROWS):
        row_str = f"  {row} |"
        for col in range(NUM_COLS):
            row_str += f" {public_board[row][col]} |"
        print(row_str)
        print(border_line)
    print("\n")
    print(f"Player {turn + 1}'s turn.")

    # --- Get and Validate Second Input ---
    while True:
        try:
            coordinate_input = input(f"Player {turn + 1}: Enter a coordinate (e.g. B3): ").strip().upper()

            if not coordinate_input:
                print("Invalid input: Please enter a coordinate.")
                continue

            col_char = coordinate_input[0]
            row_str = coordinate_input[1:]

            if not 'A' <= col_char <= chr(ord('A') + NUM_COLS - 1):
                print("Invalid input: Column must be a letter from A to F.")
                continue

            if not row_str.isdigit():
                print("Invalid input: Row must be a number from 0 to 5.")
                continue

            col2 = ord(col_char) - ord('A')
            row2 = int(row_str)

            if not (0 <= row2 < NUM_ROWS and 0 <= col2 < NUM_COLS):
                print("Invalid input: Coordinates are out of bounds.")
                continue

            if public_board[row2][col2] != '#':
                print("Invalid input: Card is already turned over")
                continue

            if (row1, col1) == (row2, col2):
                print("Invalid input: You must select a different card.")
                continue

            break
        except (IndexError, ValueError):
            print("Invalid input: Please enter a coordinate in the format 'AO'.")
            continue

    public_board[row2][col2] = hidden_board[row2][col2]

    # Print the board after second card is revealed
    os.system('clear')
    print(f"Player 2 score: {SCORES[1]}")
    print(f"Player 1 score: {SCORES[0]}")
    print("\n ")

    col_labels = "      " + " ".join([f" {chr(ord('A') + col)} " for col in range(NUM_COLS)])
    print(col_labels)
    border_line = "    +" + "---+" * NUM_COLS
    print(border_line)
    for row in range(NUM_ROWS):
        row_str = f"  {row} |"
        for col in range(NUM_COLS):
            row_str += f" {public_board[row][col]} |"
        print(row_str)
        print(border_line)
    print("\n")
    print(f"Player {turn + 1}'s turn.")

    card1 = hidden_board[row1][col1]
    card2 = hidden_board[row2][col2]

    # Check for a match
    is_joker_match = '*' in [card1, card2] and card1 != card2
    is_normal_match = card1.lower() == card2.lower() and card1 != card2

    if is_joker_match:
        print("Joker Match!!!")
        SCORES[turn] += 2
        public_board[row1][col1] = ' '
        public_board[row2][col2] = ' '
        hidden_board[row1][col1] = ' '
        hidden_board[row2][col2] = ' '
        time.sleep(2)
    elif is_normal_match:
        print("Match found!!")
        SCORES[turn] += 1
        public_board[row1][col1] = ' '
        public_board[row2][col2] = ' '
        hidden_board[row1][col1] = ' '
        hidden_board[row2][col2] = ' '
        time.sleep(2)
    else:
        print("No match. Turn ends.")
        time.sleep(2)
        public_board[row1][col1] = '#'
        public_board[row2][col2] = '#'
        turn = (turn + 1) % NUM_PLAYERS

# --- End of game logic ---
print("Game Over!?")
print(f"Final Score: Player 1 - {SCORES[0]}, Player 2 - {SCORES[1]}")
if SCORES[0] > SCORES[1]:
    print("Player 1 is the winner!")
elif SCORES[1] > SCORES[0]:
    print("Player 2 is the winner!")
else:
    print("It's a tie!")
