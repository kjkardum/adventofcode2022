"""
find index of last of first 14 characters that have no repeating characters
"""

def main():
    text = open("input.txt").read().strip()
    for i in range(len(text) - 14):
        if len(set(text[i:i+14])) == 14:
            print(i+14)
            break

if __name__ == "__main__":
    # main()
    # or one-liner
    print((lambda t:[next(i+x for i in range(len(t))if len(set(t[i:i+x]))==x)for x in(4,14)])(open("input.txt").read()))

