def removerTodosRepetidos(arr):
    arrN=[]
    for j in range (len(arr)):
        contador=0
        for i in range (0,len(arr)):
            if arr[j]==arr[i]:
                contador+=1
        if contador==1:
            arrN.append(arr[j])
    return arrN

arr=[9,3,1,3,9,2]
print(removerTodosRepetidos(arr))
