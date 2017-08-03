import string
import sys

def dfs(graph, v, visited, path):
    visited.add(v)
    path.append(v)

    for adj in graph[v]:
        if adj not in visited:
            dfs(graph, adj, visited, path)

n = int(raw_input())

for i in range(n):
    graph = {}
    visited = set()
    v, e = map(int, raw_input().split())

    for j in range(v):
        graph.update({ string.ascii_lowercase[j]: [] })

    for k in range(e):
        v1, v2 = raw_input().split()
        graph[v1].append(v2)
        graph[v2].append(v1)

    connected_components = 0

    print "Case #%d:" % (i + 1)
    paths = []

    for v in graph:
        if v not in visited:
            path = []
            dfs(graph, v, visited, path)
            connected_components += 1
            
            path.sort()
            paths.append(path)
    
    paths.sort(key=lambda x: x[0])
    for path in paths:
        for v in path:
            sys.stdout.write("%s," % v)
        print

    print "%d connected components" % connected_components
    print