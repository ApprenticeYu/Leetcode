#include<iostream>
#include<queue>
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
	vector<vector<int>> level_order(TreeNode* root)
	{
		vector<vector<int>> ret;
		if (!root)
		{
			return ret;
		}
		queue<TreeNode*> q;
		q.push(root);
		while (!q.empty())
		{
			int count = q.size();
			ret.push_back(vector<int>());
			for (int i = 1; i <= count; i++)
			{
				TreeNode* node = q.front();
				q.pop();
				ret.back().push_back(node->value);
				if (node->left)
				{
					q.push(node->left);
				}
				if (node->right)
				{
					q.push(node->right);
				}
			}
		}
		return ret;
	}
};