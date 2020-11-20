"""Conform calendarului japonez, fiecare an poarta numelui unui animal. Fiecare denumire se repeta exact odata la 12 ani.
Deci , un ciclu este format din 12 ani cu urmatoarele de denumiri de animale in aceasta ordine: sobolan, bou, tigru, iepure,
dragon, sarpe, cal,oaie, maimuta, cocos, ciine, porc. Anul dragonului a fost in 2000(anul 1000 anul sobolanului"""
a=eval(input("dati un an de 4 cifre:"))
if a>=1000 and a<10000:
    if(a-2000)%12==0:
        anul='dragonului'
    elif(a-2000)%12==1:
        anul='sarpelui'
    elif(a-2000)%12==2:
        anul='calului'
    elif(a-2000)%12==3:
        anul='oii'
    elif(a-2000)%12==4:
         anul='maimutei' 
    elif(a-2000)%12==5:
          anul='cocosului'
     elif(a-2000)%12==6:
        anul='ciinelui'
    elif(a-2000)%12==7:
        anul='porcului'
    elif(a-2000)%12==8:
        anul='sobolanului'
    elif(a-2000)%12==9:
        anul='boului'
    elif(a-2000)%12==10:
        anul='tigrului'
    else:
        anul='iepurelui'
        print("anul",anul)

            