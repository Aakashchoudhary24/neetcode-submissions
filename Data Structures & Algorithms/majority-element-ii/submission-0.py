class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # building the dictionary
        count = {}
        for n in nums :
            count[n] = count.get(n, 0) + 1

        output = []
        for key, value in count.items() : 
            if value > len(nums)/3 : 
                output.append(key)
        
        return output