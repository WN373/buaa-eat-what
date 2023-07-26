import os

def count_lines_in_py_files():
    current_directory = os.getcwd()
    total_lines = 0

    for file in os.listdir(current_directory):
        if file.endswith(".py") and os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                total_lines += len(lines)

    return total_lines

print(count_lines_in_py_files())