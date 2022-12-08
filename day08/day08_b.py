if __name__ == "__main__":
    data = [list(map(int, line.strip())) for line in open("input.txt")]
    n = len(data)
    visible_left, visible_right, visible_top, visible_bottom = ([[[0] * 10 for _ in range(n)] for _ in range(n)] for _ in range(4))
    for i in range(n):
        for j in range(n):
            re_i, re_j = n - 1 - i, n - 1 - j
            for h in range(10):
                visible_left[i][j][h] = j!=0 and (visible_left[i][j - 1][h] + 1 if data[i][j - 1] < h else 1)
                visible_top[i][j][h] = i!=0 and (visible_top[i - 1][j][h] + 1 if data[i - 1][j] < h else 1)
                visible_right[re_i][re_j][h] = re_j!=n-1 and (visible_right[re_i][re_j + 1][h] + 1 if data[re_i][re_j + 1] < h else 1)
                visible_bottom[re_i][re_j][h] = re_i!=n-1 and (visible_bottom[re_i + 1][re_j][h] + 1 if data[re_i + 1][re_j] < h else 1)

    visible_top = [[visible_top[i][j][data[i][j]] for j in range(n)] for i in range(n)]
    visible_left = [[visible_left[i][j][data[i][j]] for j in range(n)] for i in range(n)]
    visible_bottom = [[visible_bottom[i][j][data[i][j]] for j in range(n)] for i in range(n)]
    visible_right = [[visible_right[i][j][data[i][j]] for j in range(n)] for i in range(n)]

    value = []
    for i in range(n):
        value.append([])
        for j in range(n):
            value[-1].append(visible_bottom[i][j] * visible_top[i][j] * visible_left[i][j] * visible_right[i][j])
    print(max(max(t) for t in value))
