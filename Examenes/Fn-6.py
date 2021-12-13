'''Fn-6
Suma de diferencias'''
def sumDif(arr):
    suma=res=0
    resta=[]
    for i in range(0,(len(arr)-1)):
        res=arr[i]-arr[i+1]
        resta.append(res)
    for i in range(0,len(resta)):
        suma=suma+resta[i]
    return suma

elementos=[]
numelementos=int(input("¿Cuantos elementos desea ingresar en el array? "))
for i in range(0,numelementos):
    elementos.append(int(input(f"Introduzca un numero para la posicion {i}: ")))
print(sumDif(elementos))