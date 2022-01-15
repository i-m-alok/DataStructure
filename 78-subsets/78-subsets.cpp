class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> subset;
        
        findSubsets(nums, 0, ans, subset); 
        return ans;
    }
    
    void findSubsets(vector<int>& nums, int i, vector<vector<int>>& ans, vector<int>& subset){
        if(i==nums.size()){
            ans.push_back(subset);
            return;
        }
        
        subset.push_back(nums[i]);
        findSubsets(nums, i+1, ans, subset);
        subset.pop_back();
        findSubsets(nums, i+1, ans, subset);
    }
};