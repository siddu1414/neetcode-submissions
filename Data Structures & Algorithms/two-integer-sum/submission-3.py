class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dictionary to store {number: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is already in our dictionary, we found our pair!
            if complement in seen:
                return [seen[complement], i]
                
            # Otherwise, store the current number and its index for future lookups
            seen[num] = i
            
        return []      
        