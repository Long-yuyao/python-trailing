class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def get_max_depth(self, t: Node) -> int:
        if not t:
            return 0
        else:
            return 1 + max(self.get_max_depth(t.left), self.get_max_depth(t.right))

    def get_min_depth(self, t: Node) -> int:
        if not t:
            return 0
        else:
            return 1 + min(self.get_min_depth(t.left), self.get_min_depth(t.right))

    def num_node(self, t: Node) -> int:
        if not t:
            return 0
        else:
            return 1 + self.num_node(t.left) + self.num_node(t.right)

    def num_klevel_node(self, t: Node, k) -> int:
        if not t or k == 0:
            return 0
        else:
            return 1 + self.num_klevel_node(t.left, k - 1) + self.num_klevel_node(t.right, k - 1)

    def is_balance(self, t: Node) -> bool:
        if not t:
            return True
        elif t.left and t.right:
            return self.is_balance(t.left) and self.is_balance(t.right)
        else:
            return False

    def is_full_btree(self, t: Node) -> bool:
        q = [t]
        while q:
            if q[0]:
                q.append(q[0].left)
                q.append(q[0].right)
                q.pop(0)
            else:
                if q == [None] * len(q):
                    return True
                else:
                    return False

    def is_same_tree(self, t1: Node, t2: Node) -> bool:
        if t1 and t2:
            if t1.value == t2.value:
                return self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right)
            else:
                return False
        elif not t1 and not t2:
            return True
        else:
            return False

    def is_mirror(self, t1: Node, t2: Node) -> bool:
        if t1 and t2:
            if t1.value == t2.value:
                return self.is_same_tree(t1.left, t2.right) and self.is_same_tree(t1.right, t2.left)
            else:
                return False
        elif not t1 and not t2:
            return True
        else:
            return False

    def mirror_tree(self, t1: Node) -> Node:
        if t1:
            t2 = Node(t1.value)
            t2.left = self.mirror_tree(t1.right)
            t2.right = self.mirror_tree(t1.left)
        else:
            t2 = None
        return t2

    # def get_last_common_parent(self, root, t1, t2):
    #     if find(root, t1)

    def insert_node(self, root: Node, t: Node) -> Node:
        if not root:
            root = t
        else:
            tmp = root
            while tmp:
                parent = tmp
                if t.value <= parent.value:
                    tmp = tmp.left
                else:
                    tmp = tmp.right
            if t.value <= parent.value:
                parent.left = t
            else:
                parent.right = t
        return root

    """
    输⼊⼀个⼆叉树和⼀个整数，打印出⼆叉树中节点值的和等于输⼊整数所有的路径
    """

    def find_path(self, t: Node, value: int, s=0, path=[]) -> None:
        s = s + t.value
        path.append(s)
        if s == value:
            print(path)
        else:
            if t.left:
                self.find_path(t.left, value, s, path)
            if t.right:
                self.find_path(t.right, value, s, path)

    """
    给定两个值 k1 和 k2（k1 < k2）和⼀个⼆叉查找树的根节点。找到树中所有值在 k1 到
    k2 范围内的节点。即打印所有x (k1 <= x <= k2) 其中 x 是⼆叉查找树的中的节点值。返
    回所有升序的节点值。
    """

    def find_node(self, k1: int, k2: int, t: Node, l: list = []) -> list:
        if t:
            if k1 <= t.value <= k2:
                l.append(t)
            elif t.value < k1:
                self.find_node(k1, k2, t.right, l)
            else:
                self.find_node(k1, k2, t.left, l)

    """
    ⼆叉树内两个节点的最⻓距离
    ⼆叉树中两个节点的最⻓距离可能有三种情况：
    1.左⼦树的最⼤深度+右⼦树的最⼤深度为⼆叉树的最⻓距离
    2.左⼦树中的最⻓距离即为⼆叉树的最⻓距离
    3.右⼦树种的最⻓距离即为⼆叉树的最⻓距离
    """

    def longest(self, t: Node) -> int:
        if t:
            return max(self.get_max_depth(t.left) + self.get_max_depth(t.right), self.longest(t.left),
                       self.longest(t.right))
        else:
            return 0

    """
    给出 n，问由 1...n 为节点组成的不同的⼆叉查找树有多少种？
    """

    def diff_tree(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = dp[i] + dp[j] * dp[i - j - 1]
        return dp[-1]

    """
    判断⼆叉树是否是合法的⼆叉查找树(BST)
    ⼀棵BST定义为：
    节点的左⼦树中的值要严格⼩于该节点的值。
    节点的右⼦树中的值要严格⼤于该节点的值。
    左右⼦树也必须是⼆叉查找树。
    ⼀个节点的树也是⼆叉查找树。
    """

    def is_search_tree(self, t: Node) -> bool:
        if t:
            if t.left and t.left.value > t.value:
                return False
            elif t.right and t.right.value < t.value:
                return False
            else:
                return self.is_search_tree(t.left) and self.is_search_tree(t.right)
        else:
            return True


if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.left.left = Node(4)
    t.left.right = Node(5)
    t.right.right = Node(7)
    print(Tree().is_full_btree(t))
