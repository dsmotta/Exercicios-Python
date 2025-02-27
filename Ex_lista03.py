lista = []
cont = 0

while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print(f'Ja digitado ! nao pode ser duplicado!')
    else:
        lista.append(n)
        cont +=1
        print('Adcionado com sucesso')
    r = str(input('Deseja finalizar? [S/N]'))
    if r in 'Ss':
        break
print(f'\nNumeros digitados: {lista}')
print(f'Quantidade de numeros digitados: {cont}')
lista.sort(reverse=True)
print(f'Numeros digitados ordenados: {lista}')
if 5 in lista:
    print(f'Numero 5 foi digitado e adcionado na lista!')
else:
    print(f'Numero 5 nao esta na lista!')