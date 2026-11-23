import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_tree(path, indent=""):
    """Recursively print the directory structure with colors."""
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    for item in items:
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            print_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    init()
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Usage: python task_3.py <directory_path>{Style.RESET_ALL}")
        return

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"{Fore.RED}Path does not exist: {path}{Style.RESET_ALL}")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Path is not a directory: {path}{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}{path.name}/{Style.RESET_ALL}")
    print_tree(path, "    ")


if __name__ == "__main__":
    main()