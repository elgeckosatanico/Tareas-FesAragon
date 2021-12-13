def busqueda_lineal(lista, x):
    i=0
    for z in lista:
        if z == x:
            return i
        i=i+1
    return -1

#print(busqueda_lineal([1, 4, 7, 3, 0, 2], 7))#2
#print(busqueda_lineal([1, 4, 7, 3, 0, 99], 99))#5
#print(busqueda_lineal([1, 4, 7, 44, 0, 2], 44))#3
#print(busqueda_lineal([101, 4, 7, 3, 0, 2], 101))#0

lista1=[]

for x in range(10000):
    lista1.append(random.randrange(101))

elemento=int(input("Ingrese el numero a buscar"))
print(lista1)
print(busqueda_lineal(lista1,elemento))
