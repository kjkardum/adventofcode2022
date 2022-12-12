if __name__ == "__main__":
    data = [line.split() for line in open("input.txt")]
    sum_array = [1]
    for i, action in enumerate(data):
        op = action[0]
        value = int(action[1]) if len(action) > 1 else 0
        if op == "addx":
            sum_array.append(sum_array[-1])
            sum_array.append(sum_array[-1] + value)
        elif op == "noop":
            sum_array.append(sum_array[-1])
    print(sum((index+1) *value for index, value in list(enumerate(sum_array))[19:221:40]))