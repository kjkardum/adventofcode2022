def main():
    current_max, current = 0,0
    with open("input.txt") as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if line == "":
            current_max = max(current, current_max)
            current = 0
        else:
            current += int(line)
    current_max = max(current, current_max)
    print(current_max)
    

if __name__ == "__main__":
    main()
    #print(*(lambda reduce: reduce(lambda acc, curr: acc + [acc[-1] + curr],sorted(reduce(lambda acc, curr: acc[:-1] + [acc[-1] + int(curr)] if curr else acc + [0], map(lambda x: x.strip(), open("input.txt")), [0]), reverse = True),[0])[1:4:2])(__import__('functools').reduce))