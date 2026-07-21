#include <vector>
#include <cmath>

class Solution {
public:
    std::vector<int> findDuplicates(std::vector<int>& nums) {
        std::vector<int> duplicates;
        
        for (int i = 0; i < nums.size(); ++i) {
            // Use the absolute value to get the mapped index
            int targetIndex = std::abs(nums[i]) - 1;
            
            // If the value at targetIndex is negative, it's a duplicate
            if (nums[targetIndex] < 0) {
                duplicates.push_back(targetIndex + 1);
            } else {
                // Otherwise, mark it as visited by negating it
                nums[targetIndex] = -nums[targetIndex];
            }
        }
        
        return duplicates;
    }
};
