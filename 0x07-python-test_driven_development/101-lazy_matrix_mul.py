#!/usr/bin/python3
"""Multiplication function using Numpy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Args:
        m_a (list of list of ints/floats): first matrix
        m_b (list of list of ints/floats): second matrix
    """

    return (np.matmul(m_a, m_b))
