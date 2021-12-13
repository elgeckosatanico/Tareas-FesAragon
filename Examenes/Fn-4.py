def listaX2(listaNumeros1,listaNumeros2):
    laSuma1 = 0
    laSuma2 = 0
    for i in listaNumeros1:
        laSuma1 = laSuma1 + i
    for i in listaNumeros2:
        laSuma2 = laSuma2 + i
    return laSuma1/len(listaNumeros1)+laSuma2/len(listaNumeros2)

def listaX3(listaNumeros1,listaNumeros2,listaNumeros3):
    laSuma1=0
    laSuma2=0
    laSuma3=0
    for i in listaNumeros1:
        laSuma1 = laSuma1 + i
    for i in listaNumeros2:
        laSuma2 = laSuma2 + i
    for i in listaNumeros3:
        laSuma3 = laSuma3 + i
    return laSuma1/len(listaNumeros1)+laSuma2/len(listaNumeros2)+laSuma3/len(listaNumeros3)
        

 


print(listaX2([1,2,2,2,2,1],[2,1]))#3.1666
print(listaX3([10,5],[6,2,2],[1]))#11.8333
print(listaX2([3,4,1,3,5,1,4],[21,54,33,21,77]))#44.2

