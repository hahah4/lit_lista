p = {}
banco =[]
soma_idades = 0
guarda_pos= 0
total_m = 0
for c in range(1, 5):

    p['nome'] = str(input(f'Digite o nome da {c}a pessoa:'))
    p['idade'] = int(input(f'Digite a idade da {c}a pessoa:'))

    soma_idades += p['idade']
    while True:
        p['sexo'] = str(input(f'Digite o sexo (M ou F) da {c}a pessoa:')).upper()

        if p['sexo'] in 'FM':
            break
        print('Digite apenas M ou F!')

    if p['sexo'] == 'M':
        guarda = p['idade']
        if guarda > guarda_pos:
            guarda_pos = guarda
            guarda_nome = p['nome']
    if p['sexo'] == 'F':
        guarda_m = p['idade']
        if guarda_m < 20:
            total_m += 1


    banco.append(p.copy())
total_pessoas = len(banco)
media_idades = soma_idades / total_pessoas




#print(banco)
print('')
print(f'A media de idade do grupo e: {media_idades}')
print(f'O nome do homi mais velho e: {guarda_nome}, e sua idade e: {guarda_pos} anos')
print(f'O total de mulheres com menos de 20 anos e:{total_m}')

