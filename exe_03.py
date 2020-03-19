import  random
numeros = list()


def sorteia():
    for n in range(0, 5):
        x = random.randint(0,10)
        numeros.append(x)


def somaPar():
    soma=0
    for n in numeros:
        if n%2 == 0:
            soma += n
    print(f'A soma dos pares e: {soma}')


sorteia()
print(numeros)
somaPar()