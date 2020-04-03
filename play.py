# Bunaren TicTacToe AI Engine
# Created by Fransiscus Emmanuel Bunaren

# This file is for playing against AI

#Libraries
from engine import Engine
from board import Board
import os

def main():
    board = Board()

    print("Bunaren TicTacToe AI")
    print("========================")
    symbol= input("Choose your symbol (X/O) : ").upper()

    engine = Engine()
    engine.setSymbol("O" if symbol == "X" else "X")

    #Computer Starts first if X is chosen by player
    if symbol == "O":
        board.move(engine.bestMove(board.board))
    board.print()

    while not board.isOver():
        pos = list(map(int,input("Draw " + symbol + " at [row column] : ").split()))
        pos = [i-1 for i in pos]
        pos = pos[0] * 3 + pos[1]
        while not board.isValid(pos):
            print("Invalid Position")
            pos = list(map(int,input("Draw " + symbol + " at [row column] : ").split()))
            pos = [i-1 for i in pos]
            pos = pos[0] * 3 + pos[1]
        board.move(pos)

        if board.isOver():
            break

        #Computer's Turn
        board.move(engine.bestMove(board.board))
        board.print()

    print()
    board.print()
    print("\nGame Over!")
    result = board.isOver()
    if result == "Draw":
        print("It's a draw!")
    elif result == symbol:
        print("You win!")
    else:
        print("You lose!")

    #Play Again?
    play_again = input("\nPlay again? [y/n] : ").lower()
    if play_again == "y":
        os.system("cls")
        main()
    else:
        print("Thanks for playing!")
        input("Press enter to quit...")

main()