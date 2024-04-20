def check():
    with open("Floid.out", "r") as f:
        with open("Floyd_my.out", 'r') as f2:
            for el1, el2 in zip(f.readlines(), f2.readlines()):
                if el1.strip() != el2.strip():
                    print(el1)
                    print(el2)
                    return False
    return True
    # return map(lambda x: x.strip(), f.readlines()) == map(lambda x: x.strip,  f.readlines())


def main():
    p: list
    d: list

    # read W matrix
    with open("job_Var12.in", "r") as f:
        n = int(f.readline()) # n * n matrix
        # n = map(int, f.readline().split())[0]
        p = [[i] * n for i in range(1, n + 1)]
        d = [[0] * n for i in range(1, n + 1)]
        for i in range(n):
            d[i] = list(map(lambda x: int(x) if x != '*' else '*', f.readline().split()))

    f = open("job_Var12.out", "w")

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] == '*' or d[k][j] == '*':
                    continue

                alt_weight = d[i][k] + d[k][j]
                if d[i][j] == '*':
                    d[i][j] = alt_weight
                    p[i][j] = k + 1

                elif alt_weight < d[i][j]:
                    d[i][j] = alt_weight
                    p[i][j] = p[k][j]

        print(k + 1, file=f)
        # d
        print("D:", file=f)
        for j in range(n):
            print(*d[j], file=f)
        # p
        print("P:", file=f)
        for j in range(n):
            print(*p[j], file=f)

    f.close()


if __name__ == '__main__':
    main()
