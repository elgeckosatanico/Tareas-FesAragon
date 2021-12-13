'''
Examen Fn - 2.py
Crear una función que regrese el enésimo número non.
nthNon(1) //=> 1, El primer número non es 1
nthNon(3) //=> 5, El tercer número non es 5 (1, 3, 5)
nthNon(100) //=> 199
nthNon(1298734) //=> 2597467
'''
def nthNon(n):
    ene = (n* 2-1)
    print ( " El enésimo numero non de " , n, "es " , ene)

nthNon(1298734)    