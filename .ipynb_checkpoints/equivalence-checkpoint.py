class Equivalence:

		def __init__(self):
			self.parent = {}

		def add(self, a, b):
			self.addSingleton(a)
			self.addSingleton(b)
			self.merge(a, b)

		def addSingleton(self, a):
			if a not in self.parent:
				self.parent[a] = a

		def merge(self, a, b):
			self.parent[self.root(a)] = self.root(b)

		def check(self, a, b):
			return self.root(a) == self.root(b)

		def root(self, a):
			while True:
				pa = self.parent[a]
				if pa == a:
					break
				a = pa
			return a

		def classes(self):
			res = {}
			for element in self.parent:
				res.setdefault(self.root(element), set())
				res[self.root(element)].add(element)
				res[self.root(element)].add(self.root(element))
			return res