class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i, num in enumerate(nums):
            array.append([num, i])
        
        array.sort()
        left, right = 0, len(nums) - 1

        while left < right : 
            sum = array[left][0] + array[right][0]

            if sum == target : 
                return [min(array[left][1],array[right][1]), max(array[left][1],array[right][1])]

            elif sum < target : 
                left += 1
            
            elif sum > target : 
                right -= 1
            
        return []