class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect

        n = len(nums)
        
        unique_nums = sorted(list(set(nums)))
        
        min_ops = n 
        
  
        for i in range(len(unique_nums)):
            left_bound = unique_nums[i]
            right_bound = left_bound + n - 1
            
          
            idx = bisect.bisect_right(unique_nums, right_bound)
            
           
            valid_count = idx - i
            
            
            current_ops = n - valid_count
            min_ops = min(min_ops, current_ops)
            
        return min_ops
