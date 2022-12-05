"""
Input example:
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
"""
Top of input shows starting locations of n crates (3 in this example), then each line is a move
Print list of crates at top of each stack from left to right
"""

def main():
    stacks = []
    moves = []
    for line in open("input.txt"):
        line = line.replace("\n", "")
        if line == "":
            continue
        if line.startswith("move"):
            _, number, _, from_crate, _ , to_crate = line.split()
            moves.append((int(number), int(from_crate) - 1, int(to_crate) - 1))
            continue
        for index, stack in enumerate(line[1::4]):
            if index >= len(stacks):
                stacks.append([])
            if stack == " ":
                continue
            stacks[index].append(stack)
    for stack in stacks:
        stack.reverse()
    stacks = [stack[1:] for stack in stacks]
    print(stacks)
    print(moves)
    for move in moves:
        number, from_crate, to_crate = move
        moved = stacks[from_crate][-number:]
        stacks[from_crate] = stacks[from_crate][:-number]
        stacks[to_crate] = stacks[to_crate] + moved
    
    print("".join([stack[-1] for stack in stacks]))

if __name__ == "__main__":
    main()