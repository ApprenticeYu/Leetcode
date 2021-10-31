#include<iostream>
#include<queue>
#include<deque>
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
	vector<vector<int>> zig_zag(TreeNode* root)
	{
		vector<vector<int>> ans;
		if (!root)
		{
			return ans;
		}
		queue<TreeNode*> q;
		q.push(root);
		bool left = true;
		while (!q.empty())
		{
			deque<int> d;
			int count = q.size();
			for (int i = 0; i < count; i++)
			{
				TreeNode* temp = q.front();
				q.pop();
				if (left)
				{
					d.push_back(temp->value);
				}
				else
				{
					d.push_front(temp->value);
				}
				if (temp->left)
				{
					q.push(temp->left);
				}
				if (temp->right)
				{
					q.push(temp->right);
				}
			}
			ans.emplace_back(vector<int> {d.begin(), d.end()});
			left = !left;
		}
		return ans;
	}
};