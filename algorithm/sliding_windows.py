"""
https://leetcode-cn.com/problems/sliding-window-maximum/
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值

suggestion: heap/merge sort

"""


def slide_windows(nums: list, k: int) -> list:



if __name__ == '__main__':
    assert slide_windows([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert slide_windows([1, -1], 1) == [1, -1]
