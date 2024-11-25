from collections import deque


def bfs(start, target, n, m):
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    while queue:
        x, y, moves = queue.popleft()
        if (x, y) == target:
            return moves
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            while 1 <= new_x <= n and 1 <= new_y <= m:
                if (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, moves + 1))
                    visited.add((new_x, new_y))
                new_x += dx[i]
                new_y += dy[i]
    return float('inf')


def process_queries(n, m, queries):
    elephants = set()
    results = []
    for query in queries:
        if query[0] == 1:
            x, y = query[1], query[2]
            elephants.add((x, y))
        elif query[0] == 2:
            x, y = query[1], query[2]
            elephants.remove((x, y))
        elif query[0] == 3:
            x, y = query[1], query[2]
            min_moves = float('inf')
            for elephant in elephants:
                moves = bfs(elephant, (x, y), n, m)
                if moves < min_moves:
                    min_moves = moves
            if min_moves == float('inf'):
                results.append(-1)
            else:
                results.append(min_moves)
    return results


n, m = map(int, input().split())
q = int(input())
queries = []
for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)
results = process_queries(n, m, queries)
for result in results:
    print(result)