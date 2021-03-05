import math


class Solution(object):

    def reverse(self, num: int) -> int:
        """
        实现有符号整数翻转
        :param num: 整型
        :return: 整型
        """
        num_r, rev = num, 0

        num_r = math.floor(math.fabs(num_r))
        while num_r != 0:
            pop = num_r % 10
            if (rev > math.pow(2, 31) // 10) or (rev == math.pow(2, 31) // 10 and pop > 7):
                print('rev=%d   pop=%d' % (rev, pop))
                return 0
            if (num < 0) and (rev > math.pow(2, 31) // 10) or (rev == math.pow(2, 31) // 10 and pop > 8):
                print('rev=%d   pop=%d' % (rev, pop))
                return 0
            rev = rev * 10 + pop
            num_r //= 10

        return rev if num > 0 else -rev


if __name__ == '__main__':
    revs = Solution()
    print(revs.reverse(214748364))
