import random
class TicTacToe:
def ==init==(self):
self.board =[]
def create_board9self0:
for i in range(3):
row.append('_')
self.board.append(row)
def get_random_first_player(self):
return random.randit(0,1)
def fix_spot(self, row, col, player):
win = None
n= len(self.board)
# checking rows
for i in range(n):
win = True
for j in range(n):
if self.board[i][j] != player:
win = False
break
if win:
return win
# checking columns
for i in range(n):
win = True
for j in range(n):
if self.board[j][i] != player:
win = False
break
if win
return win
# checking diagonals
win = True
for i in range(n):
if self.board[i][i] != player:
win = False
break
if win:
return win
win = Tue
for i in range(n):
if self.board[i][n-1-i] != player:
win = False
break
if win:
return win
return False
for row in self.board:
for item in row:
if item=='_':
return False
return True
def is_board_filled(self):
for row in self.board:
for item in row:
if item ='_':
return False
return True
def swap_player_turn(self, player):
return 'X' if player=='0' else '0'
def show_board(self):for row in self.board:
for item in row:
print(item, end=" ")
print()
def start(self):
self.create_board()
player ='X' if self.get_random_first_player() ==1 else '0'
while True:
print(f"Player {player} turn")
self.show_board()
#taking user input
row, col = list(
map(int, input("Enter row and column numbers to fis spot: "). split()))
print()
#fixing the spot
self.fix_spot(row -1, col-1, player)
#checking whether current player has won or not
if self.is_player_win(player):
print(f"Player {player} wins the game!")
beak
# checking whether the game is draw or not
if self.is_board_filled():
print("Match Draw!")
break
#swapping the turn
player = self.swap_player_turn(player)
#showing the final view of board
print()
self.show_board()
# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start
