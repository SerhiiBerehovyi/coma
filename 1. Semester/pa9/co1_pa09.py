ob = "{(["
cb = "})]"
op = "+*"
nums = "0123456789"

def tiefe(string):
	counters = []
	count = 0
	for ch in string:
		if ch in ob:
			count += 1
		if ch in cb:
			counters.append(count)
			count -= 1
	if counters:
		return max(counters)
	return 0

def is_valid(st):
	def brackets(bstart='([{', bend=')]}'):
		dt = dict.fromkeys(range(len(bend)), 0)
		for s in st:
			if s in bstart:
				dt[bstart.index(s)] += 1
			elif s in bend:
				i = bend.index(s)
				dt[i] -= 1
				if dt[i] < 0:
					return
		return not any(dt.values())

	if brackets():
		return True
	raise Exception('syntaktisch inkorrekt') 
	
def parse(str):
	arr = []
	i = 0
	while i < len(str):
		if str[i].isalpha()or str[i] in "-_/' .!@#$%^&=|\\><:;\"":
			raise Exception('syntaktisch inkorrekt')  
		# elif str[i].isspace():
		# 	i += 1
		elif str[i].isdigit():
			num = ""
			while i < len(str) and str[i].isdigit():
				num += str[i]
				i += 1
			arr.append(num)
		else:
			if str[i] in ob+op+cb:
				arr.append(str[i])
				i += 1
	arr.append('=')
	return arr

def calculate(term):
	term = parse(term)
	def get():
		t = term[get.i]
		if get.i < len(term)-1:
			get.i += 1
		return t

	get.i = 0

	def primary():
		t = get()
		if t.isdigit():
			return int(t)
		elif t in ob:
			d = expression()
			t = get()
			next = get()
			if t in cb and next.isdigit():
				raise Exception('syntaktisch inkorrekt') 
			get.i -= 1
			return d
		else:
			raise Exception('syntaktisch inkorrekt') 

	def multiply():
		left = primary()
		token = get()
		while True:
			if token == '*':
				left *= primary()
				token = get()
			else:
				if token in ob:
					raise Exception('syntaktisch inkorrekt') 
				get.i -= 1
				return left

	def expression():
		left = multiply()
		token = get()
		while True:
			if token == '+':
				left += multiply()
				token = get()
			else:
				get.i -= 1
				return left

	return expression()

def evaluate(string):
	is_valid(string)
	v = calculate(string)
	t = tiefe(string)
	return (v,t)

def eval_depth0(n):
	return calculate(n)
