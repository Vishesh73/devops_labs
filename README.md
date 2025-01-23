# Simple Calculator

A simple Python-based calculator that can perform basic operations like addition, subtraction, multiplication, and division.

## Features
- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

## Requirements
- Python 3.x (No external dependencies required)

## Installation

### 1. Clone the repository or download the project

To get started, you can either clone the repository or download the project as a ZIP file from the directory where the code is hosted.

git clone <repository_url>
cd <repository_directory>

Alternatively, if you haven't done so already, you can create a project folder manually and place the script `main.py` inside it.

### 2. Set up your Python environment (Optional but recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv calculator-env

#Running the Calculator Script

Once you've set up your environment, navigate to the folder containing the calculator.py script and run the following command in your terminal:

python main.py

# Packaging the Script as an Executable
If you'd like to package the script into a standalone executable file that doesn't require Python to be installed, you can use PyInstaller to create an executable.

1. Install PyInstaller:
If you don't have PyInstaller installed, you can install it via pip:

pip install pyinstaller

2. Package the Script:
Navigate to the directory containing main.py and run the following command to create an executable:

pyinstaller --onefile main.py

3. Running the Executable:
After packaging the script, you can run the executable file directly from the dist folder without needing Python installed on your system.

dist\calculator.exe   # On Windows
./dist/calculator      # On macOS/Linux

# License

Conclusion
You've successfully run a Python application
