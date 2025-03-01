import subprocess

def install_package(pkg_name):
    """Searches for a package in both pacman and AUR, then installs it."""
    pacman_search = subprocess.run(["pacman", "-Ss", pkg_name], capture_output=True, text=True)
    yay_search = subprocess.run(["yay", "-Ss", pkg_name], capture_output=True, text=True)

    if pacman_search.stdout and yay_search.stdout:
        print(f"'{pkg_name}' found in both pacman and AUR. Installing...")
    elif pacman_search.stdout:
        print(f"'{pkg_name}' found in pacman. Installing...")
    elif yay_search.stdout:
        print(f"'{pkg_name}' found in AUR. Installing...")
    else:
        print(f"Package '{pkg_name}' not found.")
        return

    subprocess.run(["yay", "-S", pkg_name])

def remove_package(pkg_name):
    """Removes a package using pacman (and yay for AUR packages)."""
    subprocess.run(["yay", "-Rns", pkg_name])

def search_package(pkg_name):
    """Searches for a package in pacman and AUR."""
    pacman_search = subprocess.run(["pacman", "-Ss", pkg_name], capture_output=True, text=True)
    yay_search = subprocess.run(["yay", "-Ss", pkg_name], capture_output=True, text=True)

    if pacman_search.stdout and yay_search.stdout:
        print(f"'{pkg_name}' is available in both pacman and AUR.")
    elif pacman_search.stdout:
        print(f"'{pkg_name}' is available in pacman.")
    elif yay_search.stdout:
        print(f"'{pkg_name}' is available in AUR.")
    else:
        print(f"'{pkg_name}' is not found in either pacman or AUR.")

def update_package(pkg_name):
    """Updates a specific package using yay."""
    subprocess.run(["yay", "-S", pkg_name])

def update_system():
    """Updates the entire system including AUR and official repos."""
    subprocess.run(["yay", "-Syu"])

def main():
    while True:
        print("\nOptions:")
        print("1. Install")
        print("2. Remove")
        print("3. Search")
        print("4. Update")
        print("5. Update system")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            pkg = input("Enter package name to install: ")
            install_package(pkg)
        elif choice == "2":
            pkg = input("Enter package name to remove: ")
            remove_package(pkg)
        elif choice == "3":
            pkg = input("Enter package name to search: ")
            search_package(pkg)
        elif choice == "4":
            pkg = input("Enter package name to update: ")
            update_package(pkg)
        elif choice == "5":
            update_system()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
