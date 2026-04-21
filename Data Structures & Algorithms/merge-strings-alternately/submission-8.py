class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ''

        m = len(word1)
        n = len(word2)
        net = word1 + word2

        if m < n : 
            shorter = word1
            longer = word2 
        else : 
            shorter = word2
            longer = word1

        if word1 == '' : 
            return word1
        
        if word2 == '' : 
            return word2

        for i in range(len(shorter)) : 
            new = new + word1[i]
            new = new + word2[i]

        # filling in the remaining words...
        for i in range(len(new) // 2, len(longer)) : 
            new = new + longer[i]
        
        return new