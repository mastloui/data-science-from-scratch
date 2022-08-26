from collections import Counter
import matplotlib.pyplot as plt
from math import sqrt
from typing import List
from ...libraries.vectors import mean, sum_of_squares 

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def show_histogram(friends_data):
    friends_count = Counter(num_friends)

    xs = range(101)
    ys = [friends_count[x] for x in xs]

    plt.bar(xs,ys)
    plt.axis([0,101,0,25])
    plt.title("Histogram of Friend Counts")
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.show()


def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    n = len(xs)
    assert n >= 2

    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def std_dev(xs: List[float]) -> float:
    return sqrt(variance(xs))

def quantile_range(xs: List[float], p) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def print_statistics(friends_data: List[float]):
    num_datapoints = len(friends_data)
    max_value = max(friends_data)
    min_value = min(friends_data)
    print(f"Number of data points: {num_datapoints}")
    print(f"Max value: {num_datapoints}")
    print(f"Min value: {num_datapoints}")

def print_dispersion(friends_data):
    data_range = max(friends_data) - min(friends_data)
    print(f"Dispersion: {data_range}")

show_histogram(num_friends)
print_statistics(num_friends)
print_dispersion(num_friends)