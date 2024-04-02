MAX_EQUATION_NUMBER = 10


def read_equation_system(filename):
    equation_system = []
    iterator = 0
    with open(filename, 'r') as file:
        for line in file:
            if iterator > MAX_EQUATION_NUMBER:
                raise Exception("Maksymalna liczba równań przekroczona.")
            numbers = line.strip().split()
            equation = [float(num) for num in numbers]
            equation_system.append(equation)
    return equation_system
