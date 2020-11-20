"""Se dau numerele pozitive a,b,c.Sa se verifice daca exista un triunghi cu aceste laturi,
daca da;atunci ce fel de triungi este:scalen, isoscel sau echilateral"""
x=int(input("dati un numar pozitiv:"))
y=int(input("dati un numar pozitiv:"))
z=int(input("dati un numar pozotiv:"))
if (x+y)>z and (x+z)>y and (y+z)>x:
    print("exista un triunghi cu astfel de laturi")
if x!=y and y!=z and x!=z:
    print("triunghiul este scalen")
elif x==y and x==z and y==z:
    print("triunghiul este echilateral")
else:
    print("triunghiul este isoscel")
else:
    print("nu exista un triunghi cu astfel de laturi")
