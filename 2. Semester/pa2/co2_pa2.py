class MaxHeap:
	"""
		realisation of datastructure Max Heap realized as an array.
		with one attribute keys.
	"""
	def __init__(self, keys):
		"""
			initial MaxHeap with an array.
			:keys: array, that must be saved as nodes of Max Heap
		"""
		self.keys = keys.copy()
		self.build_max_heap()

	def maximum(self):
		"""
			maximal node aufter hepify is at keys[0]
		"""
		return self.keys[0]

	def extractMax(self):
		"""
			removers and returns maximal value and build max heap relationship
		"""
		val = self.keys.pop(0)
		self.build_max_heap()
		return val

	def increaseKey(self, i, k):
		"""
			increases key on i-position by k and builds 
			max heap relationship
			returns string "k too small" if value in i-position is bigger than k
			:i: index to increase
			:k: new value of node
		"""
		if k < self.keys[i]:
			return "k too small"
		self.keys[i] = k
		while i > 0 and self.keys[(i-1)//2] < self.keys[i]:
			self.keys[(i-1)//2], self.keys[i] = self.keys[i], self.keys[(i-1)//2]
			i = (i-1)//2

	def insert(self, k):
		"""
			inserts k with saving max heap relationship
			:k: new value to insert
		"""
		n = len(self.keys)
		self.keys.append(-999999999) # -infinity
		self.increaseKey(n, k)

	def heapSort(self):
		"""
			sorts self.keys in ascending order and returns a copy of sorted list
			uses reverce() to build max heap relationship again
		"""
		n = len(self.keys) - 1
		while n > 0:
			self.keys[0], self.keys[n] = self.keys[n], self.keys[0]
			self.heapify(0, n)
			n -= 1
		arr = self.keys.copy()
		self.keys.reverse()
		return arr


	def build_max_heap(self):
		"""
			buids max heap relationship in array self.keys
		"""
		n = len(self.keys)
		for i in range(n // 2, -1, -1):
			self.heapify(i, n)

	def heapify(self, i, n):
		"""
			builds max heap relationship for all child-nodes of i-th element
			:i: index of element to buil max heap relationship
			:n: lenth of self.array
		"""
		l = 2 * i + 1
		r = 2 * i + 2
		largest = i
		if l < n and self.keys[l] > self.keys[i]:
			largest = l

		if r < n and self.keys[r] > self.keys[largest]:
			largest = r

		if largest != i:
			self.keys[largest], self.keys[i] = self.keys[i], self.keys[largest]
			self.heapify(largest, n)
