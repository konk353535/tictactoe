
class tictactoe(object):

	def __init__(self, board):
		# Initialises our board and class
		self.board = board
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

def check_winner(board):
	# will return true if the game is won (includes draws)
	# False if the game isn't over

	# Checks left vertical
	if(sum(board[0]) == 3 or sum(board[0]) == -3):
		return True
	# Middle Vertical
	elif(sum(board[1]) == 3 or sum(board[1]) == -3):
		return True
	# Right Vertical
	elif(sum(board[2]) == 3 or sum(board[2]) == -3):
		return True

	# Top Horizontal
	elif(sum([board[0][0], board[1][0], board[2][0]]) == 3 or sum([board[0][0], board[1][0], board[2][0]]) == -3):
		return True
	# Middle Horizontal
	elif(sum([board[0][1], board[1][1], board[2][1]]) == 3 or sum([board[0][1], board[1][1], board[2][1]]) == -3):
		return True
	# Right Horizontal
	elif(sum([board[0][2], board[1][2], board[2][2]]) == 3 or sum([board[0][2], board[1][2], board[2][2]]) == -3):
		return True
	
	# Diagonal
	elif((board[0][0] + board[1][1] + board[2][2]) == 3 or (board[0][0] + board[1][1] + board[2][2]) == -3):
		return True
	# Diagonal
	elif((board[0][2] + board[1][1] + board[2][0]) == 3 or (board[0][2] + board[1][1] + board[2][0]) == -3):
		return True
	elif(not any(0 in sublist for sublist in board)):
		return True
	else:
		return False

def get_winner(board):
	# Will return 1 or 2 depending on who won
	for number in [-1, 1]:
		# Checks left vertical
		if(sum(board[0]) == number*3 ):
			return number
		# Middle Vertical
		elif(sum(board[1]) == number*3 ):
			return number
		# Right Vertical
		elif(sum(board[2]) == number*3):
			return number

		# Top Horizontal
		elif(sum([board[0][0], board[1][0], board[2][0]]) == number*3):
			return number
		# Middle Horizontal
		elif(sum([board[0][1], board[1][1], board[2][1]]) == number*3):
			return number
		# Right Horizontal
		elif(sum([board[0][2], board[1][2], board[2][2]]) == number*3):
			return number
		
		# Diagonal
		elif((board[0][0] + board[1][1] + board[2][2]) == number*3):
			return number
		# Diagonal
		elif((board[0][2] + board[1][1] + board[2][0]) == number*3):
			return number
	else:
		return 0


def get_best_move(board, bot_id):


	# Will evaluate each base move
	# For instance if there is currently 2 moves, will return a score for each move
	moves = get_list_moves(board)

	for key, values in moves.iteritems():
		total_score = 0
		dummy_board = board
		xy = moves[key]
		x = xy[0]
		y = xy[1]

		dummy_board[x][y] = bot_id
		if(check_winner(dummy_board)):
			# Someone Won
			winner = get_winner(dummy_board)
			if(winner == bot_id):
				total_score += 1
			elif(winner == 0):
				total_score += 0
			else:
				total_score -= 1
		else:
			print board
			total_score += get_best_move_not_main(board, bot_id*-1, bot_id)

		print "Key: " + str(key) + " - move: " + str(xy) + " score: " + str(total_score) + "end"

def get_best_move_not_main(board, whosMove, bot_id):
	# Will evaluate each base move
	# For instance if there is currently 2 moves, will return a score for each move
	moves = get_list_moves(board)
	total_score = 0

	for key, values in moves.iteritems():
		
		dummy_board = board
		xy = moves[key]
		x = xy[0]
		y = xy[1]

		dummy_board[x][y] = whosMove

		if(check_winner(dummy_board)):
			# Someone Won
			winner = get_winner(dummy_board)
			if(winner == bot_id):
				total_score += 1
			elif(winner == 0):
				total_score += 0
			else:
				total_score -= 1
		else:
			total_score += get_best_move_not_main(board, whosMove*-1, bot_id)

	return total_score

def get_list_moves(board):
	moves = {}
	move_number = 1

	for x in [0,1,2]:
		for y in [0,1,2]:
			if(board[x][y] == 0):
				moves[move_number] = [x,y]
				move_number += 1
	return moves



board = [[0,0,0],[0,-1,-1],[0,0,0]]
game = tictactoe(board)

toMove = -1

# Runs while the game is not over
while(not check_winner(board)):
	
	# Defaults to the move entered being incorrect
	move = False
	
	while(not move):
		game.display_board()
		get_best_move(board, toMove)
		inputX = input("Enter X")
		inputY = input("Enter Y")
		move = game.move(inputX, inputY, toMove)
		board = game.board

	# Sets move to the other player
	toMove *= -1

print "Game Over"
print str(get_winner(board)) + "Won"