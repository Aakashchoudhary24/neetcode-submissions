class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # created the dictionary
        mydict = {}
        for i in nums : 
            if i in mydict : 
                mydict[i] +=1
            else : 
                mydict[i] = 1

        sortedpairs  = []
        for key, value in mydict.items() : 
            sortedpairs.append((value, key))
        
        sortedpairs.sort(reverse=True)

        output = []
        for i in range(k) : 
            output.append(sortedpairs[i][1])
        
        return output 