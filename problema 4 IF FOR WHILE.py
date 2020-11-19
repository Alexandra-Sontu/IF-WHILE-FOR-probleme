"""Sa se scrie un program care va efectua:
a) adunarea a 2 fractii date;
b)inmultirea a 2 fractii date;
Rezultatul va fi o fractie ireductibila"""
m=eval(input("dati un numar:"))#numarator
n=eval(input("dati un numar:"))#numitor
e=eval(input("dati un numar:"))#numarator
f=eval(input("dati un numar:"))#numitor
g=(m*f+e*n)
h=n*f
i=m*e
from fractions import Fraction
if n!=0 or f!=0:
    print("suma este =",Fraction(g,h))
    print("produsul este =",Fraction(i,h))
else:
        print("impartirea la 0 nu are sens")