class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # sort keys by their frequency, descending
        # understanding -> lambda arguments : expression
        # basically count[x] are the keys and lambda function is returning them
        # then they are sorted
        sorted_keys = sorted(count, key=lambda x: count[x], reverse=True)
        
        return sorted_keys[:k]  # taking only the first k keys 