"""Un numar natural se numeste numr perfect daca este gal cu suma divizorilor lui deoarece 6=1+2+3. Sa se afle numerele perfecte mai mici decat numarul natural n."""
n=int(input("introduceti numarul n:"))
for p in range(1,n):
    s=0
    for m in range(1,p):
        if(p%m==0):
            s+=m
            if s==p:
                print(p,end=" ")