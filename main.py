import folium
import webbrowser

# Dane
klienci = [
    ("Jan Kowalski", "52.2297,21.0122"),
    ("Anna Nowak", "52.2208,21.0103"),
    ("Piotr Wiśniewski", "52.2409,21.0304"),
    ("Marek Zalewski", "52.2350,21.0155"),
    ("Magda Kowalczyk", "52.2233,21.0199"),
    ("Jacek Wójcik", "52.2377,21.0288"),
    ("Paweł Zieliński", "52.2155,21.0054"),
    ("Katarzyna Kwiatkowska", "52.2104,21.0255"),
    ("Krzysztof Zając", "52.2256,21.0112"),
    ("Dorota Czarnecka", "52.2323,21.0209"),
    ("Michał Piotrowski", "52.2305,21.0156"),
    ("Sylwia Kamińska", "52.2344,21.0167"),
]

kierowcy = [
    ("Marcin Kowalski", "52.2333,21.0166"),
    ("Tomasz Nowak", "52.2364,21.0189"),
    ("Andrzej Wiśniewski", "52.2399,21.0220"),
    ("Krzysztof Lewandowski", "52.2268,21.0245"),
    ("Paweł Kwiatkowski", "52.2287,21.0271"),
    ("Dominik Nowicki", "52.2224,21.0265"),
    ("Jacek Król", "52.2292,21.0188"),
    ("Łukasz Pawlak", "52.2230,21.0250"),
]

taksowki = [
    ("Taksówka nr 1 Honda", "52.2282,21.0255"),
    ("Taksówka nr 2 Toyota", "52.2278,21.0184"),
    ("Taksówka nr 3 Ford", "52.2250,21.0200"),
    ("Taksówka nr 4 Mercedes", "52.2325,21.0215"),
    ("Taksówka nr 5 BMW", "52.2331,21.0223"),
    ("Taksówka nr 6 Audi", "52.2300,21.0230"),
    ("Taksówka nr 7 Skoda", "52.2244,21.0244"),
    ("Taksówka nr 8 Peugeot", "52.2211,21.0266"),
]

rezerwacje = []


# Funkcje

def dodaj_do_listy(lista, item, coords):
    lista.append((item, coords))
    print("Dodano element do listy!")


def wyswietl_liste(lista):
    if not lista:
        print("Lista jest pusta!")
    else:
        for i, (item, coords) in enumerate(lista, start=1):
            print(f"{i}. {item} - {coords}")


def usun_element(lista):
    item = int(input("Podaj numer elementu do usunięcia: ")) - 1
    if 0 <= item < len(lista):
        del lista[item]
        print("Usunięto element z listy!")
    else:
        print("Element nie znaleziony!")


def aktualizuj_element(lista):
    item = int(input("Podaj numer elementu do aktualizacji: ")) - 1
    if 0 <= item < len(lista):
        new_item = input("Podaj nową wartość: ")
        new_coords = input("Podaj nowe współrzędne: ")
        lista[item] = (new_item, new_coords)
        print("Zaktualizowano element!")
    else:
        print("Element nie znaleziony!")


def wyswietl_klientow_dla_taksowki():
    taksowka = int(input("Podaj numer taksówki: ")) - 1
    dzien = input("Podaj dzień (YYYY-MM-DD): ")
    if 0 <= taksowka < len(taksowki):
        taksowka_nazwa = taksowki[taksowka][0]
        klienci_w_dniu = [r[2] for r in rezerwacje if r[0] == taksowka_nazwa and r[1] == dzien]
        if klienci_w_dniu:
            print("\n".join(klienci_w_dniu))
        else:
            print("Brak klientów dla tej taksówki w wybranym dniu!")
    else:
        print("Niepoprawny numer taksówki!")


def dodaj_rezerwacje():
    taksowka = int(input("Podaj numer taksówki: ")) - 1
    dzien = input("Podaj dzień (YYYY-MM-DD): ")
    klient = int(input("Podaj numer klienta: ")) - 1
    if 0 <= klient < len(klienci) and 0 <= taksowka < len(taksowki):
        klient_nazwa = klienci[klient][0]
        taksowka_nazwa = taksowki[taksowka][0]
        rezerwacje.append((taksowka_nazwa, dzien, klient_nazwa))
        print(f"Dodano rezerwację! Klient: {klient_nazwa}, Taksówka: {taksowka_nazwa}")
    else:
        print("Niepoprawny numer klienta lub taksówki!")


def generuj_mape():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=12)

    for klient, coords in klienci:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Klient: {klient}").add_to(mapa)

    for kierowca, coords in kierowcy:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Kierowca: {kierowca}").add_to(mapa)

    for taksowka, coords in taksowki:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Taksówka: {taksowka}").add_to(mapa)

    mapa.save("mapa.html")
    print("Mapa została wygenerowana i zapisana jako 'mapa.html'.")

    # Otwórz mapę w przeglądarce
    webbrowser.open("mapa.html")


# Logowanie
def zaloguj():
    user = input("Użytkownik: ")
    password = input("Hasło: ")
    if user == "Jakub" and password == "geoinformatyka":
        print("Zalogowano pomyślnie!")
        otworz_panel_glowny()
    else:
        print("Niepoprawne dane logowania!")


# Panel główny
def otworz_panel_glowny():
    while True:
        print("\n--- Panel Główny ---")
        print("1. Dodaj klienta")
        print("2. Wyświetl klientów")
        print("3. Usuń klienta")
        print("4. Aktualizuj klienta")
        print("5. Dodaj kierowcę")
        print("6. Wyświetl kierowców")
        print("7. Usuń kierowcę")
        print("8. Aktualizuj kierowcę")
        print("9. Dodaj taksówkę")
        print("10. Wyświetl taksówki")
        print("11. Usuń taksówkę")
        print("12. Aktualizuj taksówkę")
        print("13. Dodaj rezerwację")
        print("14. Wyświetl klientów dla taksówki")
        print("15. Generuj mapę")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            dodaj_do_listy(klienci, input("Podaj imię klienta: "), input("Podaj współrzędne klienta: "))
        elif choice == "2":
            wyswietl_liste(klienci)
        elif choice == "3":
            usun_element(klienci)
        elif choice == "4":
            aktualizuj_element(klienci)
        elif choice == "5":
            dodaj_do_listy(kierowcy, input("Podaj imię kierowcy: "), input("Podaj współrzędne kierowcy: "))
        elif choice == "6":
            wyswietl_liste(kierowcy)
        elif choice == "7":
            usun_element(kierowcy)
        elif choice == "8":
            aktualizuj_element(kierowcy)
        elif choice == "9":
            dodaj_do_listy(taksowki, input("Podaj nazwę taksówki: "), input("Podaj współrzędne taksówki: "))
        elif choice == "10":
            wyswietl_liste(taksowki)
        elif choice == "11":
            usun_element(taksowki)
        elif choice == "12":
            aktualizuj_element(taksowki)
        elif choice == "13":
            dodaj_rezerwacje()
        elif choice == "14":
            wyswietl_klientow_dla_taksowki()
        elif choice == "15":
            generuj_mape()
        elif choice == "0":
            break
        else:
            print("Niepoprawna opcja!")


if __name__ == "__main__":
    zaloguj()