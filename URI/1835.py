def dfs(graph, v, visited):
    visited.add(v)

    for adj in graph[v]:
        if adj not in visited:
            dfs(graph, adj, visited)


t = int(raw_input())

for i in range(t):
    entrada = map(int, raw_input().split())
    if len(entrada) == 2:
        n = entrada[0]
        m = entrada[1]
    else:
        n = entrada[0]
        m = int(raw_input())

    graph = {k: set() for k in range(1, n+1)}
    
    for j in range(m):
        x, y = map(int, raw_input().split())

        graph[x].add(y)
        graph[y].add(x)

    visited = set()

    count = 0
    for v in graph:
        if v not in visited:
            count += 1
            dfs(graph, v, visited)
    
    if count == 1:
        print "Caso #%d: a promessa foi cumprida" % (i + 1)
    else:
        print "Caso #%d: ainda falta(m) %d estrada(s)" % ((i + 1), (count - 1))
