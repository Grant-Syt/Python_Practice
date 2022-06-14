from time import perf_counter
import timeit

"""
Cracking the Coding Interview p.90

StringBuilder is data structure for concatenating n strings of length x in O(nx) time rather 
than O(xn^2) time. Rather than copying the string at each concatenation, we
store the strings in a resizable array, copying them back to a string when
necessary.

Run file to test different implementations.
Adjust globals to alter test.

"""

# globals
str2test = "abcdef"
range2test = 500000


class StringBuilder:

    def __init__(self) -> None:
        self.arrList = []

    def append(self, str):
        self.arrList.append(str)

    def toString(self):
        return "".join(self.arrList)


def test_string_builder():
    sb = StringBuilder()
    for _ in range(range2test):
        sb.append(str2test)
    return sb.toString()


def test_concat():
    out_str = ""
    for _ in range(range2test):
        out_str += str2test
    return out_str

def test_join():
    arr = []
    for _ in range(range2test):
        arr.append(str2test)
    return "".join(arr)

def test_list_comp_join():
    return "".join([str2test for _ in range(range2test)])


# def time_func(func, args=None):
#     start = perf_counter()
#     if not args:
#         func()
#     else:
#         func(args)
#     end = perf_counter()
#     return end-start


if __name__ == "__main__":
    # sb_time = time_func(test_string_builder)
    # c_time = time_func(test_concat)
    # f_time = time_func(test_join)
    # print(f"\nstring builder time:{sb_time}")
    # print(f"concatenation time: {c_time}")
    # print(f"join time: {f_time}")

    res = {}
    
    for k, v in dict(globals()).items():
        if k.startswith('test_'):
            res[k] = timeit.timeit(v, number=10)
    
    print("\n")
    for k, v in sorted(res.items(), key=lambda x: x[1]):
        print('{:.5f} {}'.format(v, k))
