# fun.py

def dodawanie(a, b):
    return a + b

def odniemanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b


def imie(x):
    return x

def lista(liczby):
    return list(range(1, liczby+1))

#zad4
def oblicz(func, x, y):
    return func(x, y)





#zad3
globalna = 10
def my_function(localna):
    global globalna
    print("Wartość zmiennej globalnej:", globalna)
    print("Wartość zmiennej lokalnej:", localna)

    globalna1 = globalna
    globalna1 += localna
    print(f"Dodawanie globalnej i lokalnej:{globalna} + {localna} = ", globalna1)
