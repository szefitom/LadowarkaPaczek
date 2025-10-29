ile = int(input("Ile elementów chcesz wysłać? "))

paczki = []
sumy = []
obecna = []
suma_obecna = 0
licznik = 1
wprowadzono = 0

while wprowadzono < ile:
    waga = float(input("Podaj wagę elementu " + str(licznik) + ": "))

    if waga < 1 or waga > 10:
        print("waga musi być od 1 do 10 kg")
        break

    if suma_obecna + waga > 20:
        paczki.append(obecna)
        sumy.append(suma_obecna)
        obecna = [waga]
        suma_obecna = waga
    else:
        obecna.append(waga)
        suma_obecna = suma_obecna + waga

    licznik = licznik + 1
    wprowadzono = wprowadzono + 1

if obecna:
    paczki.append(obecna)
    sumy.append(suma_obecna)

if len(sumy) == 0:
    print("Nie wysłano żadnej paczki.")
else:
    puste = []
    for s in sumy:
        puste.append(20 - s)

    wszystkie_kg = 0
    for s in sumy:
        wszystkie_kg = wszystkie_kg + s

    wszystkie_puste = 0
    for p in puste:
        wszystkie_puste = wszystkie_puste + p

    max_puste = puste[0]
    nr_max = 1
    i = 1
    for p in puste:
        if p > max_puste:
            max_puste = p
            nr_max = i
        i = i + 1

    print("\n" + "=" * 40)
    print("PODSUMOWANIE")
    print("=" * 40)
    print("Wysłano paczek: " + str(len(paczki)))
    print("Wysłano kilogramów: " + str(wszystkie_kg) + " kg")
    print("Suma pustych kilogramów: " + str(wszystkie_puste) + " kg")
    print("Najwięcej pustych kilogramów ma paczka " + str(nr_max) + " (" + str(max_puste) + " kg)")

    print("\nSzczegóły paczek:")
    for i in range(len(paczki)):
        tekst = ""
        for w in paczki[i]:
            if tekst != "":
                tekst = tekst + " + "
            tekst = tekst + str(w)
        print("  Paczka " + str(i + 1) + ": " + tekst + " = " + str(sumy[i]))