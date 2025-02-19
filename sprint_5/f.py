import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

        def __str__(self):
            return f'Node({self.value})'


def get_depth(root):
    if root is None:
        return 0
    return max(get_depth(root.left), get_depth(root.right)) + 1


def solution(root) -> int:
    return get_depth(root)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == '__main__':
    test()
