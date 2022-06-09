from itertools import count
from unicodedata import numeric
import os


escolha_da_palavra = input('Digite sua palavra chave: ')
dica_um = input('Digitea primeira dica: ')
dica_dois = input('Digitea segunda dica: ')
dica_treis = input('Digitea terceira dica: ') 



dica = -1
erros = -1
acertos = 0
letras = []
asteriscos = []
letra_correta = 0

os.system ('cls')

for range in escolha_da_palavra:
    numero_asterisco = len(escolha_da_palavra) * '*' 
    asteriscos.append(numero_asterisco)
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
    print(letras)
    if letras[-1] in escolha_da_palavra:
        print('Letra certa!')
        letra_correta += 1
        numero_de_letras = len(asteriscos)
        lugar_da_letra = escolha_da_palavra.index(letras[-1])
        asteriscos.insert(lugar_da_letra, letras[-1])
        ultima_da_lista = len(asteriscos) -1
        ultima_letra = asteriscos[ultima_da_lista]
        asteriscos.remove(ultima_letra)
        print(asteriscos)
        if letra_correta == numero_de_letras:
            print('Você venceu!!')
            input()
            break
    else:
        print('Letra errada!')
        erros += 1
        if erros == 5:
            print('Você perdeu!') 
            input()
            break