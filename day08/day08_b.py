if __name__ == "__main__":
    data = [list(map(int, line.strip())) for line in open("input.txt")]
    n = len(data)
    visible_left, visible_right, visible_top, visible_bottom = [], [], [], []
    for i in range(n):
        visible_left.append([])
        visible_top.append([])
        for j in range(n):
            visible_left[-1].append([])
            visible_top[-1].append([])
            for k in range(10):
                if i == 0 and j == 0:
                    visible_left[-1][-1].append(0)
                    visible_top[-1][-1].append(0)
                elif i == 0:
                    visible_left[-1][-1].append(visible_left[-1][-2][k] + 1 if data[i][j-1] < k else 1)
                    visible_top[-1][-1].append(0)
                elif j == 0:
                    visible_left[-1][-1].append(0)
                    visible_top[-1][-1].append(visible_top[-2][j][k] + 1 if data[i-1][j] < k else 1)
                else:
                    visible_left[-1][-1].append(visible_left[-1][-2][k] + 1 if data[i][j-1] < k else 1)
                    visible_top[-1][-1].append(visible_top[-2][j][k] + 1 if data[i-1][j] < k else 1)
    for i in range(n - 1, -1, -1):
        visible_right.append([])
        visible_bottom.append([])
        for j in range(n - 1, -1, -1):
            visible_right[-1].append([])
            visible_bottom[-1].append([])
            for k in range(10):
                if i == n-1 and j == n-1:
                    visible_right[-1][-1].append(0)
                    visible_bottom[-1][-1].append(0)
                elif i == n-1:
                    visible_right[-1][-1].append(visible_right[-1][-2][k] + 1 if data[i][j + 1] < k else 1)
                    visible_bottom[-1][-1].append(0)
                elif j == n-1:
                    visible_right[-1][-1].append(0)
                    visible_bottom[-1][-1].append(visible_bottom[-2][j][k] + 1 if data[i + 1][j] < k else 1)
                else:
                    visible_right[-1][-1].append(visible_right[-1][-2][k] + 1 if data[i][j + 1] < k else 1)
                    visible_bottom[-1][-1].append(visible_bottom[-2][j][k] + 1 if data[i + 1][j] < k else 1)
        visible_right[-1].reverse()
        visible_bottom[-1].reverse()
    visible_right.reverse()
    visible_bottom.reverse()

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
