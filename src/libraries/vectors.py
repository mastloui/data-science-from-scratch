from math import sqrt
from typing import List

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def substract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v,w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided"

    num_elements = len(vectors[0])

    assert all(len(v) == num_elements for v in vectors)

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    num_vectors = len(vectors)
    return scalar_multiply(1/num_vectors, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> Vector:
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1,2,3], [4,5,6]) == 32


def sum_of_squares(v: Vector) -> Vector:
    return dot(v, v)

def magnitude(v: Vector) -> float:
    return sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(substract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return magnitude(substract(v, w))