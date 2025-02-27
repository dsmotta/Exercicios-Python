lista = []

while True:
    n = int(input(f'Digite um valor: '))
    if n in lista:
        print(f'Numero {n} ja foi adcionado! Não pode ser duplicado!' )
    else:
        lista.append(n)
        print('Acionado com sucesso...')

    r = str(input('continuar? [S/N]'))
    if r in 'Nn':
        break
print(f'Lista criada e ja ordenada: {sorted(lista)}')

