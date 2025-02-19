# https://contest.yandex.ru/contest/24810/run-report/133662326/
"""
-- ПРИНЦИП РАБОТЫ --
1) Находим родителя для удаляемого узла (случай когда такого нет, обрабатывается отдельно)
2) Если нашли нужно объединить его потомков, взяв самый правый узел в левом дереве
3) Вернуть "голову", даже если не поменялась

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Продуманы все варианты при поиске и перестановке:
1) Когда есть оба потомка
2) Есть только левый
3) Есть только правый

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
h - высота дерева
О(h) на поиск родителя узла для удаления (худший случай)
О(h) на поиск узла для подстановки вместо удаленного (худший случай)
Итого: О(h)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
n - кол-во элементов
O(n) - на дерево
O(n) - на "текущее дерево" (но думаю там тот же объект)
O(с) - на перемещение узлов
Итого: O(n)
"""
from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

        def __str__(self):
            return f'Node({self.value})'
else:
    from node import Node


def replace_right(root):
    while root:
        if root.right is None:
            return root
        if root.right.right is None:
            right_node = root.right
            root.right = right_node.left
            return right_node
        root = root.right


def merge_tree(left_tree: Optional[Node], right_tree: Optional[Node]):
    if not left_tree:
        return right_tree
    if not right_tree:
        return left_tree
    node = replace_right(left_tree)
    node.right = right_tree
    if left_tree is not node:
        node.left = left_tree
    return node


def remove(root, key) -> Optional[Node]:
    cur_root = root
    while cur_root:
        if cur_root.value == key:
            node = merge_tree(cur_root.left, cur_root.right)
            return node

        if cur_root.right is not None and cur_root.right.value == key:
            cur_root.right = merge_tree(cur_root.right.left, cur_root.right.right)
            return root

        if cur_root.left is not None and cur_root.left.value == key:
            cur_root.left = merge_tree(cur_root.left.left, cur_root.left.right)
            return root

        if cur_root.value < key:
            cur_root = cur_root.right
        else:
            cur_root = cur_root.left
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8

    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node10 = Node(11)
    node6 = Node(node5, node10, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8

    node4 = Node(value=11)
    node6 = Node(value=32)
    node7 = Node(value=50)
    node9 = Node(value=72)
    node10 = Node(value=99)
    node8 = Node(value=91, left=node9, right=node10)
    node5 = Node(value=29, right=node6)
    node2 = Node(value=20, left=node4, right=node5)
    node3 = Node(value=65, left=node7, right=node8)
    node1 = Node(value=41, left=node2, right=node3)
    new_head = remove(node1, 41)
    new_head.value = 32

    node = Node(value=5)
    new_node = remove(node, 5)
    assert new_node is None

    node4 = Node(value=1)
    node5 = Node(value=3)
    node6 = Node(value=5)
    node7 = Node(value=7)
    node2 = Node(value=2, left=node4, right=node5)
    node3 = Node(value=6, left=node6, right=node7)
    node1 = Node(value=4, left=node2, right=node3)
    new_head = remove(node1, 2)
    assert new_head is node1
    assert new_head.left is node4
    assert new_head.left.left is None

    node0 = Node(value=0)
    node4 = Node(value=1, left=node0)
    node5 = Node(value=3)
    node6 = Node(value=5)
    node7 = Node(value=7)
    node2 = Node(value=2, left=node4, right=node5)
    node3 = Node(value=6, left=node6, right=node7)
    node1 = Node(value=4, left=node2, right=node3)
    new_head = remove(node1, 2)
    assert new_head is node1
    assert new_head.left is node4
    assert new_head.left.left is node0

    node4 = Node(value=266)
    node6 = Node(value=701)
    node8 = Node(value=822)
    node10 = Node(value=932)
    node3 = Node(value=191, right=node4)
    node2 = Node(value=298, left=node3)
    node9 = Node(value=912, right=node10)
    node7 = Node(value=870, left=node8, right=node9)
    node5 = Node(value=702, left=node6, right=node7)
    node1 = Node(value=668, left=node2, right=node5)
    assert remove(node1, 545) is node1


if __name__ == '__main__':
    test()
