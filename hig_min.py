def high_and_low(numbers):
    numbers += " "
    check = []
    a = ""
    for i in numbers:
        if i == " ":
            check.append(a)
            a = ""
        else:
            a += i

    check = list(map(int, check))
    low = str(min(check))
    high = str(max(check))
    return low + " " + high


# code_wars solution cw = code wars
def high_and_low_cw(numbers):
    n = map(int, numbers.split(' '))
    return str(max(n)) + ' ' + str(min(n))


def main():
    minhig = high_and_low("1 232 3 4 5 -1")
    print(minhig)


if __name__ == "__main__":
    main()
