class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_to_head(self, value):
        """在头部插入一个节点"""
        # 生成要插入的新节点
        new_node = self.Node(value)
        # 如果链表为空，直接将新节点赋值给头结点
        if self.head is None:
            self.head = new_node
            return True

        # 如果链表不为空，先将新节点的next指向头结点，再将新节点赋值给头结点成为新的头结点
        new_node.next = self.head
        self.head = new_node
        return True

    def insert_tail(self, value):
        """在尾部插入一个节点"""
        # 如果链表为空，则直接调用插入到头部函数
        if self.head is None:
            self.insert_to_head(value)
            return True

        # 链表不为空时，先生成要插入的新节点
        new_node = self.Node(value)
        q = self.head
        # 从头部开始寻找最后一个节点
        while q.next is not None:
            q = q.next
        # 将最后一个节点的next指向新节点生成新的尾结点
        q.next = new_node
        return True

    def delete_by_value(self, value):
        """根据数据删除节点"""
        # 如果链表为空直接返回False
        if self.head is None:
            return False

        # 如果链表不为空，从头节点开始寻找目标节点，p指向当前节点的前节点
        q = self.head
        p = None
        if self.head.data == value:
            self.head = self.head.next
            return True
        while q.data != value and q.next is not None:
            p = q
            q = q.next
        # 循环查询完毕后，如果q不匹配，说明没找到目标节点，返回False
        if q.data != value:
            return False
        # 如果q匹配，将q的前节点（q）的next直接指向q的后一节点（q.next，可以为None），实现将q节点从链表中的删除
        p.next = q.next
        return True

    def find_by_value(self, value):
        """根据数据查找节点"""
        # 从头结点开始，如果q节点不匹配且不为None，则继续查找下一个，最后返回q（未匹配到则为None）
        q = self.head
        while q is not None and q.data != value:
            q = q.next
        return q

    def insert_after(self, node, value):
        """插入到指定节点后"""
        # 如果链表为空或指定节点未给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个
        q = self.head
        while q.data != node.data and q.next is not None:
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q节点的next，将q节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.next = q.next
        q.next = new_node
        return True

    def insert_before(self, node, value):
        """插入到指定节点前"""
        # 如果链表为空或指定节点为给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个，p节点记录当前节点的上一节点
        q = self.head
        p = None
        while q.data != node.data and q.next is not None:
            p = q
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q，将p节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.next = q
        if p is not None:
            p.next = new_node
        else:
            self.head = new_node
        return True

    def print_all(self):
        """打印所有节点"""
        # 从头结点开始，只要节点不为None，就打印
        q = self.head
        while q is not None:
            print(q.data)
            q = q.next

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


class SinglyCycleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_to_head(self, value):
        """在头部插入一个节点"""
        # 生成要插入的新节点
        new_node = self.Node(value)
        # 如果链表为空，直接将新节点赋值给头结点，下一结点是头结点
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return True

        # 如果链表不为空，先将新节点的next指向头结点，再将新节点赋值给头结点成为新的头结点
        new_node.next = self.head
        self.head = new_node
        return True

    def insert_tail(self, value):
        """在尾部插入一个节点"""
        # 如果链表为空，则直接调用插入到头部函数
        if self.head is None:
            self.insert_to_head(value)
            return True

        # 链表不为空时，先生成要插入的新节点
        new_node = self.Node(value)
        q = self.head
        # 从头部开始寻找最后一个节点
        while q.next is not None:
            q = q.next
        # 将最后一个节点的next指向新节点生成新的尾结点，新的尾结点next要指向头结点
        q.next = new_node
        new_node.next = self.head
        return True

    def delete_by_value(self, value):
        """根据数据删除节点"""
        # 如果链表为空直接返回False
        if self.head is None:
            return False

        # 如果链表不为空，从头节点开始寻找目标节点，p指向当前节点的前节点
        q = self.head
        p = None
        if self.head.data == value:
            while q.next != self.head:
                q = q.next
            q.next = self.head.next
            self.head = self.head.next
            return True
        while q.data != value and q.next is not None:
            p = q
            q = q.next
        # 循环查询完毕后，如果q不匹配，说明没找到目标节点，返回False
        if q.data != value:
            return False
        # 如果q匹配，将q的前节点（q）的next直接指向q的后一节点（q.next），实现将q节点从链表中的删除
        p.next = q.next
        return True

    def find_by_value(self, value):
        """根据数据查找节点"""
        # 从头结点开始，如果q节点不匹配且不为None，则继续查找下一个，最后返回q（未匹配到则为None）
        q = self.head
        n = 0
        while q is not None and q.data != value:
            if q.next == self.head:
                return None
            q = q.next
        return q

    def insert_after(self, node, value):
        """插入到指定节点后"""
        # 如果链表为空或指定节点未给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个
        q = self.head
        while q.data != node.data and q.next != self.head:
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q节点的next，将q节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.next = q.next
        q.next = new_node
        return True

    def insert_before(self, node, value):
        """插入到指定节点前"""
        # 如果链表为空或指定节点未给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个，p节点记录当前节点的上一节点
        q = self.head
        p = None
        while q.data != node.data and q.next != self.head:
            p = q
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q，将p节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.next = q
        if p is not None:
            p.next = new_node
        else:
            p = self.head
            while p.next != self.head:
                p = p.next
            p.next = new_node
            self.head = new_node
        return True

    def print_all(self):
        """打印所有节点"""
        # 从头结点开始，只要节点不为None，就打印，当节点的next是头结点时，打印完毕
        q = self.head
        while q is not None:
            print(q.data)
            if q.next == self.head:
                break
            q = q.next

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_to_head(self, value):
        """在头部插入一个节点"""
        # 生成要插入的新节点
        new_node = self.Node(value)
        # 如果链表为空，直接将新节点赋值给头结点
        if self.head is None:
            self.head = new_node
            return True

        # 如果链表不为空，先将新节点的next指向头结点，再将新节点赋值给头结点成为新的头结点
        new_node.next = self.head
        self.head.pre = new_node
        self.head = new_node
        return True

    def insert_tail(self, value):
        """在尾部插入一个节点"""
        # 如果链表为空，则直接调用插入到头部函数
        if self.head is None:
            self.insert_to_head(value)
            return True

        # 链表不为空时，先生成要插入的新节点
        new_node = self.Node(value)
        q = self.head
        # 从头部开始寻找最后一个节点
        while q.next is not None:
            q = q.next
        # 将最后一个节点的next指向新节点生成新的尾结点
        q.next = new_node
        new_node.pre = q
        return True

    def delete_by_value(self, value):
        """根据数据删除节点"""
        # 如果链表为空直接返回False
        if self.head is None:
            return False

        # 如果链表不为空，从头节点开始寻找目标节点
        q = self.head
        if self.head.data == value:
            self.head = self.head.next
            self.head.pre = None
            return True
        while q.data != value and q.next is not None:
            q = q.next
        # 循环查询完毕后，如果q不匹配，说明没找到目标节点，返回False
        if q.data != value:
            return False
        # 如果q匹配，将q的前节点（q.pre）的next直接指向q的后一节点（q.next，可以为None），实现将q节点从链表中的删除
        q.pre.next = q.next
        q.next.pre = q.pre
        return True

    def find_by_value(self, value):
        """根据数据查找节点"""
        # 从头结点开始，如果q节点不匹配且不为None，则继续查找下一个，最后返回q（未匹配到则为None）
        q = self.head
        while q is not None and q.data != value:
            q = q.next
        return q

    def insert_after(self, node, value):
        """插入到指定节点后"""
        # 如果链表为空或指定节点未给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个
        q = self.head
        while q.data != node.data and q.next is not None:
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q节点的next，将q节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.pre = q
        new_node.next = q.next
        if q.next is not None:
            q.next.pre = new_node
        q.next = new_node
        return True

    def insert_before(self, node, value):
        """插入到指定节点前"""
        # 如果链表为空或指定节点为给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个
        q = self.head
        while q.data != node.data and q.next is not None:
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q，将p节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.next = q
        new_node.pre = q.pre
        if q.pre is not None:
            q.pre.next = new_node
        q.pre = new_node
        self.head = new_node
        return True

    def print_all(self):
        """打印所有节点"""
        # 从头结点开始，只要节点不为None，就打印
        q = self.head
        while q is not None:
            print(q.data)
            q = q.next

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.pre = None


class DoubleCycleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_to_head(self, value):
        """在头部插入一个节点"""
        # 生成要插入的新节点
        new_node = self.Node(value)
        # 如果链表为空，直接将新节点赋值给头结点
        if self.head is None:
            new_node.pre = new_node
            new_node.next = new_node
            self.head = new_node
            return True

        # 如果链表不为空，先将新节点的next指向头结点，再将新节点赋值给头结点成为新的头结点
        new_node.next = self.head
        new_node.pre = self.head.pre
        self.head.pre = new_node
        self.head.pre.next = new_node
        self.head = new_node
        return True

    def insert_tail(self, value):
        """在尾部插入一个节点"""
        # 如果链表为空，则直接调用插入到头部函数
        if self.head is None:
            self.insert_to_head(value)
            return True

        # 链表不为空时，先生成要插入的新节点
        new_node = self.Node(value)
        q = self.head
        # 从头部开始寻找最后一个节点
        while q.next != self.head:
            q = q.next
        # 将最后一个节点的next指向新节点生成新的尾结点
        q.next = new_node
        self.head.pre = new_node
        new_node.next = self.head
        new_node.pre = q
        return True

    def delete_by_value(self, value):
        """根据数据删除节点"""
        # 如果链表为空直接返回False
        if self.head is None:
            return False

        # 如果链表不为空，从头节点开始寻找目标节点
        q = self.head
        if self.head.data == value:
            self.head.next.pre = self.head.pre
            self.head.pre.next = self.head.next
            self.head = self.head.next
            return True
        while q.data != value and q.next != self.head:
            q = q.next
        # 循环查询完毕后，如果q不匹配，说明没找到目标节点，返回False
        if q.data != value:
            return False
        # 如果q匹配，将q的前节点（q.pre）的next直接指向q的后一节点（q.next），实现将q节点从链表中的删除
        q.pre.next = q.next
        q.next.pre = q.pre
        return True

    def find_by_value(self, value):
        """根据数据查找节点"""
        # 从头结点开始，如果q节点不匹配且不为None，则继续查找下一个，最后返回q（未匹配到则为None）
        q = self.head
        while q is not None and q.data != value:
            if q.next == self.head:
                return None
            q = q.next
        return q

    def insert_after(self, node, value):
        """插入到指定节点后"""
        # 如果链表为空或指定节点未给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个
        q = self.head
        while q.data != node.data and q.next != self.head:
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q节点的next，将q节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.pre = q
        new_node.next = q.next
        q.next = new_node
        q.next.pre = new_node
        return True

    def insert_before(self, node, value):
        """插入到指定节点前"""
        # 如果链表为空或指定节点为给出，直接返回False
        if self.head is None or node is None:
            return False
        # 从头结点开始，如果q节点不匹配且下一个节点不为None，则继续查找下一个
        q = self.head
        while q.data != node.data and q.next != self.head:
            q = q.next
        # 查找完毕，如果q节点不匹配说明没有匹配节点，返回False
        if q.data != node.data:
            return False
        # 查找到匹配节点后，将新节点的next指向q，将p节点的next指向新节点实现插入
        new_node = self.Node(value)
        new_node.next = q
        new_node.pre = q.pre
        q.pre.next = new_node
        q.pre = new_node
        self.head = new_node
        return True

    def print_all(self):
        """打印所有节点"""
        # 从头结点开始，只要节点不为None，就打印，当下一个节点是头结点时说明打印完毕
        q = self.head
        while q is not None:
            print(q.data)
            if q.next == self.head:
                break
            q = q.next

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.pre = None


def test_link():
    link = SinglyLinkedList()
    data = [1, 2, 5, 3, 1]
    for i in data:
        link.insert_tail(i)
    link.insert_to_head(99)
    # 打印内容为 99 1 2 5 3 1
    link.print_all()
    link.delete_by_value(2)
    assert not link.delete_by_value(999)
    assert link.delete_by_value(99)
    # 打印内容为 1 5 3 1
    link.print_all()
    assert link.find_by_value(2) is None
    new_node = link.find_by_value(3)
    link.insert_after(new_node, 10)
    assert link.find_by_value(3).next.data == 10
    link.insert_before(new_node, 30)
    assert link.find_by_value(5).next.data == 30


if __name__ == '__main__':
    test_link()
