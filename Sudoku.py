# Python program for the above approach

# Grid dimension

N = 2

# Function to check if the number to be present

# in the current cell is safe or not

def issafe(sudoku, i, j, n, number, region):

	# Check if the number is present in	# i-th row or j-th column or not

	for x in range(n):

		if (sudoku[x][j] == number or sudoku[i][x] == number):

			return False

	# Check if the number to be filled

	# is safe in current region or not

	r = region[i][j]

	# Initialize the queue for the BFS

	q = []

	# Insert the current cell into queue

	q.append([i, j])

	# Check if the neighbours cell is

	# visited or not

	visited = [[0 for i in range(N)]for j in range(N)]

	# Mark current cell is visited

	visited[i][j] = 1

	# Performing the BFS technique

	# Checking for 4 neighbours at a time

	while (len(q)>0):

		# Stores front element of the queue

		front = q[0]

		# Pop top element of the queue

		q.pop()

		# Check for neighbours cell

		if (front[0] + 1 < N and region[front[0] + 1][front[1]] == r and visited[front[0] + 1][front[1]] == 0):

			# If already contains the same number

			if (sudoku[front[0] + 1][front[1]] == number):

				return False

				

			q.append([front[0] + 1, front[1]])

			# Mark as neighbour cell as visited

			visited[front[0] + 1][front[1]] = 1

		# Checking for 2nd neighbours

		if(front[0] - 1 >= 0 and region[front[0] - 1][front[1]] == r and visited[front[0] - 1][front[1]] == 0):

			# If neighbours contains the same number

			if (sudoku[front[0] - 1][front[1]] == number):

				return False

			# Insert neighbour cell into queue

			q.append([front[0] - 1, front[1]])

			# Mark neighbour cell as visited

			visited[front[0] - 1][front[1]] = 1

		# Checking for 3rd neighbours

		if ( front[1] + 1 < N and region[front[0]][front[1] + 1] == r and visited[front[0]][front[1] + 1] == 0):

			# If neighbours contains the same number

			if (sudoku[front[0]][front[1] + 1] == number):

				return False

			# Insert neighbour cell into queue

			q.append([front[0], front[1] + 1])

			# Mark neighbour cell as visited

			visited[front[0]][front[1] + 1] = 1

		# Checking for 4th neighbours

		if (front[1] - 1 >= 0 and region[front[0]][front[1] - 1] == r and visited[front[0]][front[1] - 1] == 0):

			# If neighbours contains the same number

			if (sudoku[front[0]][front[1] - 1] == number):

				return False

			# Insert neighbour cell into queue

			q.append([front[0], front[1] - 1])

			# Mark neighbour cell as visited

			visited[front[0]][front[1] - 1] = 1

	return True

# Recursive function to solve the sudoku

def solveSudoku(sudoku, i, j, n, region):

	# If the given sudoku already solved

	if (i == n):

		# Print the solution of sudoku

		for a in range(n):

			for b in range(n):

				print(sudoku[a][b],end = " ")

			print()

		return True

	# If the numbers in the current row

	# already filled

	if (j == n):

		return solveSudoku(sudoku, i + 1, 0, n, region)

	# If current cell is not empty

	if (sudoku[i][j] != 0):

		return solveSudoku(sudoku, i, j + 1, n, region)

	else:

		#Iterate over all possible value of numbers

		for number in range(1,n+1):

			# If placing the current number is safe

			# in the current cell

			if (issafe(sudoku, i, j, n, number, region)):

				# Update sudoku[i][j]

				sudoku[i][j] = number

				# Fill the remaining cells of the sudoku

				rest = solveSudoku(sudoku, i, j + 1, n, region)

				# If remaining cells has been filled

				if (rest == True):

					return True

	# Otherwise No Solution

	sudoku[i][j] = 0

	return False

# Driver Code

# Given sudoku array

sudoku = [

[0, 1],

[0, 0],

]

# Given region array

region = [

["r", "r"],

["b", "b"],

]

# Function call

ans = solveSudoku(sudoku, 0, 0, N, region)

# No answer exist

if (ans == 0):

	print("-1")

# This code is contributed by shinjanpatra
