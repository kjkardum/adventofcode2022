def get_directory(tree, path):
    for dir in path:
        tree = tree.setdefault((dir), {})
    return tree

def get_size(tree, sizes, path = ""):
    sizes.append(sum(
            data if isinstance(data, int) else get_size(data, sizes, f"{path}/{name}")
            for name, data in tree.items()))
    return sizes[-1]

if __name__ == "__main__":
    dir_tree, current_path = {}, []
    for line in open("input.txt"):
        match line.split():
            case ["$", "cd", ".."]:
                current_path.pop(-1)
            case ["$", "cd", "/"]:
                current_path = []
            case ["$", "cd", dir]:
                current_path.append(dir)
            case ["$", "ls"] | ["dir", _]:
                pass
            case [size, file]:
                get_directory(dir_tree, current_path)[(file)] = int(size)
    sizes = []
    get_size(dir_tree, sizes)
    print(sum(filter(lambda size: size < 100_000, sizes)))

    needed_space = max(sizes) - 40_000_000
    print(min(filter(lambda size: size > needed_space, sizes)))