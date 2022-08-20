
def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [int(first) | float(first), *rest]:
            return first + sum_list(rest)
        case _:
            raise ValueError(f"Can only sum lists of numbers")


sum_list([45.94, 46.17, 46.72])  # 138.82999999999998
