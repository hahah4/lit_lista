n = list()
for c in range(0, 5):

    adc = int(input(f'Digite o {c} numero inteiro:'))

    if c == 0 or adc > n[-1]:
        n.append(adc)
    else:
        caca_num =0 #aqui e onde a magica acontece
        for caca_num in range(0, len(n)):
            if adc <= n[caca_num]:
                n.insert(caca_num, adc)
                break
            caca_num += 1 #faz com q ele incremente sempre 1 no qual sera comparada no proximo for
                          #esse incremento aconte sempre que a condição n for satisfeta e o bloco para
                          # e começa de novo, porem vai comparar sempre a proxima posicao
print(n)