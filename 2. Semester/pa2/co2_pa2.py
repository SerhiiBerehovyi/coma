class MaxHeap:
	def __init__(self, keys):
		self.keys = keys.copy()
		self.build_max_heap()

	def maximum(self):
		return self.keys[0]

	def extractMax(self):
		val = self.keys.pop(0)
		self.build_max_heap()
		return val

	def increaseKey(self, i, k):
		if k < self.keys[i]:
			return "k too small"
		self.keys[i] = k
		while i > 0 and self.keys[(i-1)//2] < self.keys[i]:
			self.keys[(i-1)//2], self.keys[i] = self.keys[i], self.keys[(i-1)//2]
			i = (i-1)//2

	def insert(self, k):
		n = len(self.keys)
		self.keys.append(-999999999) # -infinity
		self.increaseKey(n, k)

	def heapSort(self):
		n = len(self.keys) - 1
		while n > 0:
			self.keys[0], self.keys[n] = self.keys[n], self.keys[0]
			self.heapify(0, n)
			n -= 1
		arr = self.keys.copy()
		self.keys.reverse()
		return arr


	def build_max_heap(self):
		n = len(self.keys)
		for i in range(n // 2, -1, -1):
			self.heapify(i, n)

	def heapify(self, i, n):
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
