import requests
import folium
import webbrowser
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

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
geolocator = Nominatim(user_agent="myGeocoder")

def pobierz_wspolrzedne(miejscowosc):
    try:
        location = geolocator.geocode(miejscowosc)
        if location:
            return f"{location.latitude},{location.longitude}"
        else:
            print(f"Nie znaleziono współrzędnych dla miejscowości {miejscowosc}.")
            return None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Błąd geokodowania dla miejscowości {miejscowosc}: {e}")
        return None

# Funkcje pomocnicze
def dodaj_do_listy(lista, item, miejscowosc):
    wspolrzedne = pobierz_wspolrzedne(miejscowosc)
    if wspolrzedne:
        lista.append((item, wspolrzedne))
        print(f"Dodano element {item} do listy!")
    else:
        print("Nie można dodać elementu do listy bez współrzędnych!")

def wyswietl_liste(lista):
    if not lista:
        print("Lista jest pusta!")
    else:
        for i, (item, coords) in enumerate(lista, start=1):
            print(f"{i}. {item} - {coords}")

def usun_taksowke():
    wyswietl_liste(taksowki)
    taksowka_idx = int(input("Podaj numer taksówki do usunięcia: ")) - 1
    if 0 <= taksowka_idx < len(taksowki):
        del taksowki[taksowka_idx]
        print("Taksówka została usunięta.")
    else:
        print("Niepoprawny numer taksówki.")

def usun_klienta():
    wyswietl_liste(klienci)
    klient_idx = int(input("Podaj numer klienta do usunięcia: ")) - 1
    if 0 <= klient_idx < len(klienci):
        del klienci[klient_idx]
        print("Klient został usunięty.")
    else:
        print("Niepoprawny numer klienta.")

def usun_kierowce():
    wyswietl_liste(kierowcy)
    kierowca_idx = int(input("Podaj numer kierowcy do usunięcia: ")) - 1
    if 0 <= kierowca_idx < len(kierowcy):
        del kierowcy[kierowca_idx]
        print("Kierowca został usunięty.")
    else:
        print("Niepoprawny numer kierowcy.")

def aktualizuj_element(lista):
    wyswietl_liste(lista)
    idx = int(input("Podaj numer elementu do aktualizacji: ")) - 1
    if 0 <= idx < len(lista):
        nowy_element = input("Podaj nową nazwę elementu: ")
        miejscowosc = input("Podaj miejscowość: ")
        wspolrzedne = pobierz_wspolrzedne(miejscowosc)
        if wspolrzedne:
            lista[idx] = (nowy_element, wspolrzedne)
            print("Element został zaktualizowany.")
        else:
            print("Nie można zaktualizować elementu bez współrzędnych!")
    else:
        print("Niepoprawny numer elementu.")

def dodaj_rezerwacje():
    wyswietl_liste(taksowki)
    taksowka_idx = int(input("Podaj numer taksówki do zarezerwowania: ")) - 1
    dzien = input("Podaj dzień (DD-MM-YYYY): ")
    wyswietl_liste(klienci)
    klient_idx = int(input("Podaj numer klienta: ")) - 1

    if 0 <= taksowka_idx < len(taksowki) and 0 <= klient_idx < len(klienci):
        taksowka_nazwa, _ = taksowki[taksowka_idx]
        klient_nazwa, _ = klienci[klient_idx]
        rezerwacje.append((taksowka_nazwa, dzien, klient_nazwa))
        print(f"Dodano rezerwację! Klient: {klient_nazwa}, Taksówka: {taksowka_nazwa}")
    else:
        print("Niepoprawny numer klienta lub taksówki!")

def wyswietl_rezerwacje_dla_taksowki():
    wyswietl_liste(taksowki)
    taksowka_idx = int(input("Podaj numer taksówki do wyświetlenia rezerwacji: ")) - 1

    if 0 <= taksowka_idx < len(taksowki):
        taksowka_nazwa, _ = taksowki[taksowka_idx]
        rezerwacje_dla_taksowki = [(r[2], r[1]) for r in rezerwacje if r[0] == taksowka_nazwa]

        if rezerwacje_dla_taksowki:
            print(f"Rezerwacje dla taksówki {taksowka_nazwa}:")
            for klient, dzien in rezerwacje_dla_taksowki:
                print(f"Klient: {klient}, Dzień: {dzien}")
        else:
            print(f"Brak rezerwacji dla taksówki {taksowka_nazwa}.")
    else:
        print("Niepoprawny numer taksówki!")


