#include<iostream>
using namespace std;

struct status
{
	int selected;
	int nonselected;
};

struct TreeNode
{
	int value;
	TreeNode* left;
	TreeNode* right;
};

class Solution
{
public:
	status dfs(TreeNode* root)
	{
		if (!root)
		{
			return { 0,0 };
		}
		status l = dfs(root->left);
		status r = dfs(root->right);
		int select = root->value + l.nonselected + r.nonselected;
		int non = max(l.nonselected, l.selected) + max(r.nonselected, r.selected);
		return { select,non };
	}

	int result(TreeNode* root)
	{
		auto ans = dfs(root);
		return max(ans.nonselected, ans.selected);
	}
};