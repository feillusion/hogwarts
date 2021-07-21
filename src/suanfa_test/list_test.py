class Array:
    def __init__(self, capacity):
        # 为列表分配制定长度的空间
        self.data = [-1] * capacity
        # 记录列表的数据长度（初始为0）
        self.count = 0
        self.max = capacity

    def insert(self, location, value):
        """指定位置插入数据"""
        # 如果列表已满，则不允许插入
        if self.count == self.max:
            return False
        # 如果插入位置不满足要求也不允许插入
        if location < 0 or location > self.count:
            return False
        # 从尾部开始将指定位置的数据整体往后迁移一位，将插入的数据放入指定位置，并将计数加1
        for i in range(self.count, location, -1):
            self.data[i] = self.data[i-1]
        self.data[location] = value
        self.count = self.count + 1
        return True

    def find(self, location):
        """查询指定位置数据"""
        # 如果查询位置不满足要求返回-1
        if location < 0 or location >= self.count:
            return -1
        # 返回指定位置的数据
        return self.data[location]

    def delete(self, location):
        """删除指定位置数据"""
        # 如果删除位置不满足要求不允许删除
        if location < 0 or location >= self.count:
            return False
        # 从指定位置开始顺序将后一个数据赋值给当前位置，实现对指定位置的删除，并将计数减1
        for i in range(location, self.count-1):
            self.data[i] = self.data[i+1]
        self.count = self.count - 1
        return True


def test_demo():
    array = Array(5)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 3)
    array.insert(2, 4)
    array.insert(4, 5)

    # 判断插入不成功
    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(2) == 4
    assert array.find(4) == 5
    assert array.find(10) == -1
    assert array.count == 5
    removed = array.delete(4)
    assert removed
    assert array.find(4) == -1
    removed = array.delete(10)
    assert not removed
    # 2 3 4 1 5
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()
