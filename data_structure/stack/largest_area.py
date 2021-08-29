"""
input:[2,1,5,6,2,3]
output:10
take place heights with orders
"""


# class Solution:
#     def largestRectangleArea(self, heights: [int]) -> int:
#         n = len(heights)
#         left = [0] * n
#         right = [n] * n
#         stack = []
#         for i in range(n):
#             while stack and heights[i] <= heights[stack[-1]]:
#                 right[stack[-1]] = i
#                 stack.pop()
#             left[i] = stack[-1] + 1 if stack else 0
#             stack.append(i)
#
#         return max(((right[i]-left[i]) * heights[i]) for i in range(n))
#
#
# if __name__ == '__main__':
#     assert Solution().largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]) == 10
class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        stack = []
        l = len(heights)
        left = [0]*l
        right = [l-1]*l
        for i in range(l):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            # left[i] = stack[-1] if stack else 0
            stack.append(i)
        print([(right[i]-left[i])*heights[i] for i in range(len(heights))])
        return max((right[i]-left[i])*heights[i] for i in range(len(heights)))


print (Solution().largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]))
