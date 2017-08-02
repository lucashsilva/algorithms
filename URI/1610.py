def cycled(g, start, total):
    visited = [ False for i in range(total+1) ]
    stack = []
    stack.append(start)

    while stack:
        top = stack.pop()
        
        if not visited[top]:
            visited[top] = True

            for v in g[top]:
                stack.append(v)    
        else:
            return True
    return False
        
		
t = int(raw_input())

for i in range(t):
    n, m = map(int, raw_input().split())
    graph = [[] for i in range(n+1)]

    for i in range(m):
        a, b = map(int, raw_input().split())
        graph[a].append(b)

    if cycled(graph, a, n):
        print "SIM"
    else:
        print "NAO"