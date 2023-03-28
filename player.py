# author: Ugonna Ezeokoli
# date: Feb 4, 2023
# file: player.py a Python program that implements each player for the tic-tac-toe game
# input: parameters to complete the functions 
# output: the sign of the player to put on board

from random import choice
import math
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'B1', 'C1','A2','B2','C2','A3','B3','C3']
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
                  if cell in valid_choices:
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                              print('You did not choose correctly.')
                  else:
                        print('You did not choose correctly.')

class AI(Player):
      def __init__(self,name,sign,board):
            super().__init__(name,sign)
            self.board = board  #tic-tac-toe board

      def choose(self,board):
          #   AI automatically chooses a cell by using choice function in random module
          #   picks a random cell from valid_choices and if that cells is empty it will put players sign in the cell
            valid_choices = ['A1', 'B1', 'C1','A2','B2','C2','A3','B3','C3']
            while True:
                  cell = choice(valid_choices)
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        break


class MiniMax(AI):
    def __init__(self,name,sign,board):
      super().__init__(name,sign,board)
      self.valid_choices = ['A1', 'B1', 'C1','A2','B2','C2','A3','B3','C3']
      if self.sign == "X":
           self.mm_sign = "O"
      else:
           self.mm_sign = "X"


    def choose(self, board):
     #  Chooses a cell by checking all avaliable cells and going through all of possiblities and choosing cell with best outcome  
        maxscore = -math.inf
        move = " "
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        for cell in self.valid_choices:
             if board.isempty(cell):
                  board.set(cell,self.sign)
                  score = MiniMax.minimax(self,board,False,False)
                  board.clear(cell)
                  if (score > maxscore):
                       maxscore = score
                       move = cell
                       
        print(move)
        board.set(move, self.sign)


        
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.get_sign():
                return 1
            # is a tie
            elif board.get_winner() == None:
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
                
        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code
          # When it is predicting the players move 
        if self_player:
            maxscore = -math.inf
            for cell in self.valid_choices:
                 if board.isempty(cell):
                      board.set(cell,self.sign)
                      score = MiniMax.minimax(self,board,False,False)
                      board.clear(cell)
                      if (score > maxscore):
                           maxscore = score

            return maxscore
     #    When it is predicting the opponents move
        else:
            minscore = math.inf
            for cell in self.valid_choices:
                 if board.isempty(cell):
                      board.set(cell,self.mm_sign)
                      score = MiniMax.minimax(self,board,True,True)
                      board.clear(cell)
                      if (score < minscore):
                           minscore = score
            return minscore

