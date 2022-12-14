if __name__ == "__main__":
    map = open("input.txt").read().splitlines()
    start = next((i, j) for i in range(len(map)) for j in range(len(map[0])) if map[i][j] == "S")
    queue, visited = [(*start, 0)], []
    while queue:
        x, y, length = queue.pop(0)
        if (x, y) in visited:
            continue
        if map[x][y] == "E":
            print(length)
            break
        visited.append((x, y))
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < len(map) and 0 <= j < len(map[0]):
                order = ord(map[i][j] if map[i][j] != "E" else "z")
                my_order = ord(map[x][y] if map[x][y] != "S" else "z") + 1
                if order <= my_order:
                    queue.append((i, j, length + 1))