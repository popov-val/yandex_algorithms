import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def get_cnt(root):
    if root is None:
        return 0, True

    if root.left is None and root.right is None:
        return 1, True

    if root.right is not None:
        cnt_right, is_bal_right = get_cnt(root.right)
    else:
        cnt_right, is_bal_right = 0, False

    if root.left is not None:
        cnt_left, is_bal_left = get_cnt(root.left)
    else:
        cnt_left, is_bal_left = 0, False
    return max(cnt_left + 1, cnt_right + 1), is_bal_right and is_bal_left


def solution(root) -> bool:
    left, is_bal_left = get_cnt(root.left)
    right, is_bal_right = get_cnt(root.right)
    return abs(right - left) <= 1 and is_bal_right and is_bal_left


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)

    node0 = Node(0)
    node2 = Node(2)
    node1 = Node(1, node0, node2)
    assert solution(node1)

    node3 = Node(3)
    node6 = Node(6)
    node0 = Node(0, node3, node6)
    node2 = Node(2)
    node1 = Node(1, node0, node2)
    assert solution(node1)

    node12 = Node(12)
    node4 = Node(4, node12)
    node8 = Node(8)
    node7 = Node(7, node4, node8)
    node2 = Node(2)
    node0 = Node(0, node2, node7)
    assert not solution(node0)

    node0 = Node(0)
    assert solution(node0)


if __name__ == '__main__':
    test()
