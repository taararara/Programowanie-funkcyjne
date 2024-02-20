import fun
#zad pierwsze i drugie
print(fun.dodawanie(4,2))
print(fun.odniemanie(4,2))
print(fun.mnozenie(4,2))
print(fun.dzielenie(4,2))
print(fun.imie('Taras'))

#zad3
fun.my_function(6)

#zad4
wynik1 = fun.oblicz(fun.dodawanie, 3, 5)
print(wynik1)

#zad5
def liczby_nieparzyste(lista):
    return [liczba for liczba in lista if liczba % 2 != 0]
liczby = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nieparzyste = liczby_nieparzyste(liczby)
print("Liczby nieparzyste:", nieparzyste)
