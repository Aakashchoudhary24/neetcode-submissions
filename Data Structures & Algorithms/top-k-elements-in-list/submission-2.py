class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # sort keys by their frequency, descending
        # lambda functions -> lambda arguments : expression
        # sorted(count...) iterates over the keys of the dictionary
        # count[x] -> returns the values for the keys 
        # these values are used for sorting
        # sorted() internally maps the keys to the values iterated
        sorted_keys = sorted(count, key=lambda x: count[x], reverse=True)
        
        return sorted_keys[:k]  # taking only the first k keys 