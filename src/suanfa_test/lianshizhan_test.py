class StackBasedOnLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        """添加节点"""
        new_node = self.Node(value)
        # 如果堆栈不为空，需要先将新节点的next指向原有的top节点
        if self.top is not None:
            new_node.next = self.top
        # 将新节点赋值给top节点
        self.top = new_node
        return True

    def pop(self):
        # 如果堆栈为空，返回-1
        if self.top is None:
            return -1
        # 先将要删除的节点数据取出，方便后续返回
        result = self.top.data
        # 将top节点的下一节点作为top节点实现原top节点的删除，并返回原有top节点的值
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