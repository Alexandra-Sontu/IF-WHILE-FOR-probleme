"""Mihai are un unchi bogat care i-a daruit in ziua cind s-a nascut un dolar, iar in fiecare an el dubla cadoul  si mai adauga atitia dolari
citi ani implinea mihai.
a)sa se calculeze citi dolari a primit Mihai atunci cind a implinit n ani(n<20).
b)La ce virsta cadoull lui Mihai era mai mare de 100$?"""
n=eval(input("dati un numar mai mic ca 20:"))
a=1
b=0
for c in range(1,n+1):
    a=a*2+c
    print("la",n,"ani","Mihaia primit",a,"dolari")
    a=1
    for c in range(1,20):
        while a<=100:
            a=a*2+c
            b+=1
        print("La varsta de",b,"ani va primi ma mult de 100$")