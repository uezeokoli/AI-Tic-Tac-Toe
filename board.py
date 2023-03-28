# author: Ugonna Ezeokoli
# date: Feb 4, 2023
# file: board.py a Python program that implements the board of the tic-tac-toe game.
# input: parameters to complete the functions 
# output: the tic-tac-toe board (any updates and changes to the board)

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
      def get_size(self): 
             # optional, return the board size (an instance size)
             pass
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)    
            if (self.board[0] == self.board[1] == self.board[2] == "O") or (self.board[3] == self.board[4] == self.board[5] == "O") or \
            (self.board[6] == self.board[7] == self.board[8] == "O") or (self.board[0] == self.board[3] == self.board[6] == "O") or \
            (self.board[1] == self.board[4] == self.board[7] == "O") or (self.board[2] == self.board[5] == self.board[8] == "O") or \
            (self.board[0] == self.board[4] == self.board[8] == "O") or (self.board[2] == self.board[4] == self.board[6] == "O"):
                  return "O"
            elif (self.board[0] == self.board[1] == self.board[2] == "X") or (self.board[3] == self.board[4] == self.board[5] == "X") or \
            (self.board[6] == self.board[7] == self.board[8] == "X") or (self.board[0] == self.board[3] == self.board[6] == "X") or \
            (self.board[1] == self.board[4] == self.board[7] == "X") or (self.board[2] == self.board[5] == self.board[8] == "X") or \
            (self.board[0] == self.board[4] == self.board[8] == "X") or (self.board[2] == self.board[4] == self.board[6] == "X"):
                  return "X"
            return None
      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ['A1', 'B1', 'C1','A2','B2','C2','A3','B3','C3']
            index = valid_choices.index(cell)
            self.board[index] = sign

      def clear(self, cell):
            # clears a cell on the baord back to blank
            valid_choices = ['A1', 'B1', 'C1','A2','B2','C2','A3','B3','C3']
            index = valid_choices.index(cell)
            self.board[index] = " "

            
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            valid_choices = ['A1', 'B1', 'C1','A2','B2','C2','A3','B3','C3']
            index = valid_choices.index(cell)
            if self.board[index] == " ":
                  return True
            else:
                  return False
      def isdone(self):
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            if (self.board[0] == self.board[1] == self.board[2] != " ") or (self.board[3] == self.board[4] == self.board[5] != " ") or \
            (self.board[6] == self.board[7] == self.board[8] != " ") or (self.board[0] == self.board[3] == self.board[6] != " ") or \
            (self.board[1] == self.board[4] == self.board[7] != " ") or (self.board[2] == self.board[5] == self.board[8] != " ") or \
            (self.board[0] == self.board[4] == self.board[8] != " ") or (self.board[2] == self.board[4] == self.board[6] != " "):
                  done = True
            elif " " not in self.board:
                  done = True 
            return done
      def show(self):
            # draw the board
            # need to complete the code
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
            print(' +---+---+---+')
