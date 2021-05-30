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

def unitmtx_generate(n):
	"""
		help function
		
		@input: an integer n
		@output: unit matrix nxn
	"""
	unit = []  # unit matrix
	for i in range(n):
		arr = [] # to save all elems 
		for j in range(n):
			if i == j:
				arr.append(1)
			else:
				arr.append(0)
		unit.append(arr)

	return unit

def is_zero_mtx(mtx,r,n):
	"""
		help function, used to check if mtx[r+1][r+1] to mtx[n][n]
		a zero matrix is

		@input: mtx to check, r, n - indexes
		@output: true, if part of mtx is a zero matrix
				 false, if there is a integer != 0
	"""
	for i in range(r+1, n):
		for j in range(r+1, n):
			if mtx[i][j] != 0:
				return False
	return True

def pq_find(mtx, r, n):
	"""
		help function, used to find first element != 0

		@input: mtx to search, r,n - indexes to search between
		@output: indexes p,q of first element != 0
	"""
	p = q = r
	while p in range(r,n):
		while q in range(r,n):
			if mtx[p][q] != 0:
				return p,q
			q += 1
		q += 1

def swap_column(mtx, p, q):
	"""
		help fucntion to swap the columns in mtx

		@input: mtx - matrix, p and q - columns to swap
	"""
	for i in mtx:
		i[p], i[q] = i[q], i[p]


def LU_decomposition(s):
	"""
		function to LU decompose of matrix s

		@input: matrix nxn in form "1 2 3, 4 5 6, 7 8 9"
		@output: decomposed matrix in input-form
				output matrix is superimposition of L-matrix and U-matrix
				for each element on ij position and i > j: U[i][j] = L[i][j]
	"""
	A = tomtx(s) # convert from str to [][]
	n = len(A)
	U = A
	L = unitmtx_generate(n)	
	Pz = unitmtx_generate(n)
	Ps = unitmtx_generate(n)
	r = 0

	while not is_zero_mtx(U,r,n) and r < n:
		p, q = pq_find(U, r, n)

		if p != r:
			U[p], U[r] = U[r], U[p]
			L[p], L[r] = L[r], L[p]
			swap_column(L, p, r)
			Pz[p], Pz[r] = Pz[r], Pz[p]

		if q != r:
			swap_column(L, q, r)
			swap_column(Ps, q, r)

		for i in range(r+1, n):
			L[i][r] = int(U[i][r]) / int(U[r][r])
			for j in range(r, n):
				U[i][j] = int(U[i][j]) - int(L[i][r])*int(U[r][j])
		r += 1

	# superimposition of L and U
	for i in range(n):
		for j in range(n):
			if i > j:
				U[i][j] = int(L[i][j])

	return tostr(U)
	