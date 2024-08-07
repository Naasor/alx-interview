#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise.
    Args:
    matrix (list of list of int): The matrix to rotate
    Returns:
    None: The matrix is modified in-place
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
