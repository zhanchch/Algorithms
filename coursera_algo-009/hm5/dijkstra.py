#import resource, sys
#setrlimit(resource.RLIMIT_STACK, (2**29,-1))
#sys.setrecursionlimit(10**6)

from heapq import heappush, heappop

def dijkstra(graph, start):
    #shortest distance
    sd = {}
    visited = set()

    for k in graph.keys():
        sd[k] = 1000000

    sd[start] = 0
    Q = {[0, start]}

    while Q:
        cost, v = heappop(Q)

        if v in visited:
            continue

        sd[v] = cost
        visited.add(v)

        for u in graph[v].keys():
            if u not in visited:
                heappush(Q, [cost + graph[v][u], u])
            elif

#graph = {}
#graph_reversed = {}
#filename = "test1.txt"

#with open(filename, "r") as f:
#    for line in f:
#        tail, head = (int(x) for x in line.split())
