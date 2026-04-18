class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # add element frequencies to hash table
        # iterate frequencies and return output if freq > n/2
        freq = {}
        for num in nums : 
            if num in freq : 
                freq[num] += 1

            else : 
                freq[num] = 1
        
        for key, value in freq.items() : 
            if value > len(nums)/2 : 
                return key