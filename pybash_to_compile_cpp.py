import subprocess
import os

# -std=c++17
# - O2
# -Wall -Wextra -Werror: eforce all possible warnings, and make them erros
# -pedantic: forbids any g++ extension which is not ISO/ANSI compliant


dir_path = os.path.dirname(os.path.realpath(__file__))

source_file = dir_path + '/learning_cpp/c_pp_class.cpp'

# Specify the name of the executable file
executable_file = dir_path + '/learning_cpp/c_pp_class.exe'

# Compile the C++ code with g++
command = f"g++ -std=c++17 {source_file} -o {executable_file}"
result = subprocess.run(command, shell=True)

# Check if the compilation was successful
if result.returncode == 0:
    print("Compilation successful!")
else:
    print("Compilation failed.")
    print("Error message:")
    print(result.stderr)

# Run the executable
command = f"./{executable_file}"
result = subprocess.run(command, shell=True)

# Print the output of the executable
print(result.stdout)