def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"É a vez do jogador {current_player}")

        row = int(input("Informe o número da linha (0-2): "))
        col = int(input("Informe o número da coluna (0-2): "))

        if board[row][col] != " ":
            print("Posição inválida! Tente novamente.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"O jogador {current_player} venceu!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("O jogo terminou em empate!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()

