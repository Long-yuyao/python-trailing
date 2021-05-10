class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def reverse_list(start: Node) -> Node:
    end = None
    while start:
        p = Node(start.value)
        p.next = end
        end = p
        start = start.next
    return end


if __name__ == '__main__':
    rl = Node(1)
    rl.next = Node(3)
    rl.next.next = Node(8)
    rl.next.next.next = Node(9)
    rl.next.next.next.next = Node(0)
    l = reverse_list(rl)
    while l:
        print(l.value)
        l = l.next
