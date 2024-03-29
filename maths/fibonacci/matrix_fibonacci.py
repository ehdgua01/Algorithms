from typing import List

MatrixType = List[List[int]]


def matrix_fibonacci(number: int) -> int:
    if number < 2:
        return number
    return matrix_power([[1, 1], [1, 0]], number)[0][1]


def matrix_power(matrix: MatrixType, number: int) -> MatrixType:
    if number > 1:
        matrix = matrix_power(matrix, number // 2)
        matrix = matrix_multiply(matrix, matrix)

        if number & 1:
            matrix = matrix_multiply(matrix, [[1, 1], [1, 0]])
    return matrix


def matrix_multiply(a: MatrixType, b: MatrixType) -> MatrixType:
    return [
        [
            (a[0][0] * b[0][0]) + (a[0][1] * b[1][0]),
            (a[0][0] * b[1][0]) + (a[0][1] * b[1][1]),
        ],
        [
            (a[1][0] * b[0][0]) + (a[1][1] * b[1][0]),
            (a[1][0] * b[1][0] + a[1][1] * b[1][1]),
        ],
    ]
