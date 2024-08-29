'''
Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.

'''

def funkcija(string):
    if len(string) == 0:
        return
    else:
        print(string[-1], end='')
        funkcija(string[:-1])

string_ = input("Unesite string: ")
funkcija(string_)
