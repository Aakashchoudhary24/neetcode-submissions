class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [1,1,2,3,5,2,4,1]
        # remove all 1 in-place
        # [2,3,5,2,4]
        # return the length of the new array
        # how to remove in-place?
        # set a var k 
        k = 0

        for i in range(len(nums)) :
            if nums[i] != val : 
                nums[k] = nums[i]
                k += 1
            
        return k
        
        