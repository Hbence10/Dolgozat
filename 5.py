szám = int(input("kérem adja meg, hogy melyik szám négyzetét szeretné: "))

if szám >= 0:
    print("A szám négyzete: ",szám ** 2)
elif szám < 0:
    print("Ez a szám helytelen")
    új_szám = int(input("Adjon meg egy új számot ami most helyes: "))
    print("Az új szám négyzete: ", új_szám ** 2)