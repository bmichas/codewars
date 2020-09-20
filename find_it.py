def find_it(seq):
    res = 0
    for element in seq:
        res = res ^ element
    return res


def main():
    diff_num = find_it(
        [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
    print(diff_num)


# code_wars solution cw = code wars
def find_it_cw(seq):
    return [x for x in seq if seq.count(x) % 2][0]


if __name__ == "__main__":
    main()
