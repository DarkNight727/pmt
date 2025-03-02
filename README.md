# pmt - Package Maintainer

**pmt** is a simple Python-based package management tool for Arch Linux users, designed to interface with both the official `pacman` repository and the AUR (Arch User Repository) through `yay`. It allows users to easily install, remove, search for, and update packages, all from a simple command-line interface.

## Features

- **Install**: Searches for a package in both pacman and AUR, and installs it if found.
- **Remove**: Removes a specified package from your system using `yay`.
- **Search**: Searches for a package in pacman and AUR, and provides feedback on where it is available.
- **Update**: Updates a specific package using `yay`.
- **Update System**: Updates the entire system, including both pacman and AUR packages.

## Requirements

- Python 3.x
- `yay` (AUR helper)
- `pacman` (Arch Linux package manager)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/DarkNight727/pmt.git
2. Cd into the directory:
   
  ```bash
   cd pmt
  ```
3. Run program with python:
   ```bash
   python3 pmt.py
   ```
