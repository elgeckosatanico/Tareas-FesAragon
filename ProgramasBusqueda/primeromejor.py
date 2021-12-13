import math

class Vertice:
	"""Clase que define los vértices de los gráficas"""
	def __init__(self, i):
		"""Método que inicializa el vértice con sus atributos
		id = identificador
		vecinos = lista de los vértices con los que está conectado por una arista
		visitado = flag para saber si fue visitado o no
		padre = vértice visitado un paso antes
		costo = valor que tiene recorrerlo"""
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')

	def agregarVecino(self, v, p):
		"""Método que agrega los vertices que se encuentre conectados por una arista a la lista de vecinos 
		de un vertice, revisando si éste aún no se encuentra en la lista de vecinos"""
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Grafica:
	"""Clase que define los vértices de las gráficas"""
	def __init__(self):
		"""vertices = diccionario con los vertices de la grafica"""
		self.vertices = {}

	def agregarVertice(self, id):
		"""Método que agrega vértices, recibiendo el índice y la heuristica (para A* puede que no se reciba) revisando si éste no existe en el diccionario
		de vértices"""
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, a, b, p):
		"""Método que agrega aristas, recibiendo el índice de dos vertices y revisando si existen estos en la lista
		de vertices, además de recibir el peso de la arista , el cual se asigna a ambos vértices por medio del método
		agregar vecino"""
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		"""Método que imprime el gráfo completo arista por arista con todas sus características(incluye heurística)"""
		for v in self.vertices:
			print("El costo del vértice "+str(self.vertices[v].id)+" es "+ str(self.vertices[v].costo)+" llegando desde "+str(self.vertices[v].padre))
			
	
	def camino(self, a, b):
		"""Método que va guardando en la lista llamada 'camino' los nodos en el orden que sean visitados y actualizando dicha
		lista con los vértices con el menor costo"""
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)
			actual = self.vertices[actual].padre
		return [camino, self.vertices[b].costo]

	def minimo(self, l):
		"""Método que recibe la lista de los vertices no visitados, revisa si su longitud es mayor a cero(indica que 
		aún hay vértices sin visitar), y realiza comparaciones de los costos de cada vértice en ésta lista para encontrar
		el de menor costo"""
		if len(l) > 0:
			m = self.vertices[l[0]].costo
			v = l[0]
			for e in l:
				if m > self.vertices[e].costo:
					m = self.vertices[e].costo
					v = e
			return v
		return None

	def dijkstra(self, a):
		"""Método que sigue el algortimo de Dijkstra
		1. Asignar a cada nodo una distancia tentativa: 0 para el nodo inicial e infinito para todos los nodos restantes. Predecesor nulo para todos.
		2. Establecer al nodo inicial como nodo actual y crear un conjunto de nodos no visitados.
		3. Para el nodo actual, considerar a todos sus vecinos no visitados con peso w.
			a) Si la distancia del nodo actual sumada al peso w es menor que la distancia tentativa actual de ese vecino,
			sobreescribir la distancia con la suma obtenida y guardar al nodo actual como predecesor del vecino
		4. Cuando se termina de revisar a todos los vecino del nodo actual, se marca como visitado y se elimina del conjunto no  visitado
		5. Continúa la ejecución hasta vaciar al conjunto no visitado
		6. Seleccionar el nodo no visitado con menor distancia tentativa y marcarlo como el nuevo nodo actual. Regresar al punto 3
		"""
		if a in self.vertices:
			# 1 y 2
			self.vertices[a].costo = 0
			actual = a
			noVisitados = []
			
			for v in self.vertices:
				if v != a:
					self.vertices[v].costo = float('inf')
				self.vertices[v].padre = None
				noVisitados.append(v)

			while len(noVisitados) > 0:
				#3
				for vec in self.vertices[actual].vecinos:
					if self.vertices[vec[0]].visitado == False:
						# 3.a
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
							self.vertices[vec[0]].padre = actual

				# 4
				self.vertices[actual].visitado = True
				noVisitados.remove(actual)

				# 5 y 6
				actual = self.minimo(noVisitados)
		else:
			return False

