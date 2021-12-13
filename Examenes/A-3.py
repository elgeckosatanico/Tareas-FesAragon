'''Cuenta de positivos / Suma de negativos'''
lista = []
j = int(input("¿Cuantos numeros igresara?  "))
total=suma=0
for i in range (0,j):
    num=int(input(f"Digite un numero para la posicion {i}: "))
    lista.append(num)
    if(num==0):
        total=total
    elif(num>=1):
        total=total+1
    elif(num<0):
        suma=suma+num
print(f"Para el arreglo: {lista}\n")
print(f"{total} positivos, {suma} la suma de los negativos\n")

