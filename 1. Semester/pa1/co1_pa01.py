#!/usr/bin/python3


def roots(a,b,c,d,e,f):
	# c5 - Coefitient for h
	c5 = 1
	# Coefitients for f*g
	c4 = a*d
	c3 = a*e + b*d 
	c2 = a*f + b*e + c*d 
	c1 = b*f + c*e 
	c0 = c*f

	koef = [c5,c4,c3,c2,c1,c0]

	# the number of sign changes
	wechsel = 0 

	#flag for c5, true, because c5 > 0 
	flag = True 

	for i in koef:
		if flag and i < 0:
			flag = False
			wechsel += 1
		elif not flag and i > 0: 
			flag = True
			wechsel += 1

	output = 'Das Polynom hat eine {}gerade Anzahl von positiven reellen Wurzeln.'
	
	return output.format('un' if wechsel % 2 != 0 else '')
