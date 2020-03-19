pessoas = list()
pessoa = dict()
lista_mulheres = list()
lista_idade_acima_mda = list()
soma_idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome:'))
    pessoa['idade'] = int(input('Digite a idade:'))
    soma_idade += pessoa['idade']

    pessoa['sexo'] = str(input('Digite o sexo M/masculino - F/feminino:')).upper()
    op = str(input('Deseja continuar? Digite: S - Sim e N - Nao:')).upper()
    while True:
        if pessoa['sexo'] not in 'MF':
            pessoa['sexo'] = str(input('Digite apenas M ou F:')).upper()
        else:
            break
    pessoa.copy()
    pessoas.append(pessoa.copy())
    if op == 'N':
        break
    else:
        continue

media_idade = soma_idade / len(pessoas)

for p in pessoas:
    if p['sexo'] in 'F':
        lista_mulheres.append(p['nome'])
for p in pessoas:
    if p['idade'] > media_idade:
        lista_idade_acima_mda.append(p['nome'])

print(pessoas)
print(f'A media das idades e: {media_idade:02.2f} anos.')
print(f'O total de pessoas cadastradas foram: {len(pessoas)} pessoas.')
print(f'As mulheres sao: {lista_mulheres}')
print(f'As pessoas com a idade acima da media sao: {lista_idade_acima_mda}')



