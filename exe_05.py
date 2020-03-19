n = int(input('Digite um número inteiro:'))
if n == 1:
    print('1 não e um número primo.')
elif n == 2:
    print('2 é um numero primo')
else:
    s=0
    for v in range(2, 10):
        if v == n:
            continue
        if n % v != 0:
            s += 1
            if s == 7:
                print(f'{n} é um numero Primo.')
        else:
            print(f'{n} nao e um numero Primo.')
            break




