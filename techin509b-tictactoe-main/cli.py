# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import make_empty_board, get_winner, other_player

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for i, row in enumerate(board):
        formatted_row = [cell if cell is not None else ' ' for cell in row]
        print(" | ".join(formatted_row))
        if i < 2:  # Add two dashes below the first and second rows
            print("-" * 9)

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'  # Player 'X' starts

    while winner is None:
        # Show the board to the user.
        print_board(board)
        print(f"Player {player}'s turn.")
        
        # Input a move from the player.
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        # Check if the selected cell is empty
        if board[row][col] is not None:
            print("Invalid move. Cell already occupied.")
            continue

        # Update the board.
        board[row][col] = player

        # Update who's turn it is.
        player = other_player(player)

        # Check for a winner
        winner = get_winner(board)

    # Show the final board to the user.
    print_board(board)

    if winner == 'X':
        print("Player X won!")
    elif winner == 'O':
        print("Player O won!")
    else:
        print("It's a draw!")