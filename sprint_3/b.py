d = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def main(numbers, prefix=''):
    if len(numbers) == 1:
        return (prefix + letter for letter in d[numbers])
    for l in main(numbers[0]):
        yield from main(numbers[1::], prefix + l)


def gen(s):
    return (letter for letter in d[s])



if __name__ == '__main__':
    # s = input()
    s = '2'
    g = gen(s)
    print(next(g))
    # for l in g:
    #     print(l, end=' ')
