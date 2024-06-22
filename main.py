import folium
import webbrowser

# Dane
klienci = [("Jan Kowalski", "52.2297,21.0122"), ("Anna Nowak", "52.2298,21.0123"),
           ("Piotr Wiśniewski", "52.2299,21.0124")]
kierowcy = [("Marcin Kowalski", "52.2303,21.0128"), ("Tomasz Nowak", "52.2304,21.0129"),
            ("Andrzej Wiśniewski", "52.2305,21.0130")]
taksowki = [("T123", "52.2297,21.0122"), ("T124", "52.2298,21.0123"), ("T125", "52.2299,21.0124")]
rezerwacje = []


# Funkcje

def dodaj_do_listy(lista, item, coords):
    lista.append((item, coords))
    print("Dodano element do listy!")


def wyswietl_liste(lista):
    if not lista:
        print("Lista jest pusta!")
    else:
        for item, coords in lista:
            print(f"{item} - {coords}")


def usun_element(lista):
    item = input("Podaj element do usunięcia: ")
    for i, (elem, coords) in enumerate(lista):
        if elem == item:
            del lista[i]
            print("Usunięto element z listy!")
            return
    print("Element nie znaleziony!")


def aktualizuj_element(lista):
    old_item = input("Podaj element do aktualizacji: ")
    for i, (elem, coords) in enumerate(lista):
        if elem == old_item:
            new_item = input("Podaj nową wartość: ")
            new_coords = input("Podaj nowe współrzędne: ")
            lista[i] = (new_item, new_coords)
            print("Zaktualizowano element!")
            return
    print("Element nie znaleziony!")


def wyswietl_klientow_dla_taksowki():
    taksowka = input("Podaj numer taksówki: ")
    dzien = input("Podaj dzień (YYYY-MM-DD): ")
    klienci_w_dniu = [r[2] for r in rezerwacje if r[0] == taksowka and r[1] == dzien]
    if klienci_w_dniu:
        print("\n".join(klienci_w_dniu))
    else:
        print("Brak klientów dla tej taksówki w wybranym dniu!")


def dodaj_rezerwacje():
    taksowka = input("Podaj numer taksówki: ")
    dzien = input("Podaj dzień (YYYY-MM-DD): ")
    klient = input("Podaj imię klienta: ")
    rezerwacje.append((taksowka, dzien, klient))
    print("Dodano rezerwację!")


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

    # Spróbuj otworzyć mapę w przeglądarce
    try:
        webbrowser.open("mapa.html")
    except Exception as e:
        print(f"Nie udało się otworzyć mapy automatycznie. Otwórz plik 'mapa.html' ręcznie. Błąd: {e}")


# Logowanie
def zaloguj():
    user = input("Użytkownik: ")
    password = input("Hasło: ")
    if user == "Jakub" and password == "geoinformatyka rządzi":
        print("Zalogowano pomyślnie!")
        otworz_panel_glowny()
    else:
        print("Niepoprawne dane logowania!")


# Panel główny
def otworz_panel_glowny():
    while True:
        print("--- Panel Główny ---")
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
            dodaj_do_listy(taksowki, input("Podaj numer taksówki: "), input("Podaj współrzędne taksówki: "))
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
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    zaloguj()