entrada = raw_input()

while entrada != "0":
    tempos = [0]
    n_pizzas = [0]
 
    n = int(entrada)
    max_pizzas = int(raw_input())

    for i in range(n):
        tempo_pedido, n_pizzas_pedido = map(int, raw_input().split())
        tempos.append(tempo_pedido)
        n_pizzas.append(n_pizzas_pedido)

    t = [[0 for col in range(max_pizzas+1)] for row in range(n+1)]

    for i in range(1, n+1):
        for b in range(1, max_pizzas+1):
            if n_pizzas[i] > b:
                t[i][b] = t[i-1][b]
            else:
                t[i][b] = max(t[i-1][b], t[i-1][b-n_pizzas[i]] + tempos[i])

    print "%d min." % (t[n][max_pizzas])
    entrada = raw_input()

