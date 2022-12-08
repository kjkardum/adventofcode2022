if __name__ == "__main__":
    data = [list(map(int, line.strip())) for line in open("input.txt")]
    n = len(data)
    max_left, max_top, max_right, max_bottom = [], [], [], []

    for i in range(n):
        max_top.append([])
        max_left.append([])
        for j in range(n):
            if i == 0 and j == 0:
                max_left[-1].append(data[i][j])
                max_top[-1].append(data[i][j])
            elif i == 0:
                max_left[-1].append(max(data[i][j], max_left[-1][-1]))
                max_top[-1].append(data[i][j])
            elif j == 0:
                max_left[-1].append(data[i][j])
                max_top[-1].append(max(data[i][j], max_top[-2][j]))
            else:
                max_left[-1].append(max(data[i][j], max_left[-1][-1]))
                max_top[-1].append(max(data[i][j], max_top[-2][j]))
    for i in range(n-1, -1, -1):
        max_bottom.append([])
        max_right.append([])
        for j in range(n-1, -1, -1):
            if i == n-1 and j == n-1:
                max_bottom[-1].append(data[i][j])
                max_right[-1].append(data[i][j])
            elif i == n-1:
                max_bottom[-1].append(data[i][j])
                max_right[-1].append(max(data[i][j], max_right[-1][-1]))
            elif j == n-1:
                max_bottom[-1].append(max(data[i][j], max_bottom[-2][j]))
                max_right[-1].append(data[i][j])
            else:
                max_bottom[-1].append(max(data[i][j], max_bottom[-2][j]))
                max_right[-1].append(max(data[i][j], max_right[-1][-1]))
        max_bottom[-1].reverse()
        max_right[-1].reverse()
    max_bottom.reverse()
    max_right.reverse()
    
    peaks_number = 0
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                peaks_number += 1
            elif data[i][j] > max_left[i][j-1] or data[i][j] > max_top[i-1][j] or data[i][j] > max_right[i][j+1] or data[i][j] > max_bottom[i+1][j]:
                peaks_number += 1
    print(peaks_number)