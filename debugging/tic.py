#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col] and
                board[0][col] != " "):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] and
            board[0][0] != " "):
        return True

    if (board[0][2] == board[1][1] == board[2][0] and
            board[0][2] != " "):
        return True

    return False


def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Validate row input
        while True:
            try:
                row = int(input(
                    f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    print("Row must be 0, 1, or 2. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number 0, 1, or 2.")

        # Validate col input
        while True:
            try:
                col = int(input(
                    f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    print("Column must be 0, 1, or 2. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number 0, 1, or 2.")

        # Check if spot is free
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
