from random import random
import copy

def updatePosition(n,m,pos,rnd):
	""" 
	we assume that the world rectangle has such coordinate nets. 

		0	1	2	3	...	  m-1
	0:	*	*	*	*	 *	   *
	1:	*	*	*	*	 *	   *
	... *	*	*	*	 *	   *
	n-1	*	*	*	*	 *	   *

	reshape pos in (x, y) form, then we change the pos depending
	on rnd and reshape in acceptance form. 
	"""

	pos_max = m*n

	x_min = 0
	y_min = 0
	x_max = m - 1
	y_max = n - 1

	if pos >= pos_max:
		if pos_max != 0:
			pos %= pos_max
		else:
			pos = 0

	x = pos % m 
	y = int((pos - x) / m)

	
	if rnd >= 0 and rnd < 0.25:
		if x == x_max:
			x = x_min
		else:
			x += 1

	elif rnd >= 0.25 and rnd < 0.5:
		if x == x_min:
			x = x_max
		else:
			x -= 1

	elif rnd >= 0.5 and rnd < 0.75:
		if y == y_max:
			y = y_min
		else:
			y += 1

	elif rnd >= 0.75 and rnd < 1:
		if y == y_min:
			y = y_max
		else:
			y -= 1

	# formen wir (x,y)-Form wieder in Annahme-Form:
	new_pos = m * y + x

	return new_pos

def updatePositions(n,m,positions):
	for pos in positions:
		rnd = random()
		new_pos = updatePosition(n,m, pos[1], rnd)
		pos[1] = new_pos

def sortPositions(positions):
	def sortByPos(pos):
		return pos[1]

	positions = positions.sort(key=sortByPos)

def extractSquare(positions):
	sortPositions(positions)
	square = []
	max = -1

	for i in reversed(range(len(positions))):
		if max == -1: max = positions[i][1]
		if positions[i][1] == max:
			square.append(positions.pop(-1))
		else:
			break

	return square

def giftExchange(square):
	# a)
	zh_flag = h_flag = False
	for sq in square:
		if sq[0] == 'H':
			h_flag = True
		if sq[0] == 'ZH':
			zh_flag = True

	if zh_flag and h_flag:
		for sq in square:
			if sq[0] == 'H':
				sq[0] = 'HH'

	# b)
	znum = hnum = 0
	for sq in square:
		if sq[0] == "Z":
			znum += 1
		if sq[0] == "HH":
			hnum += 1

	if znum >= 2*hnum:
		for sq in square:
			if sq[0] == "H" or sq[0] == "HH":
				sq[0] = "Z"
	else:
		for sq in square:
			if sq[0] == "Z":
				sq[0] = "ZH"

def christmasFated(positions):
	h = False
	z = False
	for pos in positions:
		if pos[0] == 'H' or pos[0] == 'HH':
			h = True
		elif pos[0] == 'Z':
			z = True

	if not h:
		return True
	elif not z:
		return True
	else:
		return False
		

def mergeSquare(square,intermediate):
	intermediate += square
	square.clear()

def christmasFate(positions):
	h = hh = zh = False
	for pos in positions:
		if pos[0] == "H":
			h = True
		elif pos[0] == "HH":
			hh = True
		elif pos[0] == "ZH":
			zh = True

	if h or hh:
		return 'Ho, ho, ho, and a merry Zombie-Christmas!'
	else:
		return 'Zombies ate my Christmas!'

def zombieChristmas(n,m,positions):
	while not christmasFated(positions):
		updatePositions(n,m,positions)
		intermediate = []
		while len(positions):
			square = extractSquare(positions)
			giftExchange(square)
			mergeSquare(square, intermediate)
		positions = copy.copy(intermediate)
		intermediate.clear()

	print(christmasFate(positions))