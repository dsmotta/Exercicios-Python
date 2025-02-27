numeros = []
pares = []
impares = []

while True:
    n = int(input(f'Digite um numero: '))
    numeros.append(n)
    if n % 2 ==0:
        pares.append(n)
    else:
        impares.append(n)

    print('Adcionado com sucesso!')
    r = str(input(f'Deseja digitar outro? [S/N]'))
    if r in ('Nn'):
        break      

print(numeros)
print(pares)
print(impares)