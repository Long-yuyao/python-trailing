"""
1. essentially complete
2. parental dominance
eg: 10
   / \
  5   7
 / | /
4  2 1
"""


class Heap:
    def __init__(self, l):
        self.heap = l

    def create_bottom_up(self):
        n = int(len(self.heap)/2)
        for i in range(n):
            k = n-i
            v = self.heap[k-1]
            flag = False
            while 2*k <= len(self.heap) and not flag:
                j = 2*k
                if j < len(self.heap):
                    if self.heap[j-1] < self.heap[j]:
                        j = j+1
                if v < self.heap[j-1]:
                    self.heap[k-1] = self.heap[j-1]
                    k = j
                else:
                    flag = True
            self.heap[k-1] = v
        return self.heap



