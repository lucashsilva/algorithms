def solution(N):
    max_gap = 0
    actual_gap = 0

    # skip tailing 0s
    while N > 0 and N % 2 == 0:
        N //= 2
    
    while N > 0:
        r = N % 2
        N //= 2
    
        if r == 1:
            if actual_gap > max_gap:
                max_gap = actual_gap
            actual_gap = 0
        elif r == 0:
            actual_gap += 1
    return max_gap