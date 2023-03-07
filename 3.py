lista = []
szám = (input("Irja be a számot: "))

while (szám != ""):
    lista.append(int(szám))
    szám = (input("Irja be a számot: "))

print("A beirt számok összege: ",sum(lista))