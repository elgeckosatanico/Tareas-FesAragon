'''A-5
Programa que indica que números de una lista son divisinles por un número dado'''
lista=[1,2,3,4,5,6]
lista_2=[9,12,3,0,1,4]
lista_3=[10,11,3]

def lista_divisible(lista):
    divisor=int(input("Divisor: "))
    lista_nueva=[]
    for i in range(0,len(lista)):
        if(lista[i]%divisor==0 and lista[i]!=0):
            lista_nueva.append(lista[i])
    return lista_nueva

print(lista,"\n",lista_divisible(lista))
print(lista_2,"\n",lista_divisible(lista_2))
print(lista_3,"\n",lista_divisible(lista_3))