def generuj_mape_klientow():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=6)

    for klient, coords in klienci:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Klient: {klient}").add_to(mapa)

    mapa.save("mapa_klientow.html")
    print("Mapa klientów została wygenerowana i zapisana jako 'mapa_klientow.html'.")

    # Otwórz mapę w przeglądarce
    webbrowser.open("mapa_klientow.html")

def generuj_mape_kierowcow():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=6)

    for kierowca, coords in kierowcy:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Kierowca: {kierowca}").add_to(mapa)

    mapa.save("mapa_kierowcow.html")
    print("Mapa kierowców została wygenerowana i zapisana jako 'mapa_kierowcow.html'.")

    # Otwórz mapę w przeglądarce
    webbrowser.open("mapa_kierowcow.html")

def generuj_mape_taksowek():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=6)

    for taksowka, coords in taksowki:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Taksówka: {taksowka}").add_to(mapa)

    mapa.save("mapa_taksowek.html")
    print("Mapa taksówek została wygenerowana i zapisana jako 'mapa_taksowek.html'.")

    # Otwórz mapę w przeglądarce
    webbrowser.open("mapa_taksowek.html")

def generuj_mape_wszystkiego():
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

    mapa.save("mapa_wszystkiego.html")
    print("Mapa wszystkiego została wygenerowana i zapisana jako 'mapa_wszystkiego.html'.")

    # Otwórz mapę w przeglądarce
    webbrowser.open("mapa_wszystkiego.html")

# Logowanie
def zaloguj():
    print("=== LOGOWANIE ===")
    nazwa_uzytkownika = input("Podaj nazwę użytkownika: ")
    haslo = input("Podaj hasło: ")

    # Symulacja logowania (zawsze poprawne logowanie w celach demonstracyjnych)
    if nazwa_uzytkownika == "admin" and haslo == "admin":
        print("Zalogowano pomyślnie!")
        otworz_panel_glowny()
    else:
        print("Niepoprawne dane logowania.")
        zaloguj()

# Panel główny
def otworz_panel_glowny():
    while True:
        print("\n=== PANEL GŁÓWNY ===")
        print("1. Wyświetl listę klientów")
        print("2. Dodaj klienta")
        print("3. Usuń klienta")
        print("4. Aktualizuj klienta")
        print("5. Wyświetl listę kierowców")
        print("6. Dodaj kierowcę")
        print("7. Usuń kierowcę")
        print("8. Aktualizuj kierowcę")
        print("9. Wyświetl listę taksówek")
        print("10. Dodaj taksówkę")
        print("11. Usuń taksówkę")
        print("12. Aktualizuj taksówkę")
        print("13. Dodaj rezerwację")
        print("14. Wyświetl rezerwacje dla taksówki")
        print("15. Generuj mapę klientów")
        print("16. Generuj mapę kierowców")
        print("17. Generuj mapę taksówek")
        print("18. Generuj mapę wszystkiego")
        print("0. Wyloguj")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            wyswietl_liste(klienci)
        elif choice == "2":
            dodaj_do_listy(klienci, input("Podaj nazwę klienta: "), input("Podaj miejscowość klienta: "))
        elif choice == "3":
            usun_klienta()
        elif choice == "4":
            aktualizuj_element(klienci)
        elif choice == "5":
            wyswietl_liste(kierowcy)
        elif choice == "6":
            dodaj_do_listy(kierowcy, input("Podaj imię kierowcy: "), input("Podaj miejscowość kierowcy: "))
        elif choice == "7":
            usun_kierowce()
        elif choice == "8":
            aktualizuj_element(kierowcy)
        elif choice == "9":
            wyswietl_liste(taksowki)
        elif choice == "10":
            dodaj_do_listy(taksowki, input("Podaj nazwę taksówki: "), input("Podaj miejscowość taksówki: "))
        elif choice == "11":
            usun_taksowke()
        elif choice == "12":
            aktualizuj_element(taksowki)
        elif choice == "13":
            dodaj_rezerwacje()
        elif choice == "14":
            wyswietl_rezerwacje_dla_taksowki()
        elif choice == "15":
            generuj_mape_klientow()
        elif choice == "16":
            generuj_mape_kierowcow()
        elif choice == "17":
            generuj_mape_taksowek()
        elif choice == "18":
            generuj_mape_wszystkiego()
        elif choice == "0":
            break
        else:
            print("Niepoprawny wybór opcji. Spróbuj ponownie.")

# Uruchomienie programu
if __name__ == "__main__":
    zaloguj()
