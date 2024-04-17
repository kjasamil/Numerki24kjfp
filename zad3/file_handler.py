def read_nodes(filename):
    with open(filename, 'r') as f:
        arguments = list(map(float, f.readline().split()))
        values = list(map(float, f.readline().split()))
    if len(arguments) != len(values):
        raise ValueError("Liczba argumentów nie odpowiada liczbie wartości.")
    nodes = [arguments, values]
    zip_nodes = list(zip(*nodes))
    sorted_zip_nodes = sorted(zip_nodes, key=lambda x: x[0])
    sorted_nodes = list(zip(*sorted_zip_nodes))
    return sorted_nodes


def read_arguments(filename):
    with open(filename, 'r') as f:
        arguments = list(map(float, f.readline().split()))
    arguments.sort()
    return arguments
