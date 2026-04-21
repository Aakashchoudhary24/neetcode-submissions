class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        answer = 1
        for n in nums : 
            if n == answer : 
                answer += 1
        
        return answer