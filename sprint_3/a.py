brackets_map = {
    # '}': '{',
    ')': '(',
    # ']': '[',
}

class Bracket:
    def __init__(self):
        self.brackets = []
        self.is_correct = False


def check_bracket(bk_close, bk_open):
    if brackets_map.get(bk_close) == bk_open:
        return True



def is_correct(bracket):
    stack = []
    for el in bracket:
        if len(stack) == 0:
            stack.append(el)
        elif check_bracket(el, stack[-1]):
            stack.pop()
        else:
            stack.append(el)
    return len(stack) == 0


def main(n, stack=None):
    if not stack:
        stack = []

    for el in bracket:
        if len(stack) == 0:
            stack.append(el)
        elif check_bracket(el, stack[-1]):
            stack.pop()
        else:
            stack.append(el)

    return len(stack) == 0
    if n == 0:
        if flag:
            yield correct + s
        return

    if flag:
        yield from main(n - len(s), ['('], s)
    yield from main(n - 1, s + [')'])


if __name__ == '__main__':
    n = 2 * 2
    for s in main(n):
        print(s)
