from collections import defaultdict

n, k = map(int, input().split())


def count_k_length_paths(n, k, arr):
    graph = defaultdict(list)
    for u, v in arr:
        graph[u].append(v)
        graph[v].append(u)
    count = 0

    def dfs(node, depth, was):
        nonlocal count
        if depth == k:
            count += 1
            return
        for neighbor in graph[node]:
            if neighbor not in was:
                was.add(neighbor)
                dfs(neighbor, depth + 1, was)
                was.remove(neighbor)

    for start in range(1, n + 1):
        was = {start}
        dfs(start, 1, was)
    return count // 2


arr = [tuple(map(int, input().split())) for i in range(n - 1)]
print(count_k_length_paths(n, k, arr))