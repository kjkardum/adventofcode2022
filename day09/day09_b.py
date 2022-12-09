from collections import namedtuple
Cord = namedtuple("Cord", ["x", "y"], defaults=[0, 0])

if __name__ == "__main__":
    data = [line.split() for line in open("input.txt")]
    data = [(d, int(l)) for d, l in data]
    dir = {"R": Cord(0, 1), "L": Cord(0, -1), "U": Cord(-1, 0), "D": Cord(1, 0)}
    tail = [Cord() for _ in range(10)]
    visited_t = set()
    for direction, length in data:
        direction = dir[direction]
        for _ in range(length):
            tail[0] = Cord(tail[0].x + direction.x, tail[0].y + direction.y)
            for i, (prev, curr) in enumerate(zip(tail, tail[1:]), start=1):
                if not (prev.x-1 <= curr.x <= prev.x+1 and prev.y-1 <= curr.y <= prev.y+1):
                    if prev.x == curr.x:
                        tail[i] = Cord(curr.x, curr.y + [-1, 1][prev.y > curr.y])
                    elif prev.y == curr.y:
                        tail[i] = Cord(curr.x + [-1, 1][prev.x > curr.x], curr.y)
                    else:
                        tail[i] = Cord(curr.x + [-1, 1][prev.x > curr.x], curr.y + [-1, 1][prev.y > curr.y])
            visited_t.add(curr)
    print(len(visited_t))