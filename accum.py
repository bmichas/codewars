def accum(s):
    final = ""
    i = 0
    for k in s:
        i += 1
        add_w = k*i
        add_w = add_w.capitalize()
        final = final + add_w + "-"
    final = final[:-1]
    return final


def main():
    c = accum("abCd")
    print(c)


# code_wars solution cw = code wars
def accum_cw(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


if __name__ == "__main__":
    main()
