
class tictactoe(object):

	def __init__(self):
		self.board = [[0,0,0],
					  [0,0,0],
					  [0,0,0]]
		self.player1 = 1
		self.player2 = 2

	def move(self,x,y, player):
		if(self.board[x][y] == 0):
			self.board[x][y] = player
			return True
		else:
			return False

	def display_board(self):
		print "|" + str(self.board[0][0]) + "|" + str(self.board[1][0]) + "|" + str(self.board[2][0]) + "|"
		print "|" + str(self.board[0][1]) + "|" + str(self.board[1][1]) + "|" + str(self.board[2][1]) + "|"
		print "|" + str(self.board[0][2]) + "|" + str(self.board[1][2]) + "|" + str(self.board[2][2]) + "|"

	def check_winner(self):
		# will return true or false

	def get_winner(self):
		# Will return 1 or 2 depending on who won
		

game = tictactoe()
game.move(1,0,1)
game.display_board()
