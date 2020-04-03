# Bunaren TicTacToe AI Engine
# Created by Fransiscus Emmanuel Bunaren

from random import uniform,choice
import pprint
import json
from board import Board

class Engine:
    def __init__(self):
        self.symbol2value = lambda x : 1 if x == "X" else (-1 if x == "O" else 0)

    def setSymbol(self,symbol="X"):
        self.symbol = symbol

    #For changing X to O, vice versa
    def invertSymbol(self,symbol):
        return "X" if symbol.upper() == "O" else "O"

    def bestMove(self,inputs,ai_turn=True,depth=0,alpha = -float("inf"),beta = float("inf")):
        inputs = list(inputs)
        board = Board()
        board.setBoard(inputs)
        best_value = [float("inf"),0]
        best_value[0] *= -1 if ai_turn else 1
        for i in range(len(board.board)):
            #If it reaches terminating state
            if board.isOver() == self.symbol:
                return 10 - depth
            elif board.isOver() == "Draw":
                return 0
            elif board.isOver() == self.invertSymbol(self.symbol):
                return depth - 10
            #Find another possible moves
            tmp_board = board.board[:]
            if tmp_board[i] == " ":
                tmp_board[i] = self.invertSymbol(self.symbol) if not ai_turn else self.symbol
                state_value = self.bestMove(tmp_board,not ai_turn,depth + 1,alpha,beta)
                if ai_turn:
                    if best_value[0] < state_value:
                        best_value = [state_value,i]
                        alpha = max(alpha,best_value[0])
                else:
                    if best_value[0] > state_value:
                        best_value = [state_value,i]
                        beta = min(beta,best_value[0])
            #Alpha Beta Pruning
            if beta <= alpha:
                break
        return best_value[0] if depth != 0 else best_value[1]

if __name__ == "__main__":
    engine = Engine()
    engine.setSymbol("X")
    print(engine.bestMove("XO" + " "*7))