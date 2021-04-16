class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked:
    """
    有⼀个链表，奇数位升序偶数位降序，如何将链表变成升序？
    比如：1 8 3 6 5 4 7 2 9，最后输出1 2 3 4 5 6 7 8 9
    """

    def dec_inc(self, link: Node):
        count = 0
        record_down = None
        tmp2 = record_up = Node(0)
        while link:
            count = count + 1
            if count % 2 == 0:
                tmp = Node(link.value)
                head, link = tmp, link.next
                head.next, record_down = record_down, head
            else:
                tmp = Node(link.value)
                record_up.next, link = tmp, link.next
                record_up = record_up.next

        return self.merge(tmp2.next, record_down)

    def merge(self, link1: Node, link2: Node):
        answer = curl = Node(0)
        while link1 and link2:
            if link1.value <= link2.value:
                curl.next, link1 = link1, link1.next
            else:
                curl.next, link2 = link2, link2.next
            curl = curl.next
        curl.next = link1 if link1 else link2
        return answer.next


if __name__ == '__main__':
    link = Node(1)
    link.next = Node(8)
    link.next.next = Node(5)
    link.next.next.next = Node(4)
    link.next.next.next.next = Node(6)
    link.next.next.next.next.next = Node(2)
    sort = Linked().dec_inc(link)
    while sort:
        print(sort.value)
        sort = sort.next
