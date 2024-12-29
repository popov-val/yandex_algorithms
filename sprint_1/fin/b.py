# https://contest.yandex.ru/contest/22450/run-report/129372110/
def get_cnts(tablo):
    cnts = {}
    for s in tablo:
        if s == '.':
            continue
        if cnts.get(s):
            cnts[s] += 1
        else:
            cnts[s] = 1
    return cnts


def func(k, tablo):
    cnts = get_cnts(tablo)
    wins = 0
    for i in range(1, 10):
        cnt = cnts.get(str(i))
        if cnt and cnt <= k * 2:
            wins += 1
    return wins


if __name__ == '__main__':
    k = int(input())
    tablo = ''.join(input() for i in range(4))
    print(func(k, tablo))
