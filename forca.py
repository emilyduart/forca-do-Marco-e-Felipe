from itertools import count
from unicodedata import numeric


palavra_passe = []
escolha_da_palavra = input('Digite sua palavra chave: ')
dica_um = input('Digitea primeira dica: ')
dica_dois = input('Digitea segunda dica: ')
dica_treis = input('Digitea terceira dica: ') 

palavra_passe.append(escolha_da_palavra)

dica = -1

for range in palavra_passe:
    numero_asterisco = len(palavra_passe[0]) * '*' 
    print(numero_asterisco)
while True:
    print('(1) Escolher uma letra.')
    print('(2) veja uma dica.')
    opicao = int(input('Escolha uma opição: '))
    if opicao == 1:
        letra_ecolhilda = input('Escolha uma letra: ')
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
        letra_ecolhilda = input('Escolha uma letra: ')
    else:
        print('Opição invalida!')
        break