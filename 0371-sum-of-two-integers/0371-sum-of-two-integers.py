class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a