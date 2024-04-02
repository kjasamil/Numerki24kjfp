import file_handler as fh
import gauss as g

equation_system = fh.read_equation_system("equation_system.txt")
print(equation_system)
solution = []
g.solve(equation_system, solution)
print(solution)
