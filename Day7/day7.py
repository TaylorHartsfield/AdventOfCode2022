data = open('input.txt', 'r')
files = data.read().split('\n')

#build tree

class Dir:

    def __init__(self, dirName, parent, files=[]):
        self.dirName = dirName
        self.files = files
        self.parent = parent
    
    def add_file(self, new_file):
        self.files.append(new_file)

    def traverse(self):
        to_visit = [self]
        while len(to_visit) > 0:
            current_node = to_visit.pop()
            print(current_node)
            to_visit += current_node.files
    
    def __repr__(self):
        return(f"<Dir {self.dirName}>")

class File:

    def __init__(self, size, parent):
        self.size = size
        self.parent = parent


current_parent = Dir('Home', None, files=[])
print(type(current_parent))

for command in files:
    if command.startswith("dir"):
        new_dir = Dir(command[4::], current_parent)
        # print(type(new_dir))
        # print(type(current_parent))
        # current_parent.add_file(new_dir)
        # print(new_dir.parent)

    elif command[0].isalpha():
        new_file = File(int(command.split(' ')[0]), current_parent)
        current_parent.add_file(new_file)

    elif command.startswith("$ cd"):
        if command[5::] == "..":
            current_parent = current_parent.parent
        else:
            current_parent = command[5::]


