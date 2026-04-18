class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // ways to solve : brute force loops, hash maps
        // using a hash based container
        // stop the moment an element with second insertion spotted
        // min complexity = O(n) -> gotta look at each element atleast once
        unordered_set<int> seen;
        for (int i : nums){
            if (seen.count(i)){
                return true;
            }
            else {
                seen.insert(i);
            };
        };
        return false;
    };
};