class TicTacToe:
	def __init__(self):
		self.board = [" " for _ in range(9)] #we will use a single list to represent a 3x3 board
		self.current_winner = None

	def print_board(self):
		for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
			print("| " + " | ".join(row) + " |") #the first | is for the left border, the second substitutes the values in the row, and the last | is for the right border

	@staticmethod
	def print_board_nums():
		# 0 | 1 | 2 etc (tells us what number corresponds to what box)
		number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
		for row in number_board:
			print("| " + " | ".join(row) + " |")

	def available_moves(self):
		moves = []
		for (i,x) in enumerate(self.board):
			# ["x, "x", "o"] --> [(0, "x"), (1, "x"), (2, "o")]
			if x == " ":
				moves.append(i)
		return moves

	def empty_squares(self):
		return " " in self.board #returns boolean

	def num_empty_squares(self):
		return len(self.board.count(" "))

	def make_move(self, square, letter):
		#if valid move, then make the move (assign square to letter)
		#if invalid, return false
		if self.board[square] == " ":
			self.board[square] = letter
			if self.winner(square, letter):
				self.current_winner = letter
			return True
		return False

	def winner(self, square, letter):
		#winner if 3 in a row anywhere.. we have to check all of these!
		row_ind = square // 3
		row = self.board[row_ind*3:(row_ind+1)*3]
		if all([spot == letter for spot in row]):
			return True

		#check column
		col_ind = square % 3
		column = [self.board[col_ind+i*3] for i in range(3)]
		if all([spot == letter for spot in column]):
			return True
			

		

def play(game, x_player, o_player, print_game=True):
	if print_game:
		game.print_board_nums()

	letter = "x" #starting letter
	#iterate while the game still has empty squares
	#we don't have to worry about winner because we'll just return that which breaks the loop
	while game.empty_squares():
		if letter == "o":
			square = o_player.get_move(game)
		else:
			square = x_player.get_move(game)
	
		if game.make_move(square, letter):
			if print_game:
				print(letter + f" Makes a move to square {square}")
				game.print_board()
				print("") #just empty line

			if game.current_winner:
				if print_game:
					print(letter + " Wins!")
				return letter 

			#after we made our move, we need to alternate letters
			letter = "o" if letter == "x" else "x" 
			# if letter == "x":
			# 	letter = "o"
			# else:
			# 	letter = "x"
		
		if print_game:
			print("It's a tie!")