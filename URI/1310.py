def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(0, max_so_far, max_ending_here)
    return max_so_far

while True:
    try:
        n = int(raw_input())
        custo_dia = int(raw_input())

        lucros = [] 

        for i in range(n):
            lucros.append(int(raw_input()) - custo_dia)
        

        print max_subarray(lucros)

    except EOFError:
        break
