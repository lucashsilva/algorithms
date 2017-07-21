entrada = raw_input()

while entrada != "0":
    pesos = [0]
    valores = [0]
 
    n = int(entrada)

    for i in range(n):
        p, P = map(int, raw_input().split())
        valores.append(p)
        pesos.append(P)

    c = int(raw_input())

    t = [[0 for col in range(c+1)] for row in range(n+1)]

    for i in range(1, n+1):
        for b in range(1, c+1):
            if pesos[i] > b:
                t[i][b] = t[i-1][b]
            else:
                t[i][b] = max(t[i-1][b], t[i-1][b-pesos[i]] + valores[i])

    print t[n][b]
    entrada = raw_input()

