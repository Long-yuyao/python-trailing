class Node:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class BinarySearch:
    def __init__(self, root=None):
        self.root = root

    def insert(self, *value_list) -> None:
        for value in value_list:
            if self.root is None:
                self.root = Node(value)
            else:
                parent = self.root
                while True:
                    if value < parent.value:
                        if parent.left is None:
                            parent.left = Node(value, parent)
                            break
                        else:
                            parent = parent.left
                    else:
                        if parent.right is None:
                            parent.right = Node(value, parent)
                            break
                        else:
                            parent = parent.right

    def search(self, value):
        if not self.root:
            print("This is an empty tree")
        else:
            node = self.root
            while node:
                if value == node.value:
                    return node
                elif value < node.value:
                    node = node.left
                else:
                    node = node.right
            print("There is no node with {}".format(value))
        return None

    def get_max(self, node):
        if not node:
            print("There is no maximum value, because the tree is empty")
            return None
        else:
            while node.right:
                node = node.right
            print("The maximum value is {}".format(node.value))
            return node.value

    def resign_node(self, old, new) -> None:
        if old.value < old.parent.value:
            old.parent.left = new
        else:
            old.parent.right = new
        if new:
            new.parent = old.parent

    def remove(self, value):
        node = self.search(value)
        if node:
            if node.parent is None:
                self.root = None
            else:
                if node.left is None and node.right is None:
                    self.resign_node(node, None)
                elif node.left is None:
                    self.resign_node(node, node.right)
                elif node.right is None:
                    self.resign_node(node, node.left)
                else:
                    temp_value = self.get_max(node.left)
                    self.remove(temp_value)
                    node.value = temp_value

    def postorder(self, node):
        if node:
            self.postorder(node.right)
            print(node.value)
            self.postorder(node.left)


if __name__ == '__main__':
    tree = BinarySearch()
    tree.insert(22, 6, 8, 4, 7, 13, 12, 9)
    tree.postorder(tree.root)
    node = tree.search(8)
    if node:
        print("This node value is {}, parent is {}".format(node.value, node.parent))
    node = tree.search(1)
    tree.remove(7)
    tree.search(7)
    tree.postorder(tree.root)
    tree.get_max(tree.root)
