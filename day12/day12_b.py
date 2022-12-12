def find_path(M, start, end, next_condition):
    queue, visited = [(*start, 0)], []
    while queue:
        x, y, length = queue.pop(0)
        if (x, y) in visited:
            continue
        if M[x][y] == end:
            return length
        visited.append((x, y))
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < len(M) and 0 <= j < len(M[0]):
                if next_condition(M, x, y, i, j):
                    queue.append((i, j, length + 1))

if __name__ == "__main__":
    M = open("input.txt").read().splitlines()
    start_S = next(((i, row.index("S")) for i, row in enumerate(M) if "S" in row))
    start_E = next(((i, row.index("E")) for i, row in enumerate(M) if "E" in row))
    def part1(M, from_x, from_y, to_x, to_y):
        my_order = M[from_x][from_y] if M[from_x][from_y] != "S" else "z"
        order = M[to_x][to_y] if M[to_x][to_y] != "E" else "z"
        return ord(order) <= ord(my_order) + 1
    def part2(M, from_x, from_y, to_x, to_y):
        my_order = M[from_x][from_y] if M[from_x][from_y] != "E" else "z"
        order = M[to_x][to_y] if M[to_x][to_y] != "S" else "z"
        return ord(order) + 1 >= ord(my_order)
    print(find_path(M, start_S, "E", part1))
    print(find_path(M, start_E, "a", part2))