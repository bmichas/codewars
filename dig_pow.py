def dig_pow(n, p):
    n = str(n)
    dig_sum = 0

    for i in n:
        i = int(i)
        dig_sum += i**p
        p += 1

    n = int(n)
    r = dig_sum % n

    if r > 0:
        return -1
    else:
        return int(dig_sum / n)


# code_wars solution cw = code wars
def dig_pow_cw(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p+i)
    return s/n if s % n == 0 else -1


def main():
    x = dig_pow(46288, 3)
    print(x)


if __name__ == "__main__":
    main()
