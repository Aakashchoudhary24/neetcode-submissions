class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force approach
        output = []
        for i in range(len(nums)) : 
            new = nums[:i] + nums[i+1:]
            product = 1
            for j in new : 
                product = product * j
            
            output.append(product)
        
        return output