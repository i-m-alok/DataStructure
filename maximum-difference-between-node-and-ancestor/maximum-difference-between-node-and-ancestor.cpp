/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans=0;
    int maxAncestorDiff(TreeNode* root) {
        dfs(root);
        return ans; 
    }
    
    pair<int, int> dfs(TreeNode* root){
        if(!root){
            return {INT_MAX, INT_MIN};
        }
        auto [lMin, lMax] = dfs(root->left);
        auto [rMin, rMax] = dfs(root->right);
        int cMin = min({root->val, lMin, rMin});
        int cMax = max({root->val, lMax, rMax});
        ans = max({ans, (root->val)-cMin, cMax-(root->val)});
        
        return {cMin, cMax};
    }
};