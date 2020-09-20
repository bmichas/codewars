def DNA_strand(dna):

    DNA_TAB = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    fin_dna = ""
    for i in range(len(dna)):
        letter = dna[i]
        fin_dna += DNA_TAB[letter]
    return fin_dna


# code_wars solution cw = code wars
def DNA_strand_cw(dna):
    #pairs = {'A':'T','T':'A','C':'G','G':'C'}
    return dna.translate(str.maketrans("ATCG", "TAGC"))
    # return ''.join([pairs[x] for x in dna])
    # kom inne rozwiazanie co mi sie podoba


def main():
    ret_dna = DNA_strand('GATC')
    print(ret_dna)


if __name__ == "__main__":
    main()
