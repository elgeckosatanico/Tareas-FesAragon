'''Fn-5 
Encuentra a los Lideres'''
def lider(lista):
    temp=lista[0]
    resto=0
    for i in range(0,3):
        if (temp<lista[i+1]):
            resto+=temp
            temp=lista[i+1]
        else:
            resto+=lista[i+1]   
    if ((resto/3)>= temp):
        print("No hay lider")
    else:
        print(f"El lider es {temp}") 



lista = []
print("Ingresar minimos 4 numeros enteros mayores o iguales a 0")
total=suma=0
for i in range (0,4):
    num=int(input(f"Digite el numero {i+1}: "))
    lista.append(num)
print(lista)
lider(lista);