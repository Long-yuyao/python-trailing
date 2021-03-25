"""
time limited
"""


def encode(s):
    l = [int(i) for i in s]
    ll = []
    for i in range(len(l)):
        if i < len(l) - 1 and l[i + 1] == 0 and l[i] in [1, 2]:
            ll.append(int(str(l[i]) + str(l[i + 1])))
            l[i + 1] = -1
        elif l[i] == -1:
            pass
        else:
            ll.append(l[i])
    if 0 in ll:
        return 0
    times = [1] * (len(ll) + 1)
    for i in range(len(ll)):
        if ll[i - 1] == 1 or ll[i - 1] == 2:
            if i > 0 and int(str(ll[i - 1]) + str(ll[i])) <= 26:
                times[i + 1] = times[i] + times[i - 1]
            else:
                times[i + 1] = times[i]
        else:
            times[i + 1] = times[i]
    return times[len(ll)]


if __name__ == '__main__':
    assert encode('7124689') == 3
    assert encode('12') == 2
    assert encode('2101') == 1
    assert encode('1201234') == 3
    assert encode('06') == 0
