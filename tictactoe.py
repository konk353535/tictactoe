
class tictactoe(object):

	def __init__(self):
		# Initialises our board and class
		self.board = [[-1,1,-1],
					  [1,-1,1],
					  [1,-1,1]]
		self.player1 = 1
		self.player2 = -1

	def move(self,x,y, player):
		# Places a move on the board
		if(self.board[x][y] == 0):
			self.board[x][y] = player
			return True
		else:
			return False

	def display_board(self):
		# Prints the tic tac toe board
		print "|" + str(self.board[0][0]) + "|" + str(self.board[1][0]) + "|" + str(self.board[2][0]) + "|"
		print "|" + str(self.board[0][1]) + "|" + str(self.board[1][1]) + "|" + str(self.board[2][1]) + "|"
		print "|" + str(self.board[0][2]) + "|" + str(self.board[1][2]) + "|" + str(self.board[2][2]) + "|"

	def check_winner(self):
		# will return true if the game is won (includes draws)
		# False if the game isn't over

		# Checks left vertical
		if(sum(self.board[0]) == 3 or sum(self.board[0]) == -3):
			return True
		# Middle Vertical
		elif(sum(self.board[1]) == 3 or sum(self.board[1]) == -3):
			return True
		# Right Vertical
		elif(sum(self.board[2]) == 3 or sum(self.board[2]) == -3):
			return True

		# Top Horizontal
		elif(sum([self.board[0][0], self.board[1][0], self.board[2][0]]) == 3 or sum([self.board[0][0], self.board[1][0], self.board[2][0]]) == -3):
			return True
		# Middle Horizontal
		elif(sum([self.board[0][1], self.board[1][1], self.board[2][1]]) == 3 or sum([self.board[0][1], self.board[1][1], self.board[2][1]]) == -3):
			return True
		# Right Horizontal
		elif(sum([self.board[0][2], self.board[1][2], self.board[2][2]]) == 3 or sum([self.board[0][2], self.board[1][2], self.board[2][2]]) == -3):
			return True
		
		# Diagonal
		elif((self.board[0][0] + self.board[1][1] + self.board[2][2]) == 3 or (self.board[0][0] + self.board[1][1] + self.board[2][2]) == -3):
			return True
		# Diagonal
		elif((self.board[0][2] + self.board[1][1] + self.board[2][0]) == 3 or (self.board[0][2] + self.board[1][1] + self.board[2][0]) == -3):
			return True
		elif(0 not in self.board):
			return True
		else:
			return False
	def get_winner(self):
		# Will return 1 or 2 depending on who won
		pass
		

game = tictactoe()
game.display_board()
print str(game.board[0])
print str(game.check_winner())