class Solution(object):
    def largestGoodInteger(self, s): # s -> String
        if "999" in s:
            return "999"
        if "888" in s:
            return "888"
        if "777" in s:
            return "777"
        if "666" in s:
            return "666"
        if "555" in s:
            return "555"
        if "444" in s:
            return "444"
        if "333" in s:
            return "333"
        if "222" in s:
            return "222"
        if "111" in s:
            return "111"
        if "000" in s:
            return "000"
        else:
            return ""