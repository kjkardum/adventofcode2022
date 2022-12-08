"""
possible commands:
$ ls
$ cd /
$ cd ..
$ cd <next_dir> (only one level)

ls result:
dir <dir_name>
dir <dir_name>
<size> <file_name>
<size> <file_name>
...

"""

def get_directory(tree, path):
    if path == "":
        return tree
    for dir in path.split("/"):
        if ('d', dir) not in tree:
            tree[('d', dir)] = {}
        tree = tree[('d', dir)]
    return tree

def main():
    current_dir = []
    file_tree = {}
    for line in open("input.txt"):
        line = line.strip()
        if line.startswith("$ cd "):
            dir = line[5:]
            if dir == "..":
                current_dir.pop(-1)
            elif dir == "/":
                current_dir = []
            else:
                current_dir.append(dir)
            continue
        # other lines are 'dir name_of_dir' or 'size name_of_file' which are directories or files in the current directory
        if line.startswith("dir "):
            dir = line[4:]
            get_directory(file_tree, "/".join(current_dir + [dir]))
        elif not line.startswith("$"):
            size, filename = line.split(" ")
            size = int(size)
            get_directory(file_tree, "/".join(current_dir))[('f', filename)] = size
    
    # calculate total size of each directory
    sizes = {}
    def get_size(tree, path=""):
        size = 0
        for k, v in tree.items():
            if k[0] == 'f':
                size += v
            else:
                size += get_size(v, path + "/" + k[1])
        sizes[path] = size
        return size
    print(file_tree)
    get_size(file_tree)
    print(sizes)
    # sum all sizes below 100000
    print(sum([size for size in sizes.values() if size < 100000]))




def better_solution():
    lines = [line.strip() for line in open("input.txt")]
    dirs = {} # recursive directory structure {('d',dir_name):{('d',dir_name):{('f',file_name):size}}, ('f',file_name):size, ...}
    current_path = []
    #solution with python 3.10 match case
    for line in lines:
        match line.split():
            case ["$", "cd", ".."]:
                current_path.pop(-1)
            case ["$", "cd", "/"]:
                current_path = []
            case ["$", "cd", dir]:
                current_path.append(dir)
            case ["$", "ls"]:
                pass
            case ["dir", dir]:
                get_directory(dirs, current_path + [dir])
            case [size, file]:
                get_directory(dirs, current_path)[('f', file)] = int(size)
    # calculate total size of each directory
    sizes = {}
    def get_size(tree, path = ""):
        size = 0
        for (type_, name), content in tree.items():
            if type_ == 'f':
                size += content
            else:
                size += get_size(content, path + "/" + name)
        sizes[path] = size
        return size
    get_size(dirs)
    print(sum([size for size in sizes.values() if size < 100000]))
    needed_free_space = max(sizes.values()) - 40000000
    print(min([size for size in sizes.values() if size > needed_free_space]))


if __name__ == "__main__":
    main()