from random import randint

lista = []
jogos = []

print('-*'*20)
print('CRIANDO PALPITES PARA JOGOS DA MEGASENA')
print('-*'*20)

while True:
    quant = int(input('\nDigite a quantidade de jogos: '))
    total = 0 

    while quant > total:
        cont = 0
        while True:
            num = randint(1,60)
            if num not in lista:
                lista.append(num)
                cont +=1
            if cont >= 6:
                break    
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        total += 1

    print()
    print ('-='*3, f'SORTEANDO {quant} JOGOS:', '-='*3)
    print()
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1} : {l}')

    resp = str(input('\nDeseja sair?? [S/N]'))
    if resp in ('Ss'):
        break
    else:
        jogos.clear()
        lista.clear()
        total = 0

print('\n##### BOA SORTE ####')