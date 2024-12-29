def main(childrens, cookies):
    cookies.sort(reverse=True)
    happy = 0
    for children in sorted(childrens, reverse=True):
        if children <= cookies[happy]:
            happy += 1
        if len(cookies) == happy:
            return happy
    return happy


if __name__ == '__main__':
    _ = input()
    childrens = list(map(int, input().split()))
    _ = input()
    cookies = list(map(int, input().split()))
    print(main(childrens, cookies))
