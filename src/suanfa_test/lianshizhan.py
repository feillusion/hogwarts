class StackBasedOnLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = self.Node(value)
        if self.top is not None:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return -1
        result = self.top.data
        self.top = self.top.next
        return result

    class Node:
        def __init__(self, value):
            self.data = value
            self.next = None


def test_static():
    stack = StackBasedOnLinkedList()
    data = [1, 2, 3, 4, 5]
    for i in data:
        stack.push(i)
    data.reverse()
    for i in data:
        assert i == stack.pop()
    assert stack.pop() == -1