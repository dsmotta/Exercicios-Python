listanum = []
maior = 0
menor = 0

for i in range(0,5):
    listanum.append(int(input(f'Digite o valor da posião {i} :')))
    if i == 0:
        maior = menor = listanum[i]
    else:
        if  listanum[i] > maior:
            maior = listanum[i]
        if listanum[i] < menor:
            menor = listanum[i]

print('=-' * 30)
print(f'Digitados: {listanum}')
print(f'Maior: {maior} posição: ', end='')

for c,v in enumerate(listanum):
    if v == maior:
        print(f'{c}... ', end='')
print()

print(f'\nMenor: {menor} posição: ', end='')
for c,v in enumerate(listanum):
    if v == menor:
        print(f'{c}... ', end='')



    