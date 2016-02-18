import resource, sys
#.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
global t
global s
global length
length = 0

def dfs_loop(graph, ft=None):
    global t
    t = 0

    vertixes = {}
    finish_time = {}
    #length = 875714
    #length = len(graph)
    for i in range(length, 0, -1):
        if ft:
            i = ft[i]
        if i not in vertixes:
            vertixes[i] = {}
        if "v" not in vertixes[i]:
            global s
            s = i
            dfs(graph, i, vertixes, finish_time)

    return finish_time, vertixes

def dfs(graph, i, vertixes, finish_time=None):
    global t
    global s

    vertixes[i]["v"] = True
    vertixes[i]["l"] = s
    if i in graph:
        for j in graph[i]:
            if j not in vertixes:
                vertixes[j] = {}
            if "v" not in vertixes[j]:
                dfs(graph, j, vertixes, finish_time)
    t = t + 1

    finish_time[t] = i

graph = {}
graph_reversed = {}
filename = "SCC.txt"

with open(filename, "r") as f:
    for line in f:
        tail, head = (int(x) for x in line.split())

        if tail > length:
            length = tail
        if head > length:
            length = head

        if tail in graph:
            graph[tail].append(head)
        else:
            graph[tail] = [head]

        if head in graph_reversed:
            graph_reversed[head].append(tail)
        else:
            graph_reversed[head] = [tail]



ft, vt = dfs_loop(graph_reversed)
_, vt = dfs_loop(graph, ft)
scc = {}
for k in vt:
    i = vt[k]["l"]
    if i in scc:
        scc[i] = scc[i] + 1
    else:
        scc[i] = 1
print scc

