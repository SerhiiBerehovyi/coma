#!/usr/bin/python3

from math import sqrt

def new_arr(n):
	arr = [True] * (n+1)
	arr[0] = arr[1] = False
	return arr

def sieve(n):
	if n < 2:
		return None
	arr = new_arr(n)

	for i in range(2, int(sqrt(n) + 1)):
		if arr[i]:
			for j in range(i**2, n+1, i):
				arr[j] = False

	output = []
	for i in range(2, n+1):
		if arr[i] == True:
			output.append(i)
	
	return output

def isprime(n):
	if n < 2:
		return None

	prime = sieve(n)

	if n in prime:
		return True
	else:
		return False

def factorization(n):
	if n < 2:
		return None

	if n < 4:
		faktoren = sieve(n)
	else:
		m = n//2
		faktoren = sieve(m)

	output = []

	for p in faktoren:
		if n%p == 0:
			faktor = [p]
			k = 1 
			while n % p**(k+1) == 0:
				k += 1

			faktor.append(k) 
			output.append(faktor)

	if len(output) == 0:
		faktor = [n,1]
		output.append(faktor)

	return output

def divisornumber(n):
	if n < 1:
		return None
	if n == 1:
		return 1

	faktors = factorization(n)

	teilerzahl = 1
	for i in faktors:
		teilerzahl *= i[1] + 1

	return teilerzahl


def iscoprime(n,m):
	if n < 1 or m < 1:
		return None

	n_dev = factorization(n)
	m_dev = factorization(m)

	flag = True
	if n_dev and m_dev:
		for i in n_dev:
			for j in m_dev:
				if i[0] == j[0]:
					flag = False
					break
	return flag
