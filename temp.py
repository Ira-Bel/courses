from functools import reduce

temp = [
    [27.75, 23.85, 23.56, 26.36, 26.35, 29.67, 29.84, 23.27, 28.32, 27.68, 28.88, 29.34, 27.42, 26.46, 28.0, 25.79,
     29.56, 23.73, 28.13, 21.95],
    [25.89, 27.08, 22.67, 23.53, 26.73, 26.49, 25.12, 24.8, 24.56, 25.47, 27.62, 24.31, 24.12, 23.39, 29.26, 23.01,
     23.17, 21.11, 29.27, 26.54],
    [22.25, 21.6, 29.58, 21.98, 24.76, 29.76, 23.47, 28.21, 25.14, 28.64, 27.01, 26.06, 25.65, 20.12, 21.85, 23.42,
     21.39, 28.02, 23.96, 29.56],
    [26.51, 26.88, 22.43, 23.11, 26.21, 23.96, 27.53, 28.81, 27.45, 28.4, 29.04, 25.96, 22.67, 22.55, 28.83, 23.66,
     25.85, 27.66, 20.02, 24.99],
    [23.42, 23.23, 27.41, 27.06, 27.48, 26.56, 20.74, 29.57, 24.35, 28.41, 26.85, 29.19, 21.97, 21.13, 22.89, 23.25,
     22.89, 26.46, 27.46, 20.44],
    [28.92, 20.53, 20.99, 29.78, 24.57, 20.24, 24.71, 24.16, 23.65, 28.0, 26.66, 26.52, 23.83, 28.36, 27.24, 20.1,
     25.17, 29.24, 22.37, 24.05],
    [21.51, 24.3, 20.94, 29.25, 26.27, 20.84, 29.87, 21.39, 26.24, 24.16, 20.01, 28.35, 21.85, 28.16, 26.02, 26.75,
     21.73, 27.51, 22.66, 22.95],
    [28.23, 22.2, 26.53, 28.1, 24.83, 20.66, 25.64, 29.55, 24.89, 27.33, 27.62, 23.91, 20.33, 26.42, 27.37, 25.23,
     21.79, 26.11, 24.59, 22.58],
    [22.12, 21.4, 24.45, 22.61, 21.25, 22.29, 23.92, 26.15, 29.41, 23.85, 24.44, 28.49, 23.67, 20.29, 23.69, 23.96,
     23.21, 28.33, 25.39, 21.15],
    [23.53, 22.81, 25.83, 28.41, 24.48, 22.68, 24.4, 21.44, 21.17, 24.88, 29.66, 23.47, 23.69, 28.98, 26.43, 29.04,
     22.65, 25.99, 25.63, 28.5],
    [23.93, 26.1, 29.79, 25.91, 22.86, 24.68, 23.33, 26.38, 24.08, 27.89, 20.95, 20.5, 25.75, 23.07, 23.18, 21.73,
     25.55, 24.7, 20.68, 20.97],
    [21.13, 21.95, 24.54, 28.05, 27.11, 25.36, 22.86, 20.39, 20.44, 28.16, 24.36, 23.48, 21.64, 22.82, 25.55, 29.45,
     28.07, 25.07, 20.57, 26.82],
    [22.13, 26.83, 28.09, 27.38, 27.04, 22.23, 23.66, 27.46, 26.96, 24.09, 20.39, 28.26, 29.36, 22.37, 27.01, 23.63,
     23.0, 28.89, 26.93, 28.04],
    [29.8, 22.48, 27.33, 28.58, 28.27, 22.05, 20.94, 28.71, 24.04, 27.33, 28.2, 27.76, 24.4, 22.14, 29.67, 24.07, 20.14,
     22.87, 22.16, 22.47],
    [20.52, 25.23, 24.6, 28.01, 23.74, 21.21, 23.4, 22.94, 22.59, 28.47, 26.21, 21.96, 29.74, 21.78, 28.79, 27.16,
     21.99, 26.9, 23.51, 23.49],
    [28.22, 22.42, 28.63, 23.5, 21.92, 25.81, 23.53, 20.73, 26.98, 26.53, 22.52, 27.04, 27.24, 20.2, 21.96, 23.55,
     24.39, 28.99, 21.72, 29.99],
    [24.91, 23.63, 25.31, 21.74, 23.38, 29.26, 29.02, 26.33, 23.71, 26.14, 28.58, 26.14, 23.67, 29.09, 24.46, 22.51,
     21.74, 20.38, 25.77, 29.43],
    [27.81, 21.07, 20.7, 22.38, 25.74, 27.79, 23.55, 27.56, 26.28, 26.37, 26.92, 28.61, 29.25, 22.55, 24.66, 25.12,
     23.97, 24.28, 22.35, 20.43],
    [22.34, 23.1, 22.17, 21.71, 28.8, 25.06, 27.71, 24.15, 25.86, 24.75, 29.95, 26.18, 27.1, 27.96, 25.65, 27.95, 23.52,
     29.01, 22.07, 21.34],
    [24.51, 24.17, 20.18, 27.57, 25.0, 26.49, 21.0, 24.91, 25.39, 24.89, 27.72, 22.87, 28.31, 20.64, 29.71, 23.83, 29.2,
     20.31, 27.01, 28.17],
    [20.44, 20.47, 27.82, 29.86, 29.33, 22.14, 24.83, 26.38, 25.62, 24.51, 24.87, 22.8, 20.43, 22.34, 27.71, 27.42,
     27.23, 23.21, 21.57, 23.65],
    [28.64, 24.12, 25.12, 29.04, 25.79, 27.12, 20.5, 25.71, 28.14, 26.54, 24.39, 22.15, 28.25, 20.98, 24.85, 26.48,
     23.05, 26.81, 24.68, 29.74],
    [26.29, 26.74, 23.36, 23.4, 28.85, 23.0, 29.93, 26.82, 28.99, 27.53, 23.33, 21.13, 28.42, 23.41, 28.01, 20.02,
     21.73, 24.86, 29.72, 29.89],
    [27.11, 22.39, 28.88, 21.58, 24.41, 26.99, 24.55, 26.32, 27.28, 24.72, 27.01, 26.43, 27.13, 25.23, 21.26, 20.17,
     21.37, 23.46, 29.73, 23.18],
    [25.37, 29.0, 28.44, 28.38, 29.12, 29.46, 24.13, 22.3, 20.82, 22.98, 21.85, 23.43, 23.23, 25.99, 27.86, 24.08,
     24.09, 20.81, 28.06, 22.44],
    [20.04, 25.51, 26.83, 27.01, 20.9, 25.27, 22.39, 26.55, 24.89, 20.37, 27.78, 26.12, 25.51, 29.86, 21.3, 27.6, 21.49,
     28.01, 25.29, 21.2],
    [29.15, 24.03, 26.62, 26.6, 22.92, 25.99, 22.69, 24.56, 23.1, 24.09, 24.74, 24.13, 24.13, 27.02, 22.9, 25.02, 20.77,
     28.04, 23.67, 28.01],
    [21.71, 20.65, 29.21, 27.83, 28.69, 22.56, 25.87, 20.97, 24.16, 26.58, 20.8, 29.26, 20.61, 26.86, 22.9, 28.99,
     27.23, 22.69, 28.04, 28.52],
    [22.8, 23.96, 26.36, 25.75, 26.83, 23.34, 28.31, 20.49, 21.73, 25.0, 21.26, 20.99, 22.29, 24.74, 20.59, 24.43,
     20.74, 29.59, 23.34, 25.19],
    [20.39, 27.75, 29.19, 20.75, 22.23, 27.54, 28.33, 21.06, 29.3, 29.49, 20.54, 22.03, 29.67, 28.9, 22.92, 23.01,
     20.63, 22.35, 20.94, 22.73]
]

# min max

print(max(map(max, temp)))

print(min(map(min, temp)))

# средняя температура

dict_temp = {num_row + 1: ([round(sum(row)/len(row), 2) for row in temp])[num_row] for num_row in range(len(temp))}


print(dict_temp)


# температуры выше средней

print(
    list(
        map(
            lambda row: list(
                filter(
                    lambda elem: elem > sum(row)/len(row), row
                )), temp
            )
        )
    )

print(
    list(
        map(
            lambda row: 1/len(row) * 100 * len(
                list(
                    filter(
                        lambda elem: elem > (sum(row)/len(row)), row
                    ))), temp
                )
            )
        )




#max temp day


print(
    list(
        map(
            lambda row: list(
                filter(
                    lambda max_t: max_t == max(map(max, temp)), row
                )
            ), temp
        )
    )
)

num_row = 0
for row in temp:
    for elem in row:
        if elem == max(map(max, temp)):
            max_t = elem
            day = num_row
    num_row += 1

print(day, 'day -', max_t, 'degrees')


