from list_basic import Node


def copy_list(start: Node) -> Node:
    if not start:
        return None
    else:
        copy = Node(0)
        p = copy
        while start:
            p.next = Node(start.value)
            p = p.next
            start = start.next
        return copy.next


if __name__ == '__main__':
    start = Node(5)
    start.next = Node(0)
    start.next.next = Node(10)
    start.next.next.next = Node(-9)
    copy = copy_list(start)
    while copy:
        print(copy.value)
        copy = copy.next
