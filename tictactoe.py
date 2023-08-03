def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all(
        [board[i][2 - i] == player for i in range(3)]
    ):
        return True

    return False


def is_board_full(board):
    return all([cell != " " for row in board for cell in row])


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[player_index]
        row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            print_board(board)

            if check_win(board, player):
                print(f"Player {player} wins!")
                break

            if is_board_full(board):
                print("It's a draw!")
                break

            player_index = (player_index + 1) % 2
        else:
            print("Cell already taken. Try again.")


# main
tic_tac_toe()
