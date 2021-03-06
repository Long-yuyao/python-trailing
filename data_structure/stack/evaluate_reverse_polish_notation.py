"""
input ["2", "1", "+", "3", "*"]
output 9
explanation: ((2 + 1) * 3) = 9
"""


class Solution(object):
    def evalRPN(self, tokens) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        expression = []
        # maps: '/': lambda a,b: a/b
        for i in range(len(tokens)):
            if tokens[i] == '/':
                x = int(expression[-2]) / int(expression[-1])
                expression.pop()
                expression.pop()
                expression.append(x)
            elif tokens[i] == '*':
                x = int(expression[-2]) * int(expression[-1])
                expression.pop()
                expression.pop()
                expression.append(x)
            elif tokens[i] == '+':
                x = int(expression[-2]) + int(expression[-1])
                expression.pop()
                expression.pop()
                expression.append(x)
            elif tokens[i] == '-':
                x = int(expression[-2]) - int(expression[-1])
                expression.pop()
                expression.pop()
                expression.append(x)
            else:
                expression.append(tokens[i])
        return int(expression[0])


def solution_test():
    examples = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
    st = [22]
    answer = Solution()
    for i in range(len(examples)):
        assert answer.evalRPN(examples[i]) == st[i]


if __name__ == '__main__':
    solution_test()
