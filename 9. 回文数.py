class Solution(object):
    @staticmethod
    def isPalindrome(x: int) -> bool:
        """
        解法一：将数字转换成字符串，然后逆序后进行比较
        :param x: 整数
        :return: 布尔值
        """
        str_x = str(x)
        if str_x[::-1] == str_x:
            return True
        else:
            return False

    @staticmethod
    def isPalindrome1(x: int) -> bool:
        """
        解法二：
        :param x:
        :return:
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x //= 10
        return reverse_num == x or reverse_num // 10 == x


if __name__ == '__main__':
    panduan = Solution()
    print(panduan.isPalindrome(121))
    print(panduan.isPalindrome1(10))
