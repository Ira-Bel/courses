matrix = [
    [0, 1, 2, 3, 4],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34],
    [40, 41, 42, 43, 44]
]


# вывод на печать
def print_matrix(matrix):
    for raw in matrix:
        for element in raw:
            print("%5d" % element, end=' ')
        else:
            print()
    return ''


print(print_matrix(matrix))


# сумма всех элементов
def calc_elements(matrix):
    sum = 0
    for raw in matrix:
        for element in raw:
            sum += element
    return sum


print(calc_elements(matrix))


# среднее значение элементов
def mean_elements(matrix):
    amount = len([element for raw in matrix for element in raw])
    mean = calc_elements(matrix) / amount
    return mean


print(mean_elements(matrix))


aver_elem = sum([elem for row in matrix for elem in row]) / len([element for raw in matrix for element in raw])


# возведение элемента в квадрат и возвращение в матрицу
def second_degree_elements(matrix):
    new_matrix = []
    for raw in matrix:
        new_raw = []
        for element in raw:
            element = element ** 2
            new_raw.append(element)
        new_matrix.append(new_raw)
    return new_matrix


print_matrix(second_degree_elements(matrix))





# Печать элемента в обратном порядке с добавлением в матрицу

def reverse_matrix(matrix):
    new_matrix = [list(reversed(element)) for element in reversed(matrix)]
    return new_matrix


print_matrix(reverse_matrix(matrix))








