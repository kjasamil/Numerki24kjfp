def difference_quotients_func(function, arguments):
    n = len(arguments)
    quotients = [[function(argument) for argument in arguments]]
    for k in range(1, n):
        quotients.append([])
        for i in range(n - k):
            quotients_k = (quotients[k-1][i+1] - quotients[k-1][i]) / (arguments[i+k] - arguments[i])
            quotients[k].append(quotients_k)
    quotients_x0 = []
    for i in range(1, n):
        quotients_x0.append(quotients[i][0])
    return quotients_x0


def difference_quotients_val(func_values):
    n = len(func_values[0])
    quotients = [[func_values[1][i] for i in range(len(func_values[1]))]]
    for k in range(1, n):
        quotients.append([])
        for i in range(n - k):
            quotients_k = (quotients[k - 1][i + 1] - quotients[k - 1][i]) / (func_values[0][i + k] - func_values[0][i])
            quotients[k].append(quotients_k)
    quotients_x0 = []
    for i in range(1, n):
        quotients_x0.append(quotients[i][0])
    return quotients_x0


def newton_interpolation_func(x, function, arguments, difference_quotients):
    n = len(arguments)
    func_value = function(arguments[0])
    product = 1
    for i in range(n-1):
        product = product * (x - arguments[i])
        func_value += product * difference_quotients[i]
    return func_value


def newton_interpolation_val(x, func_values, difference_quotients):
    n = len(func_values[0])
    func_value = func_values[1][0]
    product = 1
    for i in range(n-1):
        product = product * (x - func_values[0][i])
        func_value += product * difference_quotients[i]
    return func_value

