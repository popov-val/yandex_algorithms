def main(s):
    uniq_els = set()
    max_len = 1
    for i, f_el in enumerate(s):
        uniq_els = set(f_el)
        for el in s[i + 1:]:
            if el in uniq_els:
                max_len = max(max_len, len(uniq_els))
                # uniq_els = set(el)
                break
            else:
                uniq_els.add(el)
        max_len = max(max_len, len(uniq_els))
    return max(max_len, len(uniq_els))


def test():
    assert main('abcabcbb') == 3
    assert main('bbbbb') == 1
    assert main('pwwkew') == 3
    assert main('awe') == 3


if __name__ == '__main__':
    # test()
    print(main(input()))
