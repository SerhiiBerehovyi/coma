#!/usr/bin/python3

def convert_to_standard(a1,a2,b1,b2) -> int:
	""" 
	return: a 4-Tuple (a1,a2,b1,b2),
	where a1,a2 a point in bottom left
	and b1,b2 a point in top right
	""" 
	if a1 <= b1 and a2 <= b2:
		t = (a1, a2, b1, b2)
	elif a1 <= b1 and a2 > b2:
		t = (a1, b2, b1, a2)
	elif a1 > b1 and a2 <= b2:
		t = (b1, a2, a1, b2)
	else:
		t = (b1, b2, a1, a2)
	return t

def intersects(h,a1,a2,b1,b2):
	""" 
	return: True, if intersection is not empty 
			and False if empty 
	"""
	right 	= min(b1,6)
	left 	= max(a1,0)
	top 	= min(b2,h)
	bottom 	= max(a2,0)

	width = right-left
	height = top - bottom

	if width < 0 or height < 0:
		return False
	else:
		return True


def get_delta_x1(a1,b1):
	return min(6,b1) - max(0,a1)

	
def get_delta_x2(h,a2,b2):
	return min(h,b2) - max(a2,0)

def get_lattice_point_number(h,a1,a2,b1,b2):
	answer= ''
	a1,a2,b1,b2 = convert_to_standard(a1,a2,b1,b2)

	if h < 0:
		answer = 'Die Eingabe ist fehlerhaft.'
	elif not intersects(h,a1,a2,b1,b2):
		answer = 'Der Schnitt der gegebenen Rechtecke ist leer.'
	else:
		punkte = (get_delta_x2(h,a2,b2)+1) * (get_delta_x1(a1,b1)+1)
		answer = 'Die Zahl der Gitterpunkte im resultierenden Rechteck betraegt {}.'
		answer = answer.format(punkte)
		

	return answer