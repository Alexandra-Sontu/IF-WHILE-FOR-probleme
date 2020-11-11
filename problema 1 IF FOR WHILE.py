a=int(input("dati un numar: "))
if ((a<28)or(a>31)):
    print("nu sunt luni cu asa numar de zile")
elif a==28:
    print("februarie, daca nu e an bisect")
elif a==29:
    print("februarie, daca e an bisect")
elif a==30:
    print("aprilie,iunie,septembrie,noiembrie")
else:
    print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")