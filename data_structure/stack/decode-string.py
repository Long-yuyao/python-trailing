"""
input:s = "3[a]2[bc]"
output:"aaabcbc"
"""


# class Solution:
#     def decodestring(self, s: str) -> str:
#         """
#
#         :type s: object
#         """
#         list_s = [[1, ""]]
#         for letter in s:
#             if letter.isdigit():
#                 if len(list_s[-1]) == 1:
#                     list_s[-1][0] = int(letter) + list_s[-1][0] * 10
#                 else:
#                     list_s.append([int(letter)])
#             elif letter == '[':
#                 list_s[-1].append("")
#             elif letter == ']':
#                 a = (list_s[-1][0]) * list_s[-1][1]
#                 list_s.pop()
#                 k = list_s[-1][1] + a
#                 list_s[-1].pop()
#                 list_s[-1].append(k)
#             else:
#                 k = list_s[-1][1] + letter
#                 list_s[-1].pop()
#                 list_s[-1].append(k)
#         return list_s[0][1]
class Solution:
    def decodestring(self, s: str) -> str:
        stack = []
        for a in s:
            if a == ']':
                word = ''
                while stack[-1] != '[':
                    word = stack[-1] + word
                    stack.pop()
                stack.pop()
                word = int(stack[-1]) * word
                stack.pop()
                stack.append(word)
            elif stack and a.isnumeric() and stack[-1].isnumeric():
                stack[-1] = stack[-1] + a
            else:
                stack.append(a)
        word = ''
        for s in stack:
            word = word + s
        return word


if __name__ == '__main__':
    assert Solution().decodestring("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodestring("abc3[cd]xyz") == "abccdcdcdxyz"
    assert Solution().decodestring("3[a2[c]]") == "accaccacc"
    assert Solution().decodestring("adbcdf") == "adbcdf"
    assert Solution().decodestring("100[leetcode]") == 100 * "leetcode"
