def main(s, t):
    mapper = {}
    if len(s) != len(t):
        return 'NO'

    for i, s_letter in enumerate(s):
        t_letter = t[i]
        if not mapper.get(s_letter):
            mapper[s_letter] = t_letter
            continue
        if mapper[s_letter] != t_letter:
            return 'NO'
    if len(mapper.values()) == len(set(t)):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    s = input()
    t = input()
    print(main(s, t))
