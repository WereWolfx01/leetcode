/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isValid(struct TreeNode* current, struct TreeNode** prev){
    if(!current) return true;
    
    if(!isValid(current->left, prev)) return false;
    if(*prev && current->val <= (*prev)->val) return false;
    *prev = current;
    return (isValid(current->right, prev));
    
}


bool isValidBST(struct TreeNode* root){
    struct TreeNode *prev = NULL;
    return isValid(root, &prev);
}
