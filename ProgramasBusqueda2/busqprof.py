class Vertice:
	# constructor
	def __init__(self, i):
		self.id = i
		self.visitado = False
		self.padre = None
		self.vecinos = []

	def agregarVecino(self, v):
		if v not in self.vecinos:
			self.vecinos.append(v)

# clase que define a una gráfica
class Grafica:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self, v):
		if v not in self.vertices:
			self.vertices[v] = Vertice(v)

	def agregarArista(self, a, b):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b)
			self.vertices[b].agregarVecino(a)

	def dfs(self, r):
		self.vertices[r].visitado = True

		for v in self.vertices[r].vecinos:
			if self.vertices[v].visitado == False:
				self.vertices[v].padre = r
				print("(" + str(v) + ", " + str(r) + ")")
				self.dfs(v)

def Main():
	g = Grafica()

	# lista de vértices 
	l = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14]
	for n in l:
		g.agregarVertice(n)

	# lista de aristas. Cada par de numeros es una arista (union entre dos vértices)
	l = [1,2, 1,3, 1,4, 1,5, 1,6, 1,7, 1,8, 1,9, 1,10, 1,11, 1,12, 1,13, 1,14, 2,3, 2,4, 2,5, 2,6, 2,7, 2,8, 2,9, 2,10, 2,11, 2,12, 2,13, 2,14, 3,4, 3,5, 3,6, 3,7, 3,8, 3,9, 3,10, 3,11, 3,12, 3,13, 3,14, 4,5, 4,6, 4,7, 4,8, 4,9, 4,10, 4,11, 4,12, 4,13, 4,14, 5,6, 5,7, 5,8, 5,9, 5,10, 5,11, 5,12, 5,13, 5,14, 6,7, 6,8, 6,9, 6,10, 6,11, 6,12, 6,13, 6,14, 7,8, 7,9, 7,10, 7,11, 7,12, 7,13, 7,14, 8,9, 8,10, 8,11, 8,12, 8,13, 8,14, 9,10, 9,11, 9,12, 9,13, 9,14, 10,11, 10,12, 10,13, 10,14, 11,12, 11,13, 11,14, 12,13, 12,14, 13,14 ]
	for i in range(1, len(l) -1, 2):
		g.agregarArista(l[i], l[i + 1])

	for v in g.vertices:
		print(v, g.vertices[v].vecinos)

	print("\n\n")

	g.dfs(2)

Main()