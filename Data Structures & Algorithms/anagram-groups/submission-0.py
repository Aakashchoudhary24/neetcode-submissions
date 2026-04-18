class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs : 
            sortedKey = ''.join(sorted(s))

            if sortedKey not in result :
                result[sortedKey] = []
            
            result[sortedKey].append(s)

        return list(result.values())