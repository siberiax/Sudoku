
Sudoku = [[0 for x in range(9)] for y in range(9)]

GivenValues = [[False for x in range(9)] for y in range(9)] 

#solve the puzzle
def solvePuzzle():
	spot = 0
	moveon = 1
	while spot < 81:
		row = int(spot/9)
		col = spot % 9	
		if (GivenValues[row][col]):
			if (moveon):
				spot += 1
			else:
				spot -= 1
		else:
			num = Sudoku[row][col]
			prev = Sudoku[row][col]
			while(num < 9):
				if (num < 9):
					num += 1
				res = checkBoard(row, col, num)
				if (res == 1):
					Sudoku[row][col] = num
					moveon = 1
					break
			if (Sudoku[row][col] == prev):
				Sudoku[row][col] = 0
				moveon = 0
			if moveon:
				spot += 1
			else:
				spot -= 1

#check if board is valid
def checkBoard(row, col, start):
	for y in range(9):
		if (Sudoku[row][y] == start):
			return 0
	for x in range(9):
		if (Sudoku[x][col] == start):
			return 0
	if (row >= 0 and row <= 2 and col >= 0 and col <= 2):
		for x in range(3):
			for y in range(3):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 0 and row <= 2 and col >= 3 and col <= 5):
		for x in range(3):
			for y in range(3,6):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 0 and row <= 2 and col >= 6 and col <= 8):
		for x in range(3):
			for y in range(6,9):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 3 and row <= 5 and col >= 0 and col <= 2):
		for x in range(3,6):
			for y in range(3):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 3 and row <= 5 and col >= 3 and col <= 5):
		for x in range(3,6):
			for y in range(3,6):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 3 and row <= 5 and col >= 6 and col <= 8):
		for x in range(3,6):
			for y in range(6,8):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 6 and row <= 8 and col >= 0 and col <= 2):
		for x in range(6,9):
			for y in range(3):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 6 and row <= 8 and col >= 3 and col <= 5):
		for x in range(6,9):
			for y in range(3,6):
				if (Sudoku[x][y] == start):
					return 0
	if (row >= 6 and row <= 8 and col >= 6 and col <= 8):
		for x in range(6,9):
			for y in range(6,9):
				if (Sudoku[x][y] == start):
					return 0
	return 1

#read the input board
def readBoard(filename):
	x = 0
	for line in open (filename):
		y = 0
		while (y < 9):
			value = int(line[y])
			if (value != 0):
				Sudoku[x][y] = value
				GivenValues[x][y] = True
			y += 1
		x += 1

#print the board
def printBoard():
	for x in range(9):
		if (x % 3 == 0 and x != 0):
			print("---|---|---")
		for y in range(9):
			if (y % 3 == 0 and y != 0):
				print("|", end="")
			if (Sudoku[x][y] == 0):
				print(" ", end="")
			else:
				print (str(Sudoku[x][y]),end="")
		print()
	print()

def main():
	readBoard("config.txt")
	print("\nStart board")
	printBoard()
	solvePuzzle()
	print("\nSolution")
	printBoard()

main()
