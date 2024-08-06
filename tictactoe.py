import random

players = ["o", "x"]
player_turn = random.choice(players)
board = [["0", "1", "2"],
         ["3", "4", "5"],
         ["6", "7", "8"]]

def printboard():
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--|---|--")
