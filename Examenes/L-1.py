'''L-1
Triangulo'''
nones=[]
num=0
for i in range (1,27):
    num = i
    if(num % 2 != 0):
        nones.append(num)
        #print(nones)

pasos=-1
for i in range (0,11):
    print("")
    pasos=pasos+1
    for j in range(0,pasos):
        print(f"{nones[j]} ",end="")
