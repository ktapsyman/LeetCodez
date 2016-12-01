class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1

        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        rest = abs_dividend
        ret = 0
        while rest >= abs_divisor:
            sub = abs_divisor
            power = 1
            while rest >= sub:
                sub <<= 1
                power <<= 1
            sub >>= 1
            power >>= 1
            rest -= sub
            ret += power

        if (divisor < 0) ^ (dividend < 0):
            ret = -ret

        return min(max(ret, MIN_INT), MAX_INT)

if __name__ == "__main__":
	res = Solution()
	print(res.divide(333, 7))
