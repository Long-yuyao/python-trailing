import copy


class BinaryTree:
    # define and init a binary tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # preorder traversal
    def preorder_traversal(self, tree) -> None:
        if tree:
            self.preorder_traversal(tree.left)
            print(tree.data)
            self.preorder_traversal(tree.right)

    # preorder non-recursive
    def preorder_non_recursive(self, tree) -> None:
        if tree:
            data_store = []
            ctree = copy.deepcopy(tree)
            data_store.append(ctree.right)
            data_store.append(ctree.data)
            ctree = ctree.left
            while data_store or ctree:
                while ctree:
                    data_store.append(ctree.right)
                    data_store.append(ctree.data)
                    ctree = ctree.left
                print(data_store[-1])
                data_store.pop(-1)
                ctree = data_store[-1]
                data_store.pop(-1)

    # To judge a tree if is a full tree
    def isfulltree(self, tree) -> bool:
        if not tree:
            return True
        elif tree.right and tree.left:
            return self.isfulltree(tree.left) and self.isfulltree(tree.right)
        else:
            return False

    def depth_of_tree(self, tree) -> int:
        return 1 + max(self.depth_of_tree(tree.left), self.depth_of_tree(tree.right)) if tree else 0


if __name__ == '__main__':
    bitree = BinaryTree(1)
    bitree.left = BinaryTree(2)
    bitree.right = BinaryTree(3)
    bitree.left.left = BinaryTree(4)
    bitree.preorder_traversal(bitree)
    bitree.preorder_non_recursive(bitree)
    if bitree.isfulltree(bitree):
        print("This is a full tree")
    else:
        print("This is not a full tree")
    print("The depth of tree is {}".format(bitree.depth_of_tree(bitree)))
