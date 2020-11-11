   
"""se da numarul n apartine (28,29,30,31) sa se afiseze lunile cu numarul n de zile"""
a=int(input("dati un numar:"))
if(a==28):
    print("februarie")
elif(a==29):
    print("februarie in an bisect")
elif(a==30):
    print("aprilie,iunie,septembrie,noiembrie")
elif(a==31):
    print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")
else:
    print("error")