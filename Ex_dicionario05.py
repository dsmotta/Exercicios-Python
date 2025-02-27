

pessoa = dict()
lista = list()
soma = meida = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo (M / F): ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite  apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
       
    lista.append(pessoa.copy())
   
    while True:
        resp = str(input('Deseja continuar cadastro? (S/N)')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N')
    if resp == 'N':
        break

print('-='*30)
print(f'\n* Pessoas Cadastradas {len(lista)}')
media = soma / len(lista)
print(f'\n* Media de idades: {media:5.2f} anos ')
print(f'\n* Mulheres cadastradas: ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'- {p["nome"]}  ', end='')
print()
print(f'\n>>> Lista pessoas idade acima da media: <<<')
for p in lista:
    if p['idade'] >= media:
        print('       ')
        for k, v in p.items():
            print(f' {k}: {v}')

print(lista)