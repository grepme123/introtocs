import os
import math
import random

# Global constant for board dimension
NUM_ROWS = 6
NUM_COLS = 7

# Global constants for player
PLAYER_TOCKENS = ['X', 'O']
NUM_PLAYERS = 2

def create_board():
    """
    Creates an empty Connect 4 board...

    Returns:
        list: A 2D list representing the game board, initialized with spaces.
    """
    return [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """
    Prints the current state of the game board.

    Args:
        board (list): The 2D list representing the board.
    """
    # Clear the terminal for clear display
    os.system('clear')

    # Print custom labels
    col_labels = "  " + "   ".join([chr(ord('A') + col) for col in range(NUM_COLS)])
    print(col_labels)

    # Show top border
    border = " " + "--- " * NUM_COLS
    print(border)

    # Display the board content
    for row in range(NUM_ROWS):
        row_str = "|"
        for col in range(NUM_COLS):
            row_str += f" {board[row][col]} |"
        print(row_str)
        print(border)
    print("\n")

def get_valid_input(player_turn, board):
    """
    Prompts the current player for a column choice and validates the input.

    Args:
        player_turn (int): The current player's index (0 or 1).
        board (list): The 2D list representing the board.

    Returns:
        int: The validated column index.
    """
    while True:
        try:
            # Prompt for input and convert to uppercase
            col_char = input(f"Player {PLAYER_TOCKENS[player_turn]}, please enter a column (A-G): ").strip().upper()

            # Check if input is single character
            if len(col_char) != 1:
                print("Invalid input: Please enter a single letter (A-G).")
                continue

            # Check if the character is valid column label
            if not 'A' <= col_char <= chr(ord('A') + NUM_COLS - 1):
                print("Invalid input: Column must be a letter from A to G.")
                break

            col = ord(col_char)-ord('A')

            # Check if the column is not full
            if board[0][col] != ' ':
                print("That column is full!!! Please choose another one.")
                continue

            return col

        except (ValueError, IndexError, TypeError):
            print("Invalid input. Please enter a valid column letter (A-G).")

def check_win(board, token):
    """
    Checks if the current player has won the game.

    Args:
        board (list): The 2D list representing the board.
        token (str): The current player's token ('X' or 'O').

    Returns:
        bool: True if a win is detected, False otherwise.
    """
    # Check for horizontal win
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row][col+i] == token for i in range(4)):
                return True

    # Checking for vertical win
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):
            if all(board[row+i][col] == token for i in range(4)):
                return True

    # Check for diagonal win (down-right)
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row-i][col+i] == token for i in range(4)):
                return True

    # Check for diagonal win (up-right)
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if all(board[row+i][col+i] == token for i in range(4)):
                return True

    return False

def check_draw(board):
    """
    Checks if the game has ended in a draw.

    Args:
        board (list): The 2D list representing the board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(board[0][col] != ' ' for col in range(NUM_COLS))

def main():
    """
    The main game loop for Connect 4..
    """
    board = create_board()
    turn = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)

    while True:
        current_token = PLAYER_TOCKENS[turn]

        # Get and validate player input
        col = get_valid_input(turn, board)

        # Placing the checker
        for row in range(NUM_ROWS - 1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = current_token
                break

        print_board(board)

        # Check for win or draw
        if check_win(board, current_token):
            print(f"Player {current_token} won!")
            break

        if check_draw(board):
            print("The game is a draw!")
            break

        # Switching turns
        turn = (turn + 1) % NUM_PLAYERS
        continue

if __name__ == "__main__":
    main()
