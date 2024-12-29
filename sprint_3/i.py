def main(universities, k):
    cnts = [(0, 0)] * (max(universities) + 1)
    for university in universities:
        id_uni, cnt = cnts[university]
        cnts[university] = (university, cnt + 1)
    i = 0
    for unim, cnt in sorted(cnts, key=lambda x: x[1], reverse=True):
        if i >= k or not cnt:
            break
        yield unim
        i += 1



if __name__ == '__main__':
    input()
    universities = list(map(int, input().split()))
    k = int(input())

    for uni in main(universities, k):
        print(uni, end=' ')
