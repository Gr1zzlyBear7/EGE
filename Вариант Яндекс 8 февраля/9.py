data = [list(map(int, line.split())) for line in open('9.txt')]
total_sum = 0
neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]
for i in range(len(data)):
    for j in range(len(data[i])):
        current_value = data[i][j]
        neighbor_values = []
        for dx, dy in neighbors:
            x, y = i + dx, j + dy
            if 0 <= x < len(data) and 0 <= y < len(data[i]):
                neighbor_values.append(data[x][y])
        if neighbor_values:
            if current_value >= max(neighbor_values) and current_value in neighbor_values:
                total_sum += current_value
print({total_sum})