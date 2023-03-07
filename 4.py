import math

átmérő = int(input("Kérem adja meg a kör átmérőjét"))

sugár = átmérő / 2
sugár_a_négyzeten = sugár*sugár
pi = math.pi

kerület = 2*sugár*pi
terület = sugár_a_négyzeten*pi

print("A kör területe: ",round(terület,2),"és a kerülete: ",round(kerület,2))