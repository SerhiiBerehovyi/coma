def tomtx(str):
	"""
		help function

		@input: string in form " 1 2 3, 4 5 6"
		@output: array[][] in form
			[	[1,2,3]
				[4,5,6] ]
	"""
	matrix = []
	s = str.split(',')
	for i in s:
		k = i.split()
		matrix.append(k)


	return matrix

def tostr(m):
	"""
		help function

		@input: array[][] in form
			[	[1,2,3]
				[4,5,6] ]
		@output: string in form " 1 2 3, 4 5 6"
	"""
	s = ''
	for a in m:
		for b in a:
			s += ' ' + str(b)
		s += ','

	return s[1:-1] # because s = " 1 2 3, 4 5 6,"


def multiply(A,B):
	""" 
		multiplies two matrices and returns a product
		uses two help-functions: 
			tomtx() - to convert strings to arrays[][]
			tostr()	- to convert arrays[][] to strings

		@input: two strings in form " 1 2 3, 4 5 6"
		@output: string whith product in form " 1 2 3, 4 5 6"
	"""
	A = tomtx(A)
	B = tomtx(B)
	
	matrix = [] # product
	for i in range(len(A)):
		line = [] 
		for j in range(len(B[0])):
			c = min(int(A[i][k]) + int(B[k][j]) for k in range(len(A[0])))
			# c is an element whith index [i][j] in line
			line.append(c)
		matrix.append(line)

	output = tostr(matrix)

	return output

def power(A, n):
	""" 
		multiplies A whith A n time.
		calls multiply() to calculate a power

		@input: A is a string in form " 1 2 3, 4 5 6"
				n is an integer
		@output: multiplied A in form " 1 2 3, 4 5 6"
	"""
	N = A # save the original A
	while n > 1:
		A = multiply(A,N)
		n -= 1

	return A
