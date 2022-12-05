def main():
    with open("input.txt") as f:
        # split line at half
        lines = [[i.split("-") for i in line.strip().split(",")] for line in f.readlines()]

    # each line contains 2 ranges from-to,from-to
    # find number of lines where one range is overlapping in another
    
    contained = 0
    for line in lines:
        from1, to1 = line[0]
        from1, to1 = int(from1), int(to1)
        from2, to2 = line[1]
        from2, to2 = int(from2), int(to2)
        if (from1 <= from2 <= to1 or from1 <= to2 <= to1) or (from2 <= from1 <= to2 or from2 <= to1 <= to2):
            contained += 1
    print(contained)
        
    

if __name__ == "__main__":
    main()