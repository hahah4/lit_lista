
def diminuir(n):
    porcent = float(input('Deseja diminuir as moedas em quantos %?:'))
    nova_quant = n - ((porcent / 100) * n)
    print(f'voce possui agora {nova_quant} moedas.')
    print('*' * 50)
def aumentar(n):
    porcent = float(input('Deseja aumentar as moedas em quantos %?:'))
    nova_quant = ((porcent/100) + 1) * n
    print(f'voce possui agora {nova_quant} moedas.')
    print('*'*50)

def dobro(n):
    d = n*2
    print(f'O dobro de {n} e : {d}')
    print('*' * 50)

def metade(n):
    m = n/2
    print(f'A metade de {n} e : {m}')
    print('*' * 50)
