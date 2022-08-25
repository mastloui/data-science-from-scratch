from typing import List
Vector = List[float]

height_weight_age = [70, 170, 40]
height_weight_age_2 = [80, 230, 31]


def add(v: Vector, w:  Vector) -> Vector:
    assert len(v) == len(w), "vectors must be of the same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def substract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be of the same length"
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"

    num_elements = len(vectors[0])
    assert all(length(v) == num_elements for v in vectors), "different sizes!"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]


def scalar_multiply(c:float, v: Vector) -> Vector:
    return [v_i * c for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:

    num_elements = len(vectors)
    return scalar_multiply(1.0/num_elements, vector)
