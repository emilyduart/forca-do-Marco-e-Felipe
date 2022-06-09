from itertools import count
from unicodedata import numeric
import os


escolha_da_palavra = input('Digite sua palavra chave com um espaço: ')
dica_um = input('Digitea primeira dica: ')
dica_dois = input('Digitea segunda dica: ')
dica_treis = input('Digitea terceira dica: ') 



dica = -1
erros = -1
acertos = 0
letras = []

os.system ('cls')

for range in escolha_da_palavra:
    numero_asterisco = len(escolha_da_palavra) * '*' 
    print(numero_asterisco)
while True:
    print('(1) Escolher uma letra.')
    print('(2) veja uma dica.')
    opicao = int(input('Escolha uma opição: '))
    if opicao == 1:
        letra_escolhilda = input('Escolha uma letra: ')
        letras.append(letra_escolhilda)
    elif opicao == 2:
        dica += 1
        if dica == 0:
            print(dica_um)
        elif dica == 1:
            print(dica_dois)
        elif dica == 2:
            print(dica_treis)
        else:
            print('Acabou as dicas!')
        letra_escolhilda = input('Escolha uma letra: ')
        letras.append(letra_escolhilda)
    else:
        print('Opição invalida!')
        break
    print(letras)
    if letras[-1] in escolha_da_palavra:
        print('Letra certa!')
    else:
        print('Letra errada!')
        erros += 1
        if erros == 5:
            print('Você perdeu!') 
            input()
            break