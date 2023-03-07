import random 

fej_vagy_irás = random.randint(1,2)

tipp = input("adja meg, hogy maga szerint fej vagy írás:  ")
szám = 0

if tipp == "írás":
    szám = szám + 1
elif tipp == "fej":
    szám = szám + 2
else:
    print("Maga nem létező választ adott meg: ")

if fej_vagy_irás == szám:
    print("Maga nyert")
elif fej_vagy_irás != szám:
    print("Maga veszitett")

