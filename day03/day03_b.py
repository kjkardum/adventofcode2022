def main():
    with open("input.txt") as f:
        # split line at half
        lines = [line.strip() for line in f.readlines()]
    grouped_each_3 = [tuple(lines[i:i+3]) for i in range(0, len(lines), 3)]
    repeated_characters = [set(first).intersection(set(second)).intersection(set(third)) for first, second, third in grouped_each_3]
    repeated_characters = [list(repeated)[0] for repeated in repeated_characters]
    print(*repeated_characters)
    converted_to_numbers = [ord(i) - ord('a') + 1 if "a"<=i<="z" else ord(i) - ord('A') + 27 for i in repeated_characters]
    print(*converted_to_numbers)

    print(sum(converted_to_numbers))
    

if __name__ == "__main__":
    main()