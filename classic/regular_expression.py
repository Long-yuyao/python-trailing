"""
'.': a character
'*':several same characters including(0) before a character
input:s = "aa" p = "a"
output:false

input:s = "aa" p = "a*"
output:Ture

the point is to use correct data structure to keep the result for looking back
"""


class IsMatch:
    def __init__(self, s, p):
        self.s = s
        self.p = p
        self.record = {}
        self.ans = self.match(0, 0)

    def match(self, i, j) -> bool:
        x = '{}{}'.format(i, j)
        if x not in self.record.keys():
            if not self.s[i:]:
                self.record[x] = not self.p[j:]
                if len(self.p[j:]) >= 2:
                    if self.p[j+1] == '*':
                        if len(self.p[j:]) == 2:
                            self.record[x] = True
                        else:
                            self.record[x] = self.match(i, j+2)
            else:
                if not self.p[j:]:
                    self.record[x] = False
                else:
                    flag = self.p[j] in [self.s[i], '.']
                    if len(self.p[j:]) >= 2:
                        if self.p[j + 1] == '*':
                            self.record[x] = self.match(i, j+2) or flag and self.match(i + 1, j + 2) or \
                                             flag and self.match(i + 1, j)
                        else:
                            self.record[x] = flag and self.match(i + 1, j + 1)
                    else:
                        self.record[x] = flag and self.match(i + 1, j + 1)
        return self.record[x]


if __name__ == '__main__':
    s = "aab"
    p = "c*a*b"
    assert IsMatch(s, p).ans is True
    s = "mississippi"
    p = "mis*is*p*."
    assert IsMatch(s, p).ans is False
    s = "aa"
    p = "a*"
    assert IsMatch(s, p).ans is True
    s = 'aa'
    p = 'a'
    assert IsMatch(s, p).ans is False
    s = 'a'
    p = 'ab*'
    assert IsMatch(s, p).ans is True
    s = "bbbba"
    p = ".*a*a"
    assert IsMatch(s, p).ans is True
    s = ''
    p = 'b*b*'
    assert IsMatch(s, p).ans is True



