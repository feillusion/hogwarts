class ArrayStack:
    def __init__(self, capacity):
        # 为堆栈分配指定长度的空间
        self.data = [-1] * capacity
        self.max = capacity
        # 记录堆栈的长度（初始为0）
        self.count = 0

    def push(self, value):
        """增加数据"""
        # 如果堆栈已满，返回False
        if self.count == self.max:
            return False
        # 如果堆栈未满，则在最新位置（索引为self.count）添加新数据，并将堆栈长度加1
        self.data[self.count] = value
        self.count = self.count + 1
        return True

    def pop(self):
        """删除数据"""
        # 如果堆栈为空，返回False
        if self.count == 0:
            return None
        # 如果堆栈不为空，则将堆栈长度减1，并返回最后位置的数据
        self.count = self.count -1
        return self.data[self.count]


def test_static():
    array_stack = ArrayStack(5)
    data = ["a", "b", "c", "d", "e"]
    for i in data:
        array_stack.push(i)

    result = array_stack.push("a")
    assert not result
    data.reverse()
    for i in data:
        assert i == array_stack.pop()

    assert array_stack.pop() is None


if __name__ == '__main__':
    test_static()