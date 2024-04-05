import file_handler as fh
import gauss as g
import os

# equation_system = fh.read_equation_system("equations/" + "7equation_system.txt")
directory = "equations/"


for files in os.listdir(directory):
    print(files)
    equation_system = fh.read_equation_system(directory + str(files))
    print(equation_system)
    print(g.solve(equation_system))
    print()