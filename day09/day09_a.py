if __name__ == "__main__":
    data = [line.split() for line in open("input.txt")]
    data = [(x, int(y)) for x, y in data]
    dir = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    pos_h, pos_t = (0, 0), (0, 0)
    visited_h, visited_t = set(), set()
    for direction, length in data:
        direction = dir[direction]
        for _ in range(length):
            pos_h = (pos_h[0] + direction[0], pos_h[1] + direction[1])
            if not (pos_h[0] -1 <= pos_t[0] <= pos_h[0] + 1 and pos_h[1] -1 <= pos_t[1] <= pos_h[1] + 1):
                # pos_t must be moved closer to pos_h, either diagonally or straight
                if pos_h[0] == pos_t[0]:
                    pos_t = (pos_t[0], pos_t[1] + (1 if pos_h[1] > pos_t[1] else -1))
                elif pos_h[1] == pos_t[1]:
                    pos_t = (pos_t[0] + (1 if pos_h[0] > pos_t[0] else -1), pos_t[1])
                else:
                    pos_t = (pos_t[0] + (1 if pos_h[0] > pos_t[0] else -1), pos_t[1] + (1 if pos_h[1] > pos_t[1] else -1))
            visited_h.add(pos_h)
            visited_t.add(pos_t)
    print(len(visited_t))