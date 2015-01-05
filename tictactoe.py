
class tictactoe(object):

	def __init__(self):
		# Initialises our board and class
		self.board = [[0,0,0],
					  [0,0,0],
					  [0,0,0]]
		self.player1 = 1
		self.player2 = -1

	def move(self,x,y, player):
		
		# checks for invalid inputs
		if(x > 2 or y > 2 or x < 0 or y < 0):
			return False
		# Places a move on the board
		elif(self.board[x][y] == 0):
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
		elif(not any(0 in sublist for sublist in self.board)):
			return True
		else:
			return False

	def get_winner(self):
		# Will return 1 or 2 depending on who won
		for number in [-1, 1]:
			# Checks left vertical
			if(sum(self.board[0]) == number*3 ):
				return number
			# Middle Vertical
			elif(sum(self.board[1]) == number*3 ):
				return number
			# Right Vertical
			elif(sum(self.board[2]) == number*3):
				return number

			# Top Horizontal
			elif(sum([self.board[0][0], self.board[1][0], self.board[2][0]]) == number*3):
				return number
			# Middle Horizontal
			elif(sum([self.board[0][1], self.board[1][1], self.board[2][1]]) == number*3):
				return number
			# Right Horizontal
			elif(sum([self.board[0][2], self.board[1][2], self.board[2][2]]) == number*3):
				return number
			
			# Diagonal
			elif((self.board[0][0] + self.board[1][1] + self.board[2][2]) == number*3):
				return number
			# Diagonal
			elif((self.board[0][2] + self.board[1][1] + self.board[2][0]) == number*3):
				return number
		else:
			return 0
	
	def play_game(self):
		# Keeps track of who's turn it is
		toMove = -1

		# Runs while the game is not over
		while(not self.check_winner()):
			
			# Defaults to the move entered being incorrect
			move = False
			
			while(not move):
				self.display_board()
				inputX = input("Enter X")
				inputY = input("Enter Y")
				move = self.move(inputX, inputY, toMove)

			
			toMove *= -1
		print "Game Over"
		print str(self.get_winner()) + "Won"


game = tictactoe()
print str(game.check_winner())
game.play_game()