'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string
koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

string = input('Unesite string: ')
pattern = r'^M.*[0-5].*K$'
match = re.search(pattern, string)

if match:
    print("Podudaranje!", match.group())
else:
    print("Nema podudaranja.")
