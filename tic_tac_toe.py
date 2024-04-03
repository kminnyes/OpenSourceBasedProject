import random


def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False


def player_turn(board):
    while True:
        try:
            move = int(input("당신의 차례입니다. 1에서 9까지의 숫자를 입력하세요: ")) - 1
            row, col = divmod(move, 3)
            if make_move(board, row, col, "X"):
                break
            else:
                print("잘못된 위치입니다. 다시 시도해주세요.")
        except ValueError:
            print("유효한 숫자를 입력해주세요.")


def computer_turn(board):
    print("컴퓨터의 차례입니다...")
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if make_move(board, row, col, "O"):
            break


def main():
    board = initialize_board()
    turn = "player" if random.randint(0, 1) == 0 else "computer"

    while True:
        print_board(board)
        if turn == "player":
            player_turn(board)
            if check_win(board, "X"):
                print_board(board)
                print("축하합니다! 당신이 이겼습니다.")
                break
            turn = "computer"
        else:
            computer_turn(board)
            if check_win(board, "O"):
                print_board(board)
                print("컴퓨터가 승리했습니다.")
                break
            turn = "player"

        if check_draw(board):
            print_board(board)
            print("무승부입니다.")
            break


if __name__ == "__main__":
    main()