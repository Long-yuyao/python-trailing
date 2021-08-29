"""
input ["2", "1", "+", "3", "*"]
output 9
explanation: ((2 + 1) * 3) = 9
"""


# class Solution(object):
#     def evalRPN(self, tokens) -> int:
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
#         expression = []
#         # maps: '/': lambda a,b: a/b
#         for i in range(len(tokens)):
#             if tokens[i] == '/':
#                 x = int(expression[-2]) / int(expression[-1])
#                 expression.pop()
#                 expression.pop()
#                 expression.append(x)
#             elif tokens[i] == '*':
#                 x = int(expression[-2]) * int(expression[-1])
#                 expression.pop()
#                 expression.pop()
#                 expression.append(x)
#             elif tokens[i] == '+':
#                 x = int(expression[-2]) + int(expression[-1])
#                 expression.pop()
#                 expression.pop()
#                 expression.append(x)
#             elif tokens[i] == '-':
#                 x = int(expression[-2]) - int(expression[-1])
#                 expression.pop()
#                 expression.pop()
#                 expression.append(x)
#             else:
#                 expression.append(tokens[i])
#         return int(expression[0])
class Solution:
    def evalRPN(self, tokens: list) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '-':
                store = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(store)
            elif tokens[i] == '+':
                store = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(store)
            elif tokens[i] == '*':
                store = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(store)
            elif tokens[i] == '/':
                store = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(store)
            else:
                stack.append(int(tokens[i]))
        return stack[0]


def solution_test():
    examples = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    answer = Solution()
    print(answer.evalRPN(examples) == 22)


if __name__ == '__main__':
    solution_test()
