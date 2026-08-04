class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
     
        # Base check: length must be a multiple of 3
        if len(s) % 3 != 0:
            return False
            
        stack = []
        
        for char in s:
            stack.append(char)
            # Check if the last three elements form "abc"
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                # Remove "abc" from the stack
                stack.pop()
                stack.pop()
                stack.pop()
                
        # If stack is empty, all patterns were validly cancelled out
        return len(stack) == 0
