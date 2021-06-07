def are_disjoint(list1,list2):
	"""
	setzt eine Variable flag und pruefft ob jeden element in list1
	auch in list2 enthalten ist. wenn ja, dann setzen wir flag als 
	False und unterbrechen den Zyklus.
	"""
	flag = True
	for i in list1:
		for j in list2:
			if i == j:
				flag = False
				break
	return flag

def are_equal(list1,list2):
	"""
	analog zu are_disjoint(), aber wenn Element aus list1 nicht in 
	list2 enthalten ist, dann dann setzen wir flag als 
	False und unterbrechen den Zyklus.
	"""
	flag = True
	if len(list1) != len(list2):
		flag = False
	else:
		for i in list1:
			if i not in list2:
				flag = False
				break

	return flag

def get_classes(n,E):
	"""
	erstellen eine V variable und fuellen wir sie mit natuerlichen
	Zahlen {0, ..., n-1} aus. erstellen wir L und fuellen wir sie mit
	Aequivalenzklassen aus.
	"""
	V = [k for k in range(n)]
	L=[[v] for v in V]
	for e in E:
		L[e[0]].append(e[1]) #index 5
	return L

def get_eqclasses(n,E):

	L = get_classes(n,E)

	#sortieren wir jede Aequivalenzklasse
	for i in range(n):
		L[i].sort()
	
	# prueffen, ob L die Menge Aequivalenzrelation beschreibt
	# wenn nicht, geben wir ein leeres List zurueck
	for i in range(n):
		for j in range(i+1,n):
			if not set(L[i]).isdisjoint(L[j]) and L[i]!=L[j]:
				return []

	# entfernen wir die Dubletten unter den Aequivalenzklassen 
	L.sort()
	last_first_index=-1
	equivalence_classes=[]

	for i in range(n):
		if L[i][0]!=last_first_index:
			equivalence_classes.append(L[i])
			last_first_index=L[i][0]
	
	return equivalence_classes