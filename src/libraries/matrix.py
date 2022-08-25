from typing import List, Tuple

Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (rowCount, columnCount)"""
    
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

