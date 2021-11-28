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
	bool exits(TreeNode* root, int level, int mid)
	{
		int bits = 1 << (level - 1);
		TreeNode* node = root;
		while (node && bits > 0)
		{
			if (!(mid & bits))
			{
				node = node->left;
			}
			else
			{
				node = node->right;
			}
			bits >>= 1;
		}
		return node != nullptr;
	}

	int numbers_of_node(TreeNode* root)
	{
		if (!root)
		{
			return 0;
		}
		int level = 0;
		TreeNode* node = root;
		while (node->left)
		{
			++level;
			node = node->left;
		}
		int low = 1 << level;
		int high = (1 << (level + 1)) - 1;
		while (low < high)
		{
			int mid = low + (high - low + 1) / 2;
			if (exits(root, level, mid))
			{
				low = mid;
			}
			else
			{
				high = mid - 1;
			}
		}
		return low;
	}
};