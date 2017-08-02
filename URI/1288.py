casos = int(raw_input())

for k in range(casos):
    poderes = [0]
    pesos = [0]
 
    n = int(raw_input())

    for i in range(n):
        poder, peso = map(int, raw_input().split())
        poderes.append(poder)
        pesos.append(peso)

    capacidade = int(raw_input())
    resistencia = int(raw_input())

    t = [[0 for col in range(capacidade+1)] for row in range(n+1)]

    for i in range(1, n+1):
        for b in range(1, capacidade+1):
            if pesos[i] > b:
                t[i][b] = t[i-1][b]
            else:
                t[i][b] = max(t[i-1][b], t[i-1][b-pesos[i]] + poderes[i])

    if t[n][capacidade] >= resistencia:
        print "Missao completada com sucesso"
    else:
        print "Falha na missao"

