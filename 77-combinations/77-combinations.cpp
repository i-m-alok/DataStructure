class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> s;
        
        findComb(n, k, 1, ans, s);
        return ans;
    }
    
    void findComb(int n, int k, int current, vector<vector<int>>& ans, vector<int>& s ){
        
        if(current==n+1 or s.size()==k){
            if(s.size()==k){
                ans.push_back(s);   
            }
            return;
        }
        
        s.push_back(current);
        findComb(n, k, current+1, ans, s);
        s.pop_back();
        findComb(n, k, current+1, ans, s);
    }
};