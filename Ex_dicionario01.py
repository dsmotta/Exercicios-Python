aluno = {}
aluno['nome'] = str(input('Digite nome: '))
aluno['media'] = float(input('Digite a média: '))

print(f'Nome é igual a: {aluno["nome"]}')
print(f'Media é igual a: {aluno["media"]}')

if aluno["media"] >= 5:
    print('Situação Aprovado!')
else:
    print('Situação Reprovado!')