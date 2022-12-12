if __name__ == "__main__":
    sum_array = [1]
    for i, action in enumerate(open("input.txt")):
        sum_array.append(sum_array[-1])
        if action.startswith("add"):
            sum_array.append(sum_array[-1] + int(action.split()[1]))
    
    print(sum((index+1)*value for index, value in list(enumerate(sum_array))[19:220:40]))
    for x in range(6):
        for y in range(40):
            print(" #"[y-1 <= sum_array[x*40+y] <= y+1], end="")
        print()