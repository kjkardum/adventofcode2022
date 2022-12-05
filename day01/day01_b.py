def main():
    totals, current = [], 0
    with open("input.txt") as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if line == "":
            totals.append(current)
            current = 0
        else:
            current += int(line)
    totals.append(current)
    #print sum of top 3
    print(sum(sorted(totals, reverse=True)[:3]))
    

if __name__ == "__main__":
    main()