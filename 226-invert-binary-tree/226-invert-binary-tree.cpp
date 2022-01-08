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
    typedef TreeNode* T;
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return root;
        
        T left = invertTree(root->left);
        T right = invertTree(root->right);
        
        root->right = left;
        root->left = right;
        return root;
        
    }
};