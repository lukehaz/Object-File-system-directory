#!/user/bin/python3.5


import datetime


class Item:
    def __init__(self, name, parentdir, permissions):
        self.name = name
        self.parentdir = parentdir
        self.permissions = permissions
        self.upddate = None


class File(Item):
    def __init__(self, name, parentdir, permissions, size):
        super().__init__(name, parentdir, permissions)
        self.size = size


class Directory(Item):
    def __init__(self, name, parentdir, permissions):
        super().__init__(name, parentdir, permissions)
        self.contents = []

    def add_file(self, file):
        self.contents.append(file)
        self.upddate = datetime.datetime.now()

    def add_directory(self, directory):
        self.contents.append(directory)
        self.upddate = datetime.datetime.now()


root = Directory("/", None, "rwx")


def delete_item():
    name = input("Enter File/Directory name: ")
    parent = input("Enter parent directory name: ")

    parent_dir = get_directory(root, parent)
    if parent_dir is None:
        print("ERROR: Parent directory not found.")
        return

    for item in parent_dir.contents:
        if item.name == name:
            parent_dir.contents.remove(item)
            print(f"{item.name} was removed")
            return

    print("ERROR: Item not found in parent directory.")




def create_directory():
    name = input("Please enter directory name or quit: ")
    if name == "quit":
     return

    permissions = input("Please enter access permissions using format rwx or quit: ")
    if permissions == 'quit':
     return
    parent = input("Please enter parent directory name or quit: ")

    parent_dir = get_directory(root, parent)
    if parent_dir is None:
        print("ERROR: Parent directory not found.")
        return

    for item in parent_dir.contents:
        if item.name == name:
            print("ERROR: Directory already exists in parent directory.")
            return

    directory = Directory(name, parent_dir, permissions)
    parent_dir.add_directory(directory)
    print("Created Directory: "+ "/" + directory.name )


def create_file():
    name = input("Please enter File name or quit: ")
    if name == 'quit':
     return
    permissions = input("Please enter access permissions using format rwx or quit: ")
    if permissions == 'quit':
     return

    size = input("Please enter size (1-Small, 2-Medium, 3-Large): ")
    parent = input("Please enter a parent directory or quit: ")
    if parent == 'quit':
     return
    parent_dir = get_directory(root, parent)
    if parent_dir is None:
        print("ERROR: Parent directory not found.")
        return

    for item in parent_dir.contents:
        if item.name == name:
            print("ERROR: File already exists in parent directory.")
            return

    file = File(name, parent_dir, permissions, size)
    parent_dir.add_file(file)
    
    print("Created File: " + parent_dir.name + file.name)


def display_file_system(directory=root, indent=0):
    print(" " * indent + directory.name)
    for item in sorted(directory.contents, key=lambda x: x.name):
        if isinstance(item, Directory):
            display_file_system(item, indent + 4)
        elif isinstance(item, File):
            print(" " * (indent + 4) + item.name)


def get_directory(directory, name):
    if directory.name == name:
        return directory
    for item in directory.contents:
        if isinstance(item, Directory):
            result = get_directory(item, name)
            if result is not None:
                return result
    return None

 

print("Welcome to Python's File System")
print("--------------------------------")

while True:
    print()
    print("Main Menu:")
    print("1. Create File")

    print("2. Create Directory")

    print("3. Remove a File/Directory")

    print("4. Display")

    print("5. Exit")
    print()
    choice = input("Enter your choice: ")

    if choice == "2":
        create_directory()
    elif choice == "1":
        create_file()
    elif choice == "4":
        display_file_system()
    elif choice == "5":
        print("Goodbye!")
        print("------------------")
        break
    elif choice =="3":
        delete_item()
    else:
        print("Invalid choice. Please try")

