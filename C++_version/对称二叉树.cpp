#include<iostream>
using namespace std;

struct TreeNode
{
	int value;
	TreeNode* left;
	TreeNode* right;
};

class Solution
{
public:
	bool check(TreeNode* root1, TreeNode* root2)
	{
		if (!root1 && !root2)
		{
			return true;
		}
		if (!root1 || !root2)
		{
			return false;
		}
		return (root1->value == root2->value) && check(root1->left, root2->right) && check(root1->right, root2->left);
	}

	bool is_symmetric(TreeNode* root)
	{
		return check(root, root);
	}
};