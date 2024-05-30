import numpy as np
import math

DEBUG_MODE=0

class MatrixParser:
    def __init__(self):
        self.x_size = 0
        self.y_size = 0

    def get_r_matrix(self, initial_matrix):
        out_r_matrix = self.__convert_to_matrix(initial_matrix)

        return out_r_matrix

    def __convert_to_matrix(self, initial_matrix):
        x_max, y_max = len(initial_matrix[0]), len(initial_matrix)
        self.x_size = x_max
        self.y_size = y_max

        i_min, i_max = 0, x_max - 1#0,1 - 2
        j_min, j_max = 0, y_max - 1#0,3 - 4

        matrix_r = [[-1 for _ in range(x_max * y_max)] for _ in range(x_max * y_max)]

        for i, x_value in enumerate(initial_matrix):
            for j, y_value in enumerate(x_value):
                if y_value == 1:
                    continue
                if y_value == 3:
                    matrix_r[(i * x_max) + j][(i * x_max) + j] = 100
                    self.target = i * self.x_size + j

                if y_value == 2:
                    self.start = i * self.x_size + j

                if DEBUG_MODE == 1:
                    print(f"from {(i * x_max) + j}: ", end='')
                # top
                if i - 1 in range(j_min, j_max + 1) and initial_matrix[i - 1][j] in (0, 2, 3):
                    matrix_r[(i * x_max) + j][((i - 1) * x_max + j)] = 0 if initial_matrix[i - 1][j] in (0, 2) else 100
                    if DEBUG_MODE == 1:
                        print(f"to {((i - 1) * x_max + j)} ", end='')
                # bottom
                if i + 1 in range(j_min, j_max + 1) and initial_matrix[i + 1][j] in (0, 2, 3):
                    matrix_r[(i * x_max) + j][((i + 1) * x_max + j)] = 0 if initial_matrix[i + 1][j] in (0, 2) else 100
                    if DEBUG_MODE == 1:
                        print(f"to {((i + 1) * x_max + j)} ", end='')
                # right
                if j + 1 in range(i_min, i_max + 1) and initial_matrix[i][j + 1] in (0, 2, 3):
                    matrix_r[(i * x_max) + j][(i * x_max + j + 1)] = 0 if initial_matrix[i][j + 1] in (0, 2) else 100
                    if DEBUG_MODE == 1:
                        print(f"to {(i * x_max + j + 1)} ", end='')
                # left
                if j - 1 in range(i_min, i_max + 1) and initial_matrix[i][j - 1] in (0, 2, 3):
                    matrix_r[(i * x_max) + j][(i * x_max + j - 1)] = 0 if initial_matrix[i][j - 1] in (0, 2) else 100
                    if DEBUG_MODE==1:
                        print(f"to {(i * x_max + j - 1)} ", end='')

                if DEBUG_MODE == 1:
                    print()

        return matrix_r