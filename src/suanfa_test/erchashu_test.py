class BinarySearchTree:
    def __init__(self) -> None:
        """初始化二叉树根节点为None"""
        self.root = None

    class Node:
        def __init__(self, data):
            """初始化一个节点"""
            self.data = data
            self.left = None
            self.right = None

    def insert(self, data):
        """新增一个节点"""
        # 二叉树为空，直接将新节点作为根节点
        if self.root is None:
            self.root = self.Node(data)
            return True
        q = self.root
        # 从根节点开始查找
        while q is not None:
            # 如果要插入的数据小于当前节点，就去找当前节点的左子节点，若没有左子节点，将新数据作为左子节点插入
            if data < q.data:
                if q.left is None:
                    q.left = self.Node(data)
                    return True
                q = q.left
            # 如果要插入的数据小于当前节点，就去找当前节点的右子节点，若没有右子节点，将新数据作为右子节点插入
            elif data > q.data:
                if q.right is None:
                    q.right = self.Node(data)
                    return True
                q = q.right

    def find(self, data):
        """查询对应数据的节点"""
        q = self.root
        # 从根节点开始查询，如果当前节点为None，说明没有匹配的节点
        while q is not None:
            # 如果当前的节点数据匹配，返回当前节点
            if data == q.data:
                return q
            # 如果当前数据偏大，就去找左子节点
            if data < q.data:
                q = q.left
            # 如果当前数据偏小，就去找右子节点
            elif data > q.data:
                q = q.right
        return None

    def delete(self, data, instead_from_right=True):
        """删除对应数据的节点"""
        q = self.root
        p = None

        # 先找出匹配的节点，用q表示，p表示匹配节点的父节点
        while q is not None and data != q.data:
            p = q
            if data < q.data:
                q = q.left
            elif data > q.data:
                q = q.right

        # 若果q节点是None，说明没有找到匹配节点
        if q is None:
            return None

        # 如果q节点的左右子节点都不为空
        if q.left is not None and q.right is not None:
            # 则找到其右子节点中的最小值替代q节点数据，并删除其原节点
            if instead_from_right:
                child = q.right
                p_child = q
                while child.left is not None:
                    p_child = child
                    child = child.left
            # 或找到其左子节点中的最大值替代q节点数据，并删除其原节点
            else:
                child = q.left
                p_child = q
                while child.right is not None:
                    p_child = child
                    child = child.right
            # 将该最大/小值替代q节点数据
            q.data = child.data
            # 将该最大/小值的节点作为要删除的节点，继续处理（相当于转换成删除单子节点的节点）
            q = child
            p = p_child

        # 如果q节点只有1个或没有子节点（记为None），则记录其子节点after_q，将q节点的父节点指向after_q实现q节点的删除
        if q.left is None:
            after_q = q.right
        elif q.right is None:
            after_q = q.left
        else:
            after_q = None
        # 若q节点是根节点，则将after_q节点作为新的根节点实现对q的删除
        if p is None:
            self.root = after_q
        # 如果q是p的左子节点，节将p的左子节点指向after_q，否则将p的右子节点指向after_q，实现对q的删除
        elif p.left is q:
            p.left = after_q
        else:
            p.right = after_q

    def pre_order(self, node):
        """根据给定节点前序遍历"""
        if node is None:
            return None
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def pre_order_by_value(self, data):
        """根据给定数据前序遍历"""
        self.pre_order(self.find(data))

    def in_order(self, node):
        """根据给定节点中序遍历"""
        if node is None:
            return None
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def in_order_by_value(self, data):
        """根据给定数据中序遍历"""
        self.in_order(self.find(data))

    def post_order(self, node):
        """根据给定节点后序遍历"""
        if node is None:
            return None
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

    def post_order_by_value(self, data):
        """根据给定数据后序遍历"""
        self.post_order(self.find(data))


def test_binary_search_tree():

    binary_search_tree = BinarySearchTree()
    data = [1, 10, 20, 40, 13]
    for i in data:
        binary_search_tree.insert(i)
    assert 20 == binary_search_tree.find(20).data
    binary_search_tree.delete(20, instead_from_right=True)
    assert binary_search_tree.find(20) is None
    # 1 10 40 13
    binary_search_tree.pre_order(binary_search_tree.root)
    print("-----------------------")
    binary_search_tree.pre_order_by_value(1)
    print("-----------------------")
    # 1 10 13 40
    binary_search_tree.in_order(binary_search_tree.root)
    print("-----------------------")
    binary_search_tree.in_order_by_value(1)
    print("-----------------------")
    # 13 40 10 1
    binary_search_tree.post_order(binary_search_tree.root)
    print("-----------------------")
    binary_search_tree.post_order_by_value(1)


if __name__ == '__main__':
    test_binary_search_tree()