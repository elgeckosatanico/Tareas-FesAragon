'''
Examen Fn - 1.py
Crear una función que regrese el enésimo número par.
nthPar(1) //=> 0, El primer número par es 0
nthPar(3) //=> 4, El tercer número par es 4 (0, 2, 4)
nthPar(100) //=> 198
nthPar(1298734) //=> 2597466
'''

def  nthPar( n ):
    ene = ((n - 1 ) * 2 )
    print ( " El enésimo numero par de " , n, "es " , ene)

nthPar(1298734)    