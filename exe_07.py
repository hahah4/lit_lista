from moeda import aumentar, metade, diminuir, dobro

quant = float(input('Digite a quantidade de moedas:'))

while True:
    opcoes = int(input('Escolha uma das opções a baixo:\n'
                       '1- Aumentar\n'
                       '2- Diminuir\n'
                       '3- Dobro\n'
                       '4- Metade\n'
                       '0- Sair\n'))

    if opcoes == 1:
        aumentar(quant)
    elif opcoes == 2:
        diminuir(quant)
    elif opcoes == 3:
        dobro(quant)
    elif opcoes == 4:
        metade(quant)
    elif opcoes == 0:
        break
