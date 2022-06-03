from itertools import count
from unicodedata import numeric


palavra_passe = []
escolha_da_palavra = input('Digite sua palavra chave: ')
dica_um = input('Digitea primeira dica: ')
dica_dois = input('Digitea segunda dica: ')
dica_treis = input('Digitea terceira dica: ') 

palavra_passe.append(escolha_da_palavra)


while True:
    for range in palavra_passe:
        numero_asterisco = len(palavra_passe[0]) * '*' 
        print(numero_asterisco)

