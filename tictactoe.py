import random

players = ["o", "x"]
player_turn = random.choice(players)
board = [["0", "1", "2"],
         ["3", "4", "5"],
         ["6", "7", "8"]]
turn = 0

def printboard():
    for i, board_row in enumerate(board):
        print(" | ".join(board_row))
        if i < len(board) - 1:
            print("--|---|--")

def check_win(player):
    #for rows
    if (board[0][0] == player) and (board[0][1] == player) and (board[0][2] == player):
        return True
    elif (board[1][0] == player) and (board[1][1] == player) and (board[1][2] == player):
        return True
    elif (board[2][0] == player) and (board[2][1] == player) and (board[2][2] == player):
        return True
    #for columns
    elif (board[0][0] == player) and (board[1][0] == player) and (board[2][0] == player):
        return True
    elif (board[0][1] == player) and (board[1][1] == player) and (board[2][1] == player):
        return True
    elif (board[0][2] == player) and (board[1][2] == player) and (board[2][2] == player):
        return True
    #for diagonals
    elif (board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player):
        return True
    elif (board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player):
        return True
    return False

while True:
    player = player_turn
    printboard()
    print("Enter number from 0 to 8, q to quit.")
    user_input = input(f"{player}'s turn: ")

    if user_input.lower() == "q":
        break
    if user_input.isdigit():
        user_input = int(user_input)
        if (user_input >= 0) and (user_input <= 8):
            row, col = divmod(user_input, 3)
            if board[row][col] not in players:
                board[row][col] = player
                turn += 1
                if check_win(player):
                    printboard()
                    print(f"Player {player} wins!")
                    break
                if turn == 9:
                    printboard()
                    print("Its a Tie!")
                    break
                player_turn = "x" if player_turn == "o" else "o"
            else:
                print("Cell is already taken.")
        else:
            print("Please enter number from 0 to 8.")
    else:
        print("Please only enter numbers.")