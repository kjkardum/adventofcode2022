if __name__ == "__main__":
    data = [list(map(int, line.strip())) for line in open("input.txt")]
    n = len(data)
    max_left, max_top, max_right, max_bottom = ([[0] * n for _ in range(n)] for _ in range(4))

    for i in range(n):
        for j in range(n):
            re_i, re_j = n - 1 - i, n - 1 - j
            max_top[i][j] = data[i][j] if i == 0 else max(data[i][j], max_top[i - 1][j])
            max_left[i][j] = data[i][j] if j == 0 else max(data[i][j], max_left[i][j - 1])
            max_bottom[re_i][re_j] = data[re_i][re_j] if re_i == n - 1 else max(data[re_i][re_j], max_bottom[re_i + 1][re_j])
            max_right[re_i][re_j] = data[re_i][re_j] if re_j == n - 1 else max(data[re_i][re_j], max_right[re_i][re_j + 1])
    peaks_number = 0
    for i in range(n):
        for j in range(n):
            peaks_number += \
                i == 0 or j == 0 or i == n - 1 or j == n - 1 or \
                data[i][j] > max_left[i][j - 1] or \
                data[i][j] > max_top[i - 1][j] or \
                data[i][j] > max_right[i][j + 1] or \
                data[i][j] > max_bottom[i + 1][j]
    print(peaks_number)
    