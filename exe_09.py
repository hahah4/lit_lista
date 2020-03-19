lnotas = list()
dnotas = dict()
soma = 0
anota = 0
def notas(n):
    lnotas.append(n)
    media = soma/len(lnotas)
    dnotas['Quantidade de notas:'] = len(lnotas)
    maior = max(lnotas)
    menor = min(lnotas)
    dnotas['Maior nota'] = maior
    dnotas['Menor nota'] = menor
    dnotas['Media da turma'] = media


while True:
    nota = float(input('Digite a nota:'))
    soma += nota
    notas(nota)
    op = str(input('Deseja continuar? S / N :')).upper()
    if op == 'S':
        continue
    else:
        break
print(lnotas)
print(dnotas)