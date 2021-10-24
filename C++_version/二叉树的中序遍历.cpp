#include<iostream>
#include<vector>
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
	void dfs(TreeNode* root, vector<int>& nums)
	{
		if (root == nullptr)
		{
			return;
		}
		dfs(root->left, nums);
		nums.push_back(root->value);
		dfs(root->right, nums);
	}

	vector<int> medium(TreeNode* root)
	{
		vector<int> ans;
		dfs(root, ans);
		return ans;
	}
};