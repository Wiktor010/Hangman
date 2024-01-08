import random
a = ['drzewo', 'warzywa', 'owoce', 'gruszka', 'jajka', 'lalka', 'magnolia', 'kaktus', 'trawa',
     'sasanka', 'indyk', 'jaguar', 'kura', 'informatyk', 'nauczyciel', 'tancerz', 'chomik', 'dzik', 'delfin',
     'analityk', ' grafik', 'automatyk', 'ananas', 'banan', 'aparat']

b = ['komputer', 'lekkoatletyka', 'gimanstyka', 'matematyka', 'instrument', 'karabin', 'okulary',
     'niezapominajka', 'pelargonia', 'tulipan', 'nietoperz', 'orka', 'pelikan',
     'jubiler', 'kamieniarz', 'ogrodnik', 'grzyb', 'elektryk', 'antylopa', 'cebula', 'gazeta',
     'chiny', 'szafa', 'kaczka', 'dach']

c = ['dom', 'ul', 'kij', 'gra', 'kret', 'megafon', 'ubikacja', 'rewolwer', 'iksja', 'klimek', 'rogownica',
     'modliszka', 'rybitwa', 'tarantula', 'lakiernik', 'magazynier', 'recepcjonista',
     'encyklopedia', 'herbata', 'garnitur', 'gorczyca', 'gawron', 'gepard', 'tygrys', 'budowlaniec']

x = 0
zapisane = [" ", None , " "]
wygrane = 0
przegrane = 0

def losowanie(y):
        print("latwy = a\n"
              "sredni = b\n"
              "trudny = c\n"
              "Wybierz poziom trudnosci: ")
        poziom = input()

        while poziom != "a" and poziom != "b" and poziom != "c":
            print("Niepoprawny poziom\n"
                  "latwy = a\n"
                  "sredni = b\n"
                  "trudny = c\n"
                  "Wybierz poziom trudnosci: ")
            poziom = input()
        else:
            if poziom == 'a':
                haslo = str(a[random.randint(0, len(a) - 1)])
            elif poziom == 'b':
                haslo = str(b[random.randint(0, len(b) - 1)])
            elif poziom == 'c':
                haslo = str(c[random.randint(0, len(c) - 1)])
            else:
                print("Błędny poziom trudności")
                return 0
            tablica = list(haslo)
            for i in range(len(haslo)):
                tablica[i] = '_'
            wylosowane = [haslo, tablica]
            return wylosowane


def gra(haslo, tablica, zycia):
    wynik = 0
    while zycia > 0:
        print("Pozostało ci", zycia, "żyć",
        wisielec(zycia), "\n",
        ' '.join(tablica), "\n",
        "Podaj literę albo napisz ZAPISZ, aby wyjść do menu: ")

        litera = input()
        if litera == "ZAPISZ":
            zapisz(tablica, zycia, haslo)
            wynik =-1
            return wynik
        else:
            if litera in haslo:
                for i in range(len(haslo)):
                    if (haslo[i] == litera):
                        tablica[i] = litera
                if ''.join(map(str, tablica)) == haslo:
                    print(wisielec(zycia))
                    print("Pozostało ci", zycia, "żyć\n")
                    print(' '.join(tablica))
                    print("Wygrałeś!!!\n")
                    wynik += 1
                    global zapisane
                    zapisane = [" ", None , " "]
                    return wynik
            else:
                zycia -= 1
    else:
        print(wisielec(zycia),
            "Przegrałeś!!!\n",
            "Hasło to:", haslo, "\n")
        zapisane = [" ", None, " "]
        return wynik


def wisielec(zycia):
    if zycia == 7:
        print('________\n'
        ' |   |\n'
        '     |\n'
        '     |\n'
        '     |\n'
        '     |\n'
        '_____|___\n'
        '')
    elif zycia == 6:
        print('________\n'
              ' |   |\n'
              ' 0   |\n'
              '     |\n'
              '     |\n'
              '     |\n'
              '_____|___\n'
              '')
    elif zycia == 5:
        print('________\n'
              ' |   |\n'
              ' 0   |\n'
              ' |   |\n'
              '     |\n'
              '     |\n'
              '_____|___\n'
              '')
    elif zycia == 4:
        print('________\n'
              ' |   |\n'
              ' 0   |\n'
              '/|   |\n'
              '     |\n'
              '     |\n'
              '_____|___\n'
              '')
    elif zycia == 3:
        print('________\n'
              ' |   |\n'
              ' 0   |\n'
              '/|\  |\n'
              '     |\n'
              '     |\n'
              '_____|___\n'
              '')
    elif zycia == 2:
        print('________\n'
              ' |   |\n'
              ' 0   |\n'
              '/|\  |\n'
              ' |   |\n'
              '     |\n'
              '_____|___\n'
              '')
    elif zycia == 1:
        print('________\n'
              ' |   |\n'
              ' 0   |\n'
              '/|\  |\n'
              ' |   |\n'
              '/    |\n'
              '_____|___\n'
              '')
    elif zycia == 0:
        print('________\n'
              ' |   |\n'
              ' 0   |\n'
              '/|\  |\n'
              ' |   |\n'
              '/ \  |\n'
              '_____|___\n'
              '')
    return ''


def statystyki(y, wins, loses):

    if wins + loses == 0:
        print("\nBrak statystyk!\n")
    else:
        print("\nIlość wygranych gier:", wins)
        print("Ilość wszystkich gier:", wins + loses)
        print("Procent wygranych gier:", wins * 100/(wins + loses), "%\n")


def zapisz(tablica, zycia, haslo):
    global zapisane
    zap_tablica = tablica
    zap_haslo = haslo
    zap_zycia = zycia
    zapisane = [zap_haslo, zap_zycia, zap_tablica]
    #menu(x)


def komenda(y):
    if y == 0:
        print('Zagraj = 1 \n'
              'Pokaż statystyki = 2 \n'
              'Wczytaj = 3 \n'
              'Zakończ = 4 \n'
              'Co chcesz zrobić?')
    k = input()
    return k


def menu(y):
    global wygrane
    global przegrane
    global zapisane
    has: str = ""
    tab: str = ""
    k = komenda(y)
    while k!=1 or k!=2 or k!=3 or k!=4:
        if k == '1':
            wylosowane = losowanie(x)
            has = wylosowane[0]
            tab = wylosowane[1]
            w = gra(has, tab, 7)
            if w == 1:
                wygrane += 1
                k = komenda(y)
            elif w == 0:
                przegrane += 1
                k = komenda(y)
            elif w == -1:
                k = komenda(y)
            else:
                print("Błąd")
                return 0

        elif k == '2':
            statystyki(y, wygrane, przegrane)
            k = komenda(y)

        elif k == '3':
            has = zapisane[0]
            tab = zapisane[2]
            zyc = zapisane[1]
            if zapisane == [" ", None , " "]:
                print("Brak gry do wczytania\n")
                k = komenda(y)
            else:
                w = gra(has, tab, zyc)
                if w == 1:
                    wygrane += 1
                    zapisane = [" ", None, " "]
                    k = komenda(y)
                elif w == 0:
                    przegrane += 1
                    zapisane = [" ", None, " "]
                    k = komenda(y)
                elif w == -1:
                    k = komenda(y)
                else:
                    print("Błąd")
                    return 0

        elif k == '4':
            if zapisane == [" ", None , " "]:
                print("GAME OVER")
                return 0
            else:
                print("GAME OVER")
                break

        else:
            print("Błędna komenda!")
            k = komenda(y)
    else:
            print("Błędna komenda!")
            menu(y)


def main():
    menu(x)
    return 0

main()
