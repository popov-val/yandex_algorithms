def main():
    s = list(input())
    rows = []
    for _ in range(int(input())):
        t, n_str = input().split()
        rows.append((t, int(n_str)))
    for t, n in sorted(rows, key=lambda x: x[1]):
        if n < len(s):
            s[n] = t + s[n]
        else:
            s.append(t)
    return ''.join(s)


if __name__ == '__main__':
    print(main())
