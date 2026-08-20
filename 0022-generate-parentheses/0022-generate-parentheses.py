class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
       
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base Case: Valid combination found when string reaches maximum length
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Rule 1: Add an opening parenthesis if we haven't reached the limit 'n'
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Rule 2: Add a closing parenthesis if it matches an existing open one
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result