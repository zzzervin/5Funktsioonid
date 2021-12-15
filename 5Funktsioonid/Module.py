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

#def arithmetic(arv1:float,arv2:float,operatsioon:str):
#    """Liitmene,lahutamine,korrutamine ja jagamine.
#   """
#    if operatsioon in ["-","+","*","*"]:
#        if operatsioon==0 and operatsioon=="/":
#            print("eiole")
#        else:
#            S=(str(arv1)+operatsioon+str(arv2))
#        return S

def Liigaasta (aasta:int)->bool:
    """ 
    """
    if aasta%4==0:
        tulemus=True
    else:
        tulemus=False
    return tulemus
 
        
        