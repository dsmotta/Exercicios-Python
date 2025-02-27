from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira Trabalho (0 para nao tenho): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + dados['contratacao'] + 35 - datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor{v} ')

