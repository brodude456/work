from copy import deepcopy

def ubaci_ime(lista,ime="Unknown"):
    lista[0].append(ime)
    lista[1].append(4)

imena=[["Sarajevp","ÏIstanbul"],[1,2]]


ubaci_ime(imena,"Zagreb")

print(imena)

