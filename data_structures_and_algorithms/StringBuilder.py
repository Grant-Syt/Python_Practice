"""
Cracking the Coding Interview p.90

A data structure for concatenating n strings of length x in O(nx) time rather 
than O(xn^2) time. Rather than copying the string at each concatenation, we
store the strings in a resizable array until, copying them back to a string when
necessary.

"""

from time import perf_counter

test_str = "abcdef"
test_range = 3000000


class StringBuilder:

    def __init__(self) -> None:
        self.arrList = []

    def append(self, str):
        self.arrList.append(str)

    def toString(self):
        return "".join(self.arrList)


def test_string_builder():
    sb = StringBuilder()
    for _ in range(test_range):
        sb.append(test_str)
    return sb.toString()


def test_concat():
    out_str = ""
    for _ in range(test_range):
        out_str += test_str
    return out_str

def test_join():
    arr = []
    for _ in range(test_range):
        arr.append(test_str)
    return "".join(arr)


def time_func(func):
    start = perf_counter()
    func()
    end = perf_counter()
    return end-start


if __name__ == "__main__":
    sb_time = time_func(test_string_builder)
    c_time = time_func(test_concat)
    f_time = time_func(test_join)
    print(f"\nstring builder time:{sb_time}")
    print(f"concatenation time: {c_time}")
    print(f"join time: {f_time}")
