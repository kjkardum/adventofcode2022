"""
find index of last of first 4 characters that have no repeating characters
for mjqjpqmgbljsphdztnvjfqwrcgsmlb
m    1
mj   2
mjq  3
mjqj 4
jqjp 5
qjpm 6
jpmg 7
result is 7 as in jpmg there are no repeating characters, and g is at index 7
"""

def main():
    text = open("input.txt").read().strip()
    for i in range(len(text) - 4):
        if len(set(text[i:i+4])) == 4:
            print(i+4)
            break

if __name__ == "__main__":
    main()