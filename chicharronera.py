import math
def discriminante(a,b,c):
    d=pow(b,2)-(4*a*c)
    return d

def solucion(a,b,d):
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    return x1,x2

a=float(raw_input('a: '))
b=float(raw_input('b: '))
c=float(raw_input('c: '))

di=discriminante(a,b,b)

if di<0:
    print("no hay raices positivas")
else:
   print("las soluciones son")
   print(solucion(a,b,di))