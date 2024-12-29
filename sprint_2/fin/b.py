# https://contest.yandex.ru/contest/22781/run-report/130121088/
"""
-- ПРИНЦИП РАБОТЫ --
Как и указано в условии задачи, решение реализовано на стеке
При итерации по каждому элементу
 проверяется является ли элемент
 - числом, то добавляем в стек
 - операцией, то берем 2 элемента с вершины стека и выполняем операцию, результат записываем обратно

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Так как последовательно пишется в стек необходимо подставлять элементы в обратной последовательности

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(N) так как итерируемся по каждому элементу в строке
Добавление и изъятие O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В худшем случае O(N)

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)


def main(s):
    stack = Stack()
    for element in s.split():
        if any(el.isdigit() for el in element):
            stack.push(element)
            continue
        value_1 = stack.pop()
        value_2 = stack.pop()
        # Преобразование для целочисленного деления
        element = element + '/' if element == '/' else element
        command = f'{value_2} {element} {value_1}'
        value = eval(command)
        stack.push(str(value))
    return stack.pop()


if __name__ == '__main__':
    s = input()
    print(main(s))
