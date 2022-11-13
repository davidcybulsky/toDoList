# ToDoList
def wczytaj(lista):
    try:
        plik = open("tasks.txt", "r")
        if (plik.readable()):
            for l in plik:
                lista.append(l.replace("\n", ""))
        #lista.extend(plik.read().splitlines())
        plik.close()
    except FileNotFoundError:
        print()


def zapisz(lista):
    try:
        plik = open("tasks.txt", "w")
        if (plik.writable()):
            for task in lista:
                plik.writelines(task + "\n")
    except FileNotFoundError:
        print()
    finally:
        plik.close()


def dodaj(lista):
    task = input("Podaj zadanie: ")
    lista.append(task)


def usun(lista):
    index = int(input("Podaj numer zadania: "))
    try:
        deleted = lista.pop(index - 1)
        print("Usunięto task numer " + str(index) + " " + deleted)
    except IndexError:
        print("Nieprawidłowy indeks: " + str(index))


def pokaz(lista):
    print("-To do list-")
    numer = 1
    print("------------")
    for l in lista:
        print(str(numer) + " - " + str(l))
        numer += 1
    print("------------")


lista = []
wczytaj(lista)
chosen_operation = 0
while (chosen_operation != 5):
    # pokaz(lista)
    print("""    1. Wyświetl liste
    2. Dodaj do listy
    3. Usun indeks z listy
    4. Zapisz liste
    5. Zakończ program
    """)
    try:
        chosen_operation = int(input("Podaj numer operacji: "))
    except ValueError:
        continue
    if chosen_operation == 1:
        pokaz(lista)
    if chosen_operation == 2:
        dodaj(lista)
    if chosen_operation == 3:
        usun(lista)
    if chosen_operation == 4:
        zapisz(lista)
print("Koniec programu")
