class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hash map technique
        # if diff len -> false
        # two hash maps
        # match frequencies
        # hash maps can be compared in python (order is ignored)

        if len(s) != len(t) : 
            return False
        
        s_count, t_count = {}, {}

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
        return s_count == t_count

        # .get() fetches the value of the key name provided
        # else it returns the default provided, here it is 0