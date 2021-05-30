"""
	Script, der den kleinsten quadratischen Abstand von 
	gegebenen Geraden zu einer gegebenen Punktmenge.

	Beispiel:
	>>> linear_regression([(-1,1),(0,2),(1,1),(3,-1)],[(1,1)])
	28
	>>> linear_regression([(-1,1),(0,2),(1,1),(3,-1)],[(-1,2)])
	4
	>>> linear_regression([(-1,1),(0,2),(1,1),(3,-1)],[(1,1),(-1,2)])
	4
"""

def get_min(int_list):
	"""
	gibt die kleinste Wert aus int_list zuruek.
	falls int_list leer ist, -> return None
	"""
	if len(int_list) != 0:
		return min(int_list)
	else:
		return None

def get_linedistance(points,line):
	"""
	Berechnet und gibt den quadratischen Abstand summ von gegebenen 
	Geraden line und zu einer gegebenen Punktmenge points zuruek.
	"""
	summ = 0
	for p in points:
		summ += (line[0]*p[0] + line[1] - p[1])**2
	return summ

def linear_regression(points,lines):
	"""
	Sammelt quadratische Abstaende von jede line in lines zu 
	Punktmenge points in int_list.
	Aufrufe:
		get_linedistance() um quadratischen Abstand zu berechnen
		get_min() um das Minimun in int_list zu finden und zuruekzugeben.
	""" 
	int_list = []
	for line in lines:
		int_list.append(get_linedistance(points, line))

	return get_min(int_list)