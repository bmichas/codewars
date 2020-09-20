def main():
    arr = array_diff([1, 1, 2, 3], [1, 6])
    print(arr)


def array_diff(a, b):
    if not b:
        pass
    else:
        for i in range(len(a)):
            for k in range(len(b)):
                if b[k] not in a:
                    pass
                else:
                    a.remove(b[k])
    return a


# code_wars solution cw = code wars
def array_diff_cw(a, b):
    return [x for x in a if x not in b]


if __name__ == "__main__":
    main()
