pessoas = []
pessoa = []
mais_pesadas = list()
mais_leves = list()
soma = 0

while True:
    pessoa.clear()
    n = str(input('Nome:'))
    pessoa.append(n)

    p = float(input('Peso:'))
    soma += p
    pessoa.append(p)
    pessoas.append(pessoa.copy())
    opcao = str(input('Deseja cadastrar mais alguem? Digite S/N para Sim ou Não:')).upper()
    if opcao == 'S':
        continue
    else:
        break

media = soma / len(pessoas)

for pesso in pessoas:
    if pesso[1] >= media:

        mais_pesadas.append(pesso)

    else:

        mais_leves.append(pesso)

print(f'O total de pessoas cadastradas foram: {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas são: {mais_pesadas}')
print(f'As pessoas mais leves são: {mais_leves}')
