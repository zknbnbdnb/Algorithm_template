# @Time    : 2021/12/28 19:44
# @Author  : 康带帅
# @FileName: 最短路径算法.py
# @Software: PyCharm
# @Blog    ：https://github.com/zknbnbdnb

MAX = float('inf')
graph = [
    [0, 2, 1, MAX, MAX, MAX, MAX, 23],
    [MAX, 0, MAX, 3, MAX, MAX, MAX, MAX],
    [MAX, MAX, 0, MAX, 6, MAX, MAX, MAX],
    [MAX, MAX, MAX, 0, 2, MAX, MAX, MAX],
    [MAX, MAX, MAX, MAX, 0, 10, 6, MAX],
    [MAX, MAX, MAX, MAX, MAX, 0, MAX, 7],
    [MAX, MAX, MAX, MAX, MAX, MAX, 0, 9],
    [MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0],
]

def floyd(graph):
    dp = graph
    n = len(dp)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    return dp

print(floyd(graph))