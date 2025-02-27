jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar (S/N)')).upper()[0]
        if resp in ('SN'):
            break
        print('>> ERRO << DIGITE S/N')
    if resp in 'N':
        break
print('-/'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-/'*30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para finalizar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('>> ERRO << Jogador não cadastradp!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g}')
    print('-'*30)
print('<> FINALIZADO <>')       