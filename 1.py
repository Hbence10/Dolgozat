összeg_a= int(input("Kérem adja meg, hogy mennyi összeget szeretne berakni: "))
év_futamidő_n = int(input("Kérem adja meg hogy hány évre szeretné berakni az összeget: "))
százalék = int(input("Adja meg a lakötés kamatát: "))

kamat = százalék/100
zárójel = 1+kamat
négyzet = zárójel**év_futamidő_n
számolás = összeg_a*négyzet

print("Ennyi lesz a pénzből a kivánt idő után: ",round(számolás))