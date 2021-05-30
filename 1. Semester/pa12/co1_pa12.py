def maxunimod(L):
	"""
		function finds max len of all unimodular 
		sequences of numbers

		uses unimod function to find next
		unimodular sequence and saves len
		of it in unimods[]. returns max(unimods)

		@input: sequence of numbers L
		@output: len of sequence with max len

	"""
	if len(L) <= 1:
		return len(L)
	unimods = []
	start = i = 0	# start and end of unimodular sequence
	while i < len(L):
		i = unimod(L,i)
		unimods.append(len(L[start:i]))
		if i != len(L):
		 	i = if_repeat(L,i) 
		start = i - 1	# refresh start for next itaration
	return max(unimods)

def unimod(L, start):
	"""
		help-function used to find index of last element
		in unimodular sequence
			( a_1 <= a_2 <= *** <= a_i >= a_i+1 >= *** >= a_d )

		@input: sequence of numbers L
		@output: index of last elemet in sequence
	"""
	i = start + 1
	# find  ( a_1 <= a_2 <= *** <= a_i ) part
	while i < len(L) and L[i] >= L[i-1]:
		i += 1
	# find ( a_i+1 >= *** >= a_d ) part
	while i < len(L) and L[i] <= L[i-1]:
		i += 1
	return i

def if_repeat(L, i):
	# if a_d == a_d-1 == *** == a_x 
	# we must to find a_x
	while i > 0 and L[i-1] == L[i-2]:
		i -= 1
	return i
