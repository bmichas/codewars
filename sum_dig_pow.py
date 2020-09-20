def sum_dig_pow(a, b):
    lst = []

    while a < b+1:

        a = str(a)
        pow_sum = 0
        p = 1

        for i in a:
            i = int(i)
            pow_sum += i ** p
            print(a, "=", pow_sum)
            p += 1

        a = int(a)

        if pow_sum == a:
            lst.append(a)

        a += 1

    return lst


# code_wars solution cw = code wars
def filter_func_cw(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a


def sum_dig_pow_cw(a, b):
    return filter(filter_func_cw, range(a, b+1))


def main():
    fin_list = sum_dig_pow(1, 100)
    print(fin_list)


if __name__ == "__main__":
    main()