class main:
	g = Grafica()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarVertice(7)
	g.agregarVertice(8)
	g.agregarVertice(9)
	g.agregarVertice(10)
	g.agregarVertice(11)
	g.agregarVertice(12)
	g.agregarVertice(13)
	g.agregarVertice(14)
	"""g.agregarVertice(15)
	g.agregarVertice(16)
	g.agregarVertice(17)
	g.agregarVertice(18)
	g.agregarVertice(19)
	g.agregarVertice(20)
	g.agregarVertice(21)
	g.agregarVertice(22)
	g.agregarVertice(23)
	g.agregarVertice(24)
	g.agregarVertice(25)
	g.agregarVertice(26)
	g.agregarVertice(27)
	g.agregarVertice(28)"""
	g.agregarArista(2, 1, 908)
	g.agregarArista(3, 1, 117)
	g.agregarArista(3, 2, 515)
	g.agregarArista(4, 1, 687)
	g.agregarArista(4, 2, 448)
	g.agregarArista(4, 3, 886)
	g.agregarArista(5, 1, 1651)
	g.agregarArista(5, 2, 970)
	g.agregarArista(5, 3, 1373)
	g.agregarArista(5, 4, 922)
	g.agregarArista(6, 1, 117)
	g.agregarArista(6, 2, 791)
	g.agregarArista(6, 3, 999)
	g.agregarArista(6, 4, 804)
	g.agregarArista(6, 5, 1540)
	g.agregarArista(7, 1, 1882)
	g.agregarArista(7, 2, 1013)
	g.agregarArista(7, 3, 117)
	g.agregarArista(7, 4, 1404)
	g.agregarArista(7, 5, 1191)
	g.agregarArista(7, 6, 1765)
	g.agregarArista(8, 1, 1310)
	g.agregarArista(8, 2, 441)
	g.agregarArista(8, 3, 844)
	g.agregarArista(8, 4, 832)
	g.agregarArista(8, 5, 529)
	g.agregarArista(8, 6, 1193)
	g.agregarArista(8, 7, 662)
	g.agregarArista(9, 1, 889)
	g.agregarArista(9, 2, 246)
	g.agregarArista(9, 3, 684)
	g.agregarArista(9, 4, 202)
	g.agregarArista(9, 5, 720)
	g.agregarArista(9, 6, 840)
	g.agregarArista(9, 7, 1202)
	g.agregarArista(9, 8, 630)
	g.agregarArista(10, 1, 760)
	g.agregarArista(10, 2, 181)
	g.agregarArista(10, 3, 559)
	g.agregarArista(10, 4, 479)
	g.agregarArista(10, 5, 997)
	g.agregarArista(10, 6, 643)
	g.agregarArista(10, 7, 1194)
	g.agregarArista(10, 8, 622)
	g.agregarArista(10, 9, 277)
	g.agregarArista(11, 1, 2348)
	g.agregarArista(11, 2, 1707)
	g.agregarArista(11, 3, 1811)
	g.agregarArista(11, 4, 1619)
	g.agregarArista(11, 5, 697)
	g.agregarArista(11, 6, 2237)
	g.agregarArista(11, 7, 694)
	g.agregarArista(11, 8, 1223)
	g.agregarArista(11, 9, 1417)
	g.agregarArista(11, 10, 1694)
	g.agregarArista(12, 1, 782)
	g.agregarArista(12, 2, 127)
	g.agregarArista(12, 3, 541)
	g.agregarArista(12, 4, 426)
	g.agregarArista(12, 5, 943)
	g.agregarArista(12, 6, 665)
	g.agregarArista(12, 7, 1140)
	g.agregarArista(12, 8, 568)
	g.agregarArista(12, 9, 223)
	g.agregarArista(12, 10, 54)
	g.agregarArista(12, 11, 1640)
	g.agregarArista(13, 1, 697)
	g.agregarArista(13, 2, 546)
	g.agregarArista(13, 3, 984)
	g.agregarArista(13, 4, 98)
	g.agregarArista(13, 5, 952)
	g.agregarArista(13, 6, 814)
	g.agregarArista(13, 7, 1502)
	g.agregarArista(13, 8, 930)
	g.agregarArista(13, 9, 300)
	g.agregarArista(13, 10, 577)
	g.agregarArista(13, 11, 1649)
	g.agregarArista(13, 12, 523)
	g.agregarArista(14, 1, 1370)
	g.agregarArista(14, 2, 928)
	g.agregarArista(14, 3, 317)
	g.agregarArista(14, 4, 1319)
	g.agregarArista(14, 5, 1463)
	g.agregarArista(14, 6, 1253)
	g.agregarArista(14, 7, 1154)
	g.agregarArista(14, 8, 934)
	g.agregarArista(14, 9, 1117)
	g.agregarArista(14, 10, 774)
	g.agregarArista(14, 11, 1848)
	g.agregarArista(14, 12, 756)
	g.agregarArista(14, 13, 1417)
	

	print("\n\nLa ruta más rápida junto con su costo es:")
	g.dijkstra(1)
	print(g.camino(1, 6))
	print("\nLos valores finales de la gráfica son los siguietes:")
	g.imprimirGrafica()
    