class SmartAI(Player):
     def __init__(self, name, sign, board):
          super().__init__(name,sign)
          if self.sign == "X":
                self.oppsign = "O"
          else:
                self.oppsign = "X"

     def choose(self,board):
          #   Chooses cell by checking through mutliple conditions based on game logic
            valid_choices = ['A1', 'B1', 'C1','A2','B2','C2','A3','B3','C3']
            corners = ['A1', 'C1','A3','C3']
            while True:
               #    Places sign in center if empty
                  if board.board[4] == " ":
                        board.board[4] = self.sign
                        break

                    #   Checks horizontal, vertical and diagnol for if player has two signs in a row  
                  if board.board[0] == board.board[1] == self.sign:
                       if board.board[2] == " ":
                              board.board[2] = self.sign
                              break
                  if board.board[1] == board.board[2] == self.sign:
                       if board.board[0] == " ":
                              board.board[0] = self.sign
                              break
                  if board.board[0] == board.board[2] == self.sign:
                       if board.board[1] == " ":
                              board.board[1] = self.sign
                              break
                  if board.board[3] == board.board[4] == self.sign:
                       if board.board[5] == " ":
                              board.board[5] = self.sign
                              break
                  if board.board[4] == board.board[5] == self.sign:
                       if board.board[3] == " ":
                              board.board[3] = self.sign
                              break
                  if board.board[3] == board.board[5] == self.sign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                  if board.board[6] == board.board[7] == self.sign:
                       if board.board[8] == " ":
                              board.board[8] = self.sign
                              break
                  if board.board[7] == board.board[8] == self.sign:
                       if board.board[6] == " ":
                              board.board[6] = self.sign
                              break
                  if board.board[6] == board.board[8] == self.sign:
                       if board.board[7] == " ":
                              board.board[7] = self.sign
                              break
                  if board.board[0] == board.board[3] == self.sign:
                       if board.board[6] == " ":
                              board.board[6] = self.sign
                              break
                  if board.board[0] == board.board[6] == self.sign:
                       if board.board[3] == " ":
                              board.board[3] = self.sign
                              break
                  if board.board[3] == board.board[6] == self.sign:
                       if board.board[0] == " ":
                              board.board[0] = self.sign
                              break
                  if board.board[1] == board.board[4] == self.sign:
                       if board.board[7] == " ":
                              board.board[7] = self.sign
                              break
                  if board.board[4] == board.board[7] == self.sign:
                       if board.board[1] == " ":
                              board.board[1] = self.sign
                              break
                  if board.board[1] == board.board[7] == self.sign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                  if board.board[2] == board.board[5] == self.sign:
                       if board.board[8] == " ":
                              board.board[8] = self.sign
                              break
                  if board.board[5] == board.board[8] == self.sign:
                       if board.board[2] == " ":
                              board.board[2] = self.sign
                              break
                  if board.board[2] == board.board[8] == self.sign:
                       if board.board[5] == " ":
                              board.board[5] = self.sign
                              break
                  if board.board[0] == board.board[4] == self.sign:
                       if board.board[8] == " ":
                              board.board[8] = self.sign
                              break
                  if board.board[4] == board.board[8] == self.sign:
                       if board.board[0] == " ":
                              board.board[0] = self.sign
                              break
                  if board.board[0] == board.board[8] == self.sign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                  if board.board[2] == board.board[4] == self.sign:
                       if board.board[6] == " ":
                              board.board[6] = self.sign
                              break
                  if board.board[4] == board.board[6] == self.sign:
                       if board.board[2] == " ":
                              board.board[2] = self.sign
                              break
                  if board.board[2] == board.board[6] == self.sign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                       
                         #   Checks horizontal, vertical and diagnol for if opponent has two signs in a row  
                  if board.board[0] == board.board[1] == self.oppsign:
                       if board.board[2] == " ":
                              board.board[2] = self.sign
                              break
                  if board.board[1] == board.board[2] == self.oppsign:
                       if board.board[0] == " ":
                              board.board[0] = self.sign
                              break
                  if board.board[0] == board.board[2] == self.oppsign:
                       if board.board[1] == " ":
                              board.board[1] = self.sign
                              break
                  if board.board[3] == board.board[4] == self.oppsign:
                       if board.board[5] == " ":
                              board.board[5] = self.sign
                              break
                  if board.board[4] == board.board[5] == self.oppsign:
                       if board.board[3] == " ":
                              board.board[3] = self.sign
                              break
                  if board.board[3] == board.board[5] == self.oppsign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                  if board.board[6] == board.board[7] == self.oppsign:
                       if board.board[8] == " ":
                              board.board[8] = self.sign
                              break
                  if board.board[7] == board.board[8] == self.oppsign:
                       if board.board[6] == " ":
                              board.board[6] = self.sign
                              break
                  if board.board[6] == board.board[8] == self.oppsign:
                       if board.board[7] == " ":
                              board.board[7] = self.sign
                              break
                  if board.board[0] == board.board[3] == self.oppsign:
                       if board.board[6] == " ":
                              board.board[6] = self.sign
                              break
                  if board.board[0] == board.board[6] == self.oppsign:
                       if board.board[3] == " ":
                              board.board[3] = self.sign
                              break
                  if board.board[3] == board.board[6] == self.oppsign:
                       if board.board[0] == " ":
                              board.board[0] = self.sign
                              break
                  if board.board[1] == board.board[4] == self.oppsign:
                       if board.board[7] == " ":
                              board.board[7] = self.sign
                              break
                  if board.board[4] == board.board[7] == self.oppsign:
                       if board.board[1] == " ":
                              board.board[1] = self.sign
                              break
                  if board.board[1] == board.board[7] == self.oppsign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                  if board.board[2] == board.board[5] == self.oppsign:
                       if board.board[8] == " ":
                              board.board[8] = self.sign
                              break
                  if board.board[5] == board.board[8] == self.oppsign:
                       if board.board[2] == " ":
                              board.board[2] = self.sign
                              break
                  if board.board[2] == board.board[8] == self.oppsign:
                       if board.board[5] == " ":
                              board.board[5] = self.sign
                              break
                  if board.board[0] == board.board[4] == self.oppsign:
                       if board.board[8] == " ":
                              board.board[8] = self.sign
                              break
                  if board.board[4] == board.board[8] == self.oppsign:
                       if board.board[0] == " ":
                              board.board[0] = self.sign
                              break
                  if board.board[0] == board.board[8] == self.oppsign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                  if board.board[2] == board.board[4] == self.oppsign:
                       if board.board[6] == " ":
                              board.board[6] = self.sign
                              break
                  if board.board[4] == board.board[6] == self.oppsign:
                       if board.board[2] == " ":
                              board.board[2] = self.sign
                              break
                  if board.board[2] == board.board[6] == self.oppsign:
                       if board.board[4] == " ":
                              board.board[4] = self.sign
                              break
                       #   Checks for edge placement game technique  
                  if (board.board[1] == board.board[3] != " ") and (board.board[0] == " ") and (board.board[2] == " ") and (board.board[6] == " "):
                        board.board[0] = self.sign
                        break
                  if (board.board[1] == board.board[5] != " ") and (board.board[2] == " ") and (board.board[0] == " ") and (board.board[8] == " "):
                        board.board[2] = self.sign
                        break
                  if (board.board[5] == board.board[7] != " ") and (board.board[8] == " ") and (board.board[2] == " ") and (board.board[6] == " "):
                        board.board[8] = self.sign
                        break
                  if (board.board[3] == board.board[7] != " ") and (board.board[6] == " ") and (board.board[0] == " ") and (board.board[8] == " "):
                        board.board[6] = self.sign
                        break
                    #     Checks for corner placement game technique
                  if (" " in board.board[0]) or (" " in board.board[2]) or (" " in board.board[6]) or (" " in board.board[8]):
                       if (board.board[0] == self.oppsign) and (board.board[8] == self.oppsign):
                             if (board.board[1] == " ") and (board.board[4] == self.sign):
                                   board.board[1] = self.sign
                                   break
                       if board.board[2] == self.oppsign and (board.board[6] == self.oppsign):
                             if (board.board[5] == " ") and (board.board[4] == self.sign):
                                   board.board[5] = self.sign
                                   break
                       if board.board[6] == self.oppsign and (board.board[2] == self.oppsign):
                             if (board.board[3] == " ") and (board.board[4] == self.sign):
                                   board.board[3] = self.sign
                                   break
                       if board.board[8] == self.oppsign and (board.board[0] == self.oppsign):
                             if (board.board[7] == " ") and (board.board[4] == self.sign):
                                   board.board[7] = self.sign
                                   break
                             

                    # places sign in a corner if none of the previous conditions are met
                       if board.board[0] == " ":
                             board.board[0] = self.sign
                             break
                       if board.board[2] == " ":
                             board.board[2] = self.sign
                             break
                       if board.board[6] == " ":
                             board.board[6] = self.sign
                             break
                       if board.board[8] == " ":
                             board.board[8] = self.sign
                             break
                    #    Chooses a random empty cell if none of the previous conditions are met.
                  cell = choice(valid_choices)
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        break
            
                        
                        
                  
