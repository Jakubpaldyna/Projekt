# Dane
klienci = ["Jan Kowalski", "Anna Nowak", "Piotr Wiśniewski"]
kierowcy = ["Marcin Kowalski", "Tomasz Nowak", "Andrzej Wiśniewski"]
taksowki = ["T123", "T124", "T125"]
rezerwacje = []


# Funkcje

def dodaj_do_listy(lista, item):
    lista.append(item)
    print("Dodano element do listy!")


def wyswietl_liste(lista):
    if not lista:
        print("Lista jest pusta!")
    else:
        print("\n".join(lista))


def usun_element(lista):
    item = input("Podaj element do usunięcia: ")
    if item in lista:
        lista.remove(item)
        print("Usunięto element z listy!")
    else:
        print("Element nie znaleziony!")


def aktualizuj_element(lista):
    old_item = input("Podaj element do aktualizacji: ")
    if old_item in lista:
        new_item = input("Podaj nową wartość: ")
        index = lista.index(old_item)
        lista[index] = new_item
        print("Zaktualizowano element!")
    else:
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


# Logowanie
def zaloguj():
    user = input("Użytkownik: ")
    password = input("Hasło: ")
    if user == "admin" and password == "password":
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
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            dodaj_do_listy(klienci, input("Podaj imię klienta: "))
        elif choice == "2":
            wyswietl_liste(klienci)
        elif choice == "3":
            usun_element(klienci)
        elif choice == "4":
            aktualizuj_element(klienci)
        elif choice == "5":
            dodaj_do_listy(kierowcy, input("Podaj imię kierowcy: "))
        elif choice == "6":
            wyswietl_liste(kierowcy)
        elif choice == "7":
            usun_element(kierowcy)
        elif choice == "8":
            aktualizuj_element(kierowcy)
        elif choice == "9":
            dodaj_do_listy(taksowki, input("Podaj numer taksówki: "))
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
        elif choice == "0":
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    zaloguj()
