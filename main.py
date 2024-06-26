import folium
import webbrowser
from geopy.geocoders import Nominatim

# Dane początkowe
klienci = [
    ("Janina Wójcicka", "52.2297,21.0122"),
    ("Anna Koralowska", "50.0647,19.9450"),
    ("Mateusz Bóbr-Sruański", "52.4064,16.9252"),
]

kierowcy = [
    ("Marcin Rozprawiciel", "52.2297,21.0122"),
    ("Tomasz z Tomaszowa", "51.1079,17.0385"),
    ("Andrzej Młyn", "54.3520,18.6466"),
]

taksowki = [
    ("Taksówka nr 1 Honda", "52.2297,21.0122"),
    ("Taksówka nr 2 Toyota", "51.7592,19.4560"),
    ("Taksówka nr 3 Ford", "53.4285,14.5528"),
]

rezerwacje = []

# Geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Funkcje
def pobierz_wspolrzedne(miejscowosc):
    location = geolocator.geocode(miejscowosc)
    if location:
        return (location.latitude, location.longitude)
    else:
        print("Nie znaleziono lokalizacji!")
        return None

def dodaj_do_listy(lista, item, miejscowosc):
    wspolrzedne = pobierz_wspolrzedne(miejscowosc)
    if wspolrzedne:
        lista.append((item, f"{wspolrzedne[0]},{wspolrzedne[1]}"))
        print(f"Dodano element {item} do listy!")
    else:
        print("Nie można dodać elementu do listy bez współrzędnych!")

def wyswietl_liste(lista):
    if not lista:
        print("Lista jest pusta!")
    else:
        for i, (item, coords) in enumerate(lista, start=1):
            print(f"{i}. {item} - {coords}")

def usun_element(lista):
    wyswietl_liste(lista)
    item = int(input("Podaj numer elementu do usunięcia: ")) - 1
    if 0 <= item < len(lista):
        del lista[item]
        print("Usunięto element z listy!")
    else:
        print("Element nie znaleziony!")

def aktualizuj_element(lista):
    wyswietl_liste(lista)
    item = int(input("Podaj numer elementu do aktualizacji: ")) - 1
    if 0 <= item < len(lista):
        new_item = input("Podaj nową wartość: ")
        miejscowosc = input("Podaj nową miejscowość: ")
        wspolrzedne = pobierz_wspolrzedne(miejscowosc)
        if wspolrzedne:
            lista[item] = (new_item, f"{wspolrzedne[0]},{wspolrzedne[1]}")
            print("Zaktualizowano element!")
        else:
            print("Nie znaleziono lokalizacji!")
    else:
        print("Element nie znaleziony!")

def wyswietl_klientow_dla_taksowki():
    wyswietl_liste(taksowki)
    taksowka = int(input("Podaj numer taksówki: ")) - 1
    dzien = input("Podaj dzień (DD-MM-YYYY): ")
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
    wyswietl_liste(taksowki)
    taksowka = int(input("Podaj numer taksówki: ")) - 1
    dzien = input("Podaj dzień (DD-MM-YYYY): ")
    wyswietl_liste(klienci)
    klient = int(input("Podaj numer klienta: ")) - 1
    if 0 <= klient < len(klienci) and 0 <= taksowka < len(taksowki):
        klient_nazwa = klienci[klient][0]
        taksowka_nazwa = taksowki[taksowka][0]
        rezerwacje.append((taksowka_nazwa, dzien, klient_nazwa))
        print(f"Dodano rezerwację! Klient: {klient_nazwa}, Taksówka: {taksowka_nazwa}")
    else:
        print("Niepoprawny numer klienta lub taksówki!")

def generuj_mape():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=6)

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
            dodaj_do_listy(klienci, input("Podaj imię klienta: "), input("Podaj miejscowość klienta: "))
        elif choice == "2":
            wyswietl_liste(klienci)
        elif choice == "3":
            usun_element(klienci)
        elif choice == "4":
            aktualizuj_element(klienci)
        elif choice == "5":
            dodaj_do_listy(kierowcy, input("Podaj imię kierowcy: "), input("Podaj miejscowość kierowcy: "))
        elif choice == "6":
            wyswietl_liste(kierowcy)
        elif choice == "7":
            usun_element(kierowcy)
        elif choice == "8":
            aktualizuj_element(kierowcy)
        elif choice == "9":
            dodaj_do_listy(taksowki, input("Podaj nazwę taksówki: "), input("Podaj miejscowość taksówki: "))
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