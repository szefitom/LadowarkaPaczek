import os

saldo_konta = 0.0
magazyn = {}
historia = []


if os.path.exists("saldo.txt"):
    with open("saldo.txt") as f:
        saldo_konta = float(f.read().strip())

if os.path.exists("magazyn.txt"):
    with open("magazyn.txt") as f:
        for linia in f:
            if linia.strip():
                nazwa, cena, ilosc = linia.strip().split(";")
                magazyn[nazwa] = {"cena": float(cena), "ilosc": int(ilosc)}

if os.path.exists("historia.txt"):
    with open("historia.txt") as f:
        for linia in f:
            if linia.strip():
                historia.append(linia.strip())

while True:
    wybor = input("""
Wybierz jedną z poniższych komend:
- saldo
- sprzedaż
- zakup
- konto
- lista
- magazyn
- przegląd
- koniec
Podaj komendę: """)

    match wybor:
        case "saldo":
            kwota = float(input("Podaj kwotę do dodania lub odjęcia: "))
            if saldo_konta + kwota < 0:
                print("Nie możesz ustawić salda na wartość ujemną.")
            else:
                saldo_konta += kwota
                historia.append(f"Zmiana salda o {kwota:.2f}")
                print(f"Aktualne saldo: {saldo_konta:.2f} PLN")

        case "sprzedaż":
            produkt = input("Podaj nazwę produktu: ")
            if produkt not in magazyn or magazyn[produkt]["ilosc"] <= 0:
                print("Brak produktu w magazynie.")
                continue
            cena = float(input("Podaj cenę sprzedaży: "))
            ilosc = int(input("Podaj liczbę sztuk: "))
            if cena < 0 or ilosc <= 0:
                print("Cena i ilość muszą być dodatnie.")
                continue
            if ilosc > magazyn[produkt]["ilosc"]:
                print("Za mało sztuk w magazynie.")
                continue
            magazyn[produkt]["ilosc"] -= ilosc
            saldo_konta += cena * ilosc
            historia.append(f"Sprzedaż: {produkt}, {ilosc} szt. po {cena:.2f} PLN")
            print("Sprzedaż zarejestrowana.")

        case "zakup":
            produkt = input("Podaj nazwę produktu: ")
            cena = float(input("Podaj cenę zakupu: "))
            ilosc = int(input("Podaj liczbę sztuk: "))
            if cena < 0 or ilosc <= 0:
                print("Cena i ilość muszą być dodatnie.")
                continue
            koszt = cena * ilosc
            if saldo_konta - koszt < 0:
                print("Niewystarczające środki na koncie.")
                continue
            saldo_konta -= koszt
            if produkt in magazyn:
                magazyn[produkt]["ilosc"] += ilosc
            else:
                magazyn[produkt] = {"cena": cena, "ilosc": ilosc}
            historia.append(f"Zakup: {produkt}, {ilosc} szt. po {cena:.2f} PLN")
            print("Zakup zarejestrowany.")

        case "konto":
            print(f"Aktualne saldo: {saldo_konta:.2f} PLN")

        case "lista":
            print("Stan magazynu:")
            if magazyn:
                for prod, dane in magazyn.items():
                    print(f"{prod}: {dane['ilosc']} szt., cena: {dane['cena']:.2f} PLN")
            else:
                print("Magazyn pusty.")

        case "magazyn":
            produkt = input("Podaj nazwę produktu: ")
            if produkt in magazyn:
                dane = magazyn[produkt]
                print(f"{produkt}: {dane['ilosc']} szt., cena: {dane['cena']:.2f} PLN")
            else:
                print("Produkt nie istnieje w magazynie.")

        case "przegląd":
            od = input("Podaj wartość 'od' (numer transakcji), jeśli nie chcesz nic nie podawaj: ")
            do = input("Podaj wartość 'do' (numer transakcji), jeśli nie chcesz nic nie podawaj: ")
            if od:
                od = int(od)
            else:
                od = 0
            if do:
                do = int(do)
            else:
                do = len(historia)
            if od < 0 or do > len(historia) or od > do:
                print(f"Błędny zakres. Liczba transakcji: {len(historia)}")
            else:
                print("Przegląd transakcji:")
                for i in range(od, do):
                    print(f"{i}: {historia[i]}")

        case "koniec":
            with open("saldo.txt", "w") as f:
                f.write(str(saldo_konta))

            with open("magazyn.txt", "w") as f:
                for nazwa, dane in magazyn.items():
                    f.write(f"{nazwa};{dane['cena']:.2f};{dane['ilosc']}\n")

            with open("historia.txt", "w") as f:
                for wpis in historia:
                    f.write(wpis + "\n")

            print("Koniec działania programu.")
            break

        case _:
            print("Nieznana komenda.")