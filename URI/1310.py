while True:
    try:
        n = int(raw_input())
        custo_dia = int(raw_input())

        lucros = [] 

        resp = 0
        maior = 0

        for i in range(n):
            lucro_atual = int(raw_input()) - custo_dia
            maior = max(0, maior + lucro_atual)

            resp = max(resp, maior)
        

        print resp

    except EOFError:
        break
