/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void preorder(struct TreeNode* root, int* arr, int* returnSize) {
    if (root == NULL) {
        return;
    }
    
     arr[*returnSize] = root->val; 
    (*returnSize)++;

    preorder(root->left, arr, returnSize);
    
    preorder(root->right, arr, returnSize);
}

int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    
    int* result = (int*)malloc(101 * sizeof(int)); 
    
    preorder(root, result, returnSize);
    
    return result;
}