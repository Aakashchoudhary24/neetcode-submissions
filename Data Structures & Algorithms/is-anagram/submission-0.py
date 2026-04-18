class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 7 minutes -> couldn't solve
        # maybe add to a set
        # maybe add to a dictionary and compare the first element of the pair
        if len(s) != len(t) : 
            return False
        
        return sorted(s) == sorted(t)