class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Edge case: If the input list is empty, return an empty string
        if not strs:
            return ""
        
        # Start by assuming the first word is the entire common prefix
        prefix = strs[0]
        
        # Compare our prefix with every other word in the list
        for word in strs[1:]:
            # Keep cutting letters off the end of the prefix 
            # until the current word starts with it
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                
                # If the prefix becomes completely empty, there is no common prefix
                if not prefix:
                    return ""
                    
        return prefix
