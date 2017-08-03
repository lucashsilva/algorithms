import sys 

n, d = map(int, raw_input().split())

while n != 0 and d != 0:
    numero = raw_input()
    apagados = 0
    pilha = []
    tamanho_pilha = 0

    for num in numero:
        while tamanho_pilha > 0 and int(num) > int(pilha[-1]) and apagados < d:
            pilha.pop()
            tamanho_pilha -=1 
            apagados += 1

        
        if tamanho_pilha < n - d:
            pilha.append(num)
            tamanho_pilha += 1

    for el in pilha:
        sys.stdout.write(el)
    print
    n, d = map(int, raw_input().split())