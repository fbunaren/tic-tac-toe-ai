# Bunaren TicTacToe Board
# Created by Fransiscus Emmanuel Bunaren

# This file is for the TicTacToe Board
class Board:
    def __init__(self):
        self.symbol2value = lambda x : 1 if x == "X" else (-1 if x == "O" else 0)
        self.board = list(" "*9)
        self.turn = "X"

    def setBoard(self,inputs):
        if type(inputs) != list:
            inputs = list(inputs)
        self.board = inputs
        return self.board

    #For printing the current state of board
    def print(self,show_turn=False):
        print("  " + str(['1','2','3']).replace("["," ").replace("]"," ").replace("'","").replace(","," "))
        print(1,str([self.board[0],self.board[1],self.board[2]]).replace("'","").replace(",","|"))
        print(2,str([self.board[3],self.board[4],self.board[5]]).replace("'","").replace(",","|"))
        print(3,str([self.board[6],self.board[7],self.board[8]]).replace("'","").replace(",","|"))
        if show_turn:
            print("\n" + self.turn , "turns")

    def getTurn(self):
        return self.turn

    def changeTurn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def isOver(self):
        #Checking Rows
        for i in [[0,1,2] , [3,4,5] , [6,7,8]]:
            is_over = abs(sum([self.symbol2value(self.board[k]) for k in i]))
            if is_over == 3:
                return self.board[i[0]]
        #Columns
        tmp = [0,3,6]
        for i in range(3):
           is_over = abs(sum([self.symbol2value(self.board[i+k]) for k in tmp]))
           if is_over == 3:
                return self.board[i+tmp[0]]
        #Diagonal
        is_over = abs(sum([self.symbol2value(self.board[0]),self.symbol2value(self.board[4]),self.symbol2value(self.board[8])]))
        if is_over == 3:
            return self.board[0]
        is_over = abs(sum([self.symbol2value(self.board[2]),self.symbol2value(self.board[4]),self.symbol2value(self.board[6])]))
        if is_over == 3:
            return self.board[2]
        
        #If none of the above satisfied, then check if it is a draw
        if self.board.count(" ") <= 0:
            return "Draw"
        else:
            return False

    #For checking if a position is valid
    def isValid(self,pos):
        if pos < 9 and pos >= 0 and self.board[pos] == " ":
            return True
        else:
            return False

    def move(self,pos):
        if self.isValid(pos):
            self.board[pos] = self.turn
            self.changeTurn()
            return self.board
        else:
            return False
