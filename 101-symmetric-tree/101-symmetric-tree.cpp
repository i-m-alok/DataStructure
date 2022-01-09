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
    typedef TreeNode*T;
    bool isSymmetric(TreeNode* root) {
        if(!root){
            return false;
        }
        return findSymmetric(root->left, root->right);
    }
    
    bool findSymmetric(T root1, T root2){
        if((!root1 && root2)||(root1 && !root2)){
            return false;
        }
        if(!root1 && !root2){
            return true;
        }
        if(root1->val != root2->val){
            return false;
        }
        
        bool left = findSymmetric(root1->left, root2->right);
        bool right = findSymmetric(root1->right, root2->left);
        
        return left&&right;
    }
};