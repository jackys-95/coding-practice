class Solution(object):
    def reverse(self, x):
        result = 0
        negative = True if x < 0 else False
        x = abs(x)
        while x != 0:
            result = (result * 10) + (x % 10)
            x //= 10
            if (result > (2**31- 1) or result < -(2**31)):
                return 0
        return result if not negative else -result 

sol = Solution()
