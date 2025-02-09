import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    if root.right is None and root.left is None:
        return root.value
    elif root.right is not None and root.left is None:
        return max(root.value, solution(root.right))
    elif root.right is None and root.left is not None:
        return max(root.value, solution(root.left))
    else:
        return max(solution(root.right), solution(root.left), root.value)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3

    node9 = Node(111)
    node8 = Node(0, right=node9)
    node7 = Node(111)
    node6 = Node(0)
    node5 = Node(0)
    node4 = Node(3, node7, node8)
    node3 = Node(3, node5, node6)
    node2 = Node(2, right=node4)
    node1 = Node(2, node3)
    node0 = Node(0, node1, node2)
    assert solution(node0) == 111


if __name__ == '__main__':
    test()