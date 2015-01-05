class Solution:
    """
    Calculate the a^n % b where a, b and n are all 32bit integers.
    @param a, b, n: 32bit integers
    @return: An integer

    >>> Solution().fastPower(3, 7, 5)
    5

    >>> Solution().fastPower(31, 1, 0)
    0
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            if b == 1:
                return 0
            else:
                return 1
        z = self.fastPower(a, b, n // 2)
        if n % 2 == 0:
            result = (z * z) % b
        else:
            result = (a * z * z) % b
        return result
