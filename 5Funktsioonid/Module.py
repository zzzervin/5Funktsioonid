
#def K_P(kulg:float,korgus:float):
#    """laiab kolmnurga pindalat. On antud kõrgus ja kulje pikkud. Tagastab S float formaadis
#    :paran float kulg: Kolmnurga kulja pikkus
#    :paran float korgus: Korgus vastav kuljele
#    :rtype:var
#    """
#    if kulg < 0 or korgus < 0 :
#        S="Valed andmet!"
#    else:
#        S=0.5*kulg*korgus
#    return S

#1
#def arithmetic(arv1:float,arv2:float,operatsioon:str):
#    """Liitmene,lahutamine,korrutamine ja jagamine.
#   """
#    if operatsioon in ["-","+","*","*"]:
#        if operatsioon==0 and operatsioon=="/":
#            print("eiole")
#        else:
#            S=(str(arv1)+operatsioon+str(arv2))
#        return S

#2
#def Liigaasta (aasta:int)->bool:
#    """ 
#    """
#    if aasta%4==0:
#        tulemus=True
#    else:
#        tulemus=False
#    return tulemus

#3
#from math import *
#def ruud(a:float):
#    """
#    :param float a:
#    :rytpe:float,float,float
#    """
#    S=a*a
#    P=2*(a+a)
#    d=a*sqrt(2)
#    return P,S,d  

#4
#def K(kuu:int)->str:
#    """
#    (talv, kevad, suvi ja sügis).
#    :param: float kuu:
#    :ryturn:s
#    """
#    if kuu>=1 and kuu<=12:
#        if kuu in [1,2,12]:
#            s="Talv"
#        if kuu in [3,4,5]:
#            s="kevad"
#        if kuu in [6,7,8]:
#            s="suvi "
#        if kuu in [9,10,11]:
#            s="sügis "        
#        return s

#5
#def bank(a:float,y:int)->float:
#    """
#    Kasutaja teeb aastateks euro suuruse sissemakse 10% aastas
#    :param: float a:
#    :ryturn:y
#    """
#    for i in range(y):
#        a*=1.1
#    return a

def is_prime(a:int)->bool:
    t=0
    for i in range(1,a+1):
        if a%0==0:t+=1
    if t==2:
        t=True
    else:
        t=False
    return t
