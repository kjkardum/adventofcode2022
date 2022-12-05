"""
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
 plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

"""
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors
"""
def main():
    with open("input.txt") as f:
        lines = [list(line.split()) for line in f.readlines()]

    print(lines)
    score = 0
    for line in lines:
        if line[0] == "A":
            if line[1] == "X":
                score += 3
            elif line[1] == "Y":
                score += 6
            elif line[1] == "Z":
                score += 0
        elif line[0] == "B":
            if line[1] == "X":
                score += 0
            elif line[1] == "Y":
                score += 3
            elif line[1] == "Z":
                score += 6
        elif line[0] == "C":
            if line[1] == "X":
                score += 6
            elif line[1] == "Y":
                score += 0
            elif line[1] == "Z":
                score += 3
        if line[1] == "X":
            score += 1
        elif line[1] == "Y":
            score += 2
        elif line[1] == "Z":
            score += 3
    print(score)
    

if __name__ == "__main__":
    main()
    #print(*(lambda reduce: reduce(lambda acc, curr: acc + [acc[-1] + curr],sorted(reduce(lambda acc, curr: acc[:-1] + [acc[-1] + int(curr)] if curr else acc + [0], map(lambda x: x.strip(), open("input.txt")), [0]), reverse = True),[0])[1:4:2])(__import__('functools').reduce))