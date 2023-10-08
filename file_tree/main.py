import os


def print_directory_structure(start_path, exclusions=[]):
    prefix = {"branch": "├── ", "last_branch": "└── ", "vertical": "│   ", "empty": "    "}

    def custom_sort(item):
        """Sort items with directories first, then by dot prefix, and then alphabetically."""
        if item.is_dir():
            order = 0
        else:
            order = 1

        is_dot = item.name.startswith(".")
        name = item.name.lower()
        return (order, not is_dot, name)

    def _print_dir_structure(path, indent=""):
        items = sorted(list(os.scandir(path)), key=custom_sort)
        for index, entry in enumerate(items):
            is_last = index == len(items) - 1
            if entry.is_dir():
                print(f'{indent}{prefix["last_branch" if is_last else "branch"]}{entry.name}/')
                new_indent = indent + (prefix["empty"] if is_last else prefix["vertical"])

                if os.path.basename(entry.path) in exclusions:
                    print(f'{new_indent}{prefix["last_branch"]}...')
                else:
                    _print_dir_structure(entry.path, new_indent)
            elif entry.is_file():
                print(f'{indent}{prefix["last_branch" if is_last else "branch"]}{entry.name}')

    _print_dir_structure(start_path)


if __name__ == "__main__":
    path = "/Users/smehta/Developer/projects/Conways-Game-Of-Life" #UPDATE path
    exclude_dirs = ["env", ".mypy_cache", ".git", "__pycache__"] #UPDATE excluded files

    if os.path.exists(path) and os.path.isdir(path):
        print_directory_structure(path, exclusions=exclude_dirs)
    else:
        print(f"The path {path} either doesn't exist or is not a directory.")
