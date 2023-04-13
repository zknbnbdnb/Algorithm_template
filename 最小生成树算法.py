# @Time    : 2021/12/28 21:05
# @Author  : 康带帅
# @FileName: 最小生成树算法.py
# @Software: PyCharm
# @Blog    ：https://github.com/zknbnbdnb

MAX = float('inf')
graph = [
    [MAX, 6, 6, MAX, MAX, 1],
    [6, MAX, MAX, 6, MAX, 2],
    [6, MAX, MAX, MAX, 2, 4],
    [MAX, 6, MAX, MAX, 2, 3],
    [MAX, MAX, 2, 2, MAX, 1],
    [1, 2, 4, 3, 1, MAX],
]

def prim(graph):
    def min_edge(a, b, graph):
        min_wight = MAX
        for i in a:
            for j in b:
                if min_wight > graph[i][j]:
                    min_wight = graph[i][j]
                    v, u = i, j
        return v, u
    vet_num = len(graph)
    a = [0]
    b = [i for i in range(vet_num) if i not in a]
    edge = []
    for i in range(1, vet_num):
        v, u = min_edge(a, b, graph)
        edge.append((v, u))
        a.append(u)
        b.remove(u)
    return edge

print(prim(graph))