import math
import random

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

def initialize_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---+---+---")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    if all(cell != EMPTY for row in board for cell in row):
        return "Draw"

    return None

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return -10 + depth
    elif winner == PLAYER_O:
        return 10 - depth
    elif winner == "Draw":
        return 0

    if is_maximizing:
        max_eval = -math.inf
        best_moves = []
        for move in get_available_moves(board):
            board[move[0]][move[1]] = PLAYER_O
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            if eval > max_eval:
                max_eval = eval
                best_moves = [move]
            elif eval == max_eval:
                best_moves.append(move)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval if depth > 0 else random.choice(best_moves)
    else:
        min_eval = math.inf
        best_moves = []
        for move in get_available_moves(board):
            board[move[0]][move[1]] = PLAYER_X
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            if eval < min_eval:
                min_eval = eval
                best_moves = [move]
            elif eval == min_eval:
                best_moves.append(move)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval if depth > 0 else random.choice(best_moves)

def ai_move(board):
    if len(get_available_moves(board)) == 9:
        move = random.choice(get_available_moves(board))
    else:
        move = minimax(board, 0, True, -math.inf, math.inf)
    board[move[0]][move[1]] = PLAYER_O

def dynamic_difficulty(board, move_count):
    if move_count < 3:
        return random.choice(get_available_moves(board))
    else:
        return minimax(board, 0, True, -math.inf, math.inf)

def main():
    board = initialize_board()
    print("Welcome to an advanced Tic-Tac-Toe!")
    print_board(board)

    move_count = 0
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column 0-2, separated by space): ").split())
            if board[row][col] != EMPTY:
                print("Cell is already occupied. Try again.")
                continue
            board[row][col] = PLAYER_X
            move_count += 1
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            continue

        print_board(board)

        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        ai_move(board)
        print("AI has made its move:")
        print_board(board)

        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

if __name__ == "__main__":
    main()
