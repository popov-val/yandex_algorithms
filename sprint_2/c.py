import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

        def __str__(self):
            return f'{self.value} -> {self.next_item}'


def solution(node, idx):
    if idx == 0:
        return node.next_item

    prev_node = node
    for i in range(idx - 1):
        prev_node = prev_node.next_item

    prev_node.next_item = prev_node.next_item.next_item

    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    # new_head = solution(node0, 1)
    # assert new_head is node0
    # assert new_head.next_item is node2
    # assert new_head.next_item.next_item is node3
    # assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3

    new_head = solution(node0, 2)
    assert new_head is node0
    assert new_head.next_item is node1
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


if __name__ == '__main__':
    test()
