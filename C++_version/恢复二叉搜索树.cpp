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
	void recover_BST(TreeNode* root)
	{
		TreeNode* x = nullptr;
		TreeNode* y = nullptr;
		TreeNode* pred = nullptr;
		TreeNode* predecessor = nullptr;
		while (root)
		{
			if (root->left)
			{
				predecessor = root->left;
				while (predecessor->right && predecessor->right != root)
				{
					predecessor = predecessor->right;
				}
				if (predecessor->right == nullptr)
				{
					predecessor->right = root;
					root = root->left;
				}
				else
				{
					if (pred != nullptr && root->value < pred->value)
					{
						y = root;
						if (x == nullptr)
						{
							x = pred;
						}
					}
					pred = root;
					predecessor->right = nullptr;
					root = root->right;
				}
			}
			else
			{
				if (pred != nullptr && root->value < pred->value)
				{
					y = root;
					if (x == nullptr)
					{
						x = pred;
					}
				}
				pred = root;
				root = root->right;
			}
		}
		swap(x->value, y->value);
	}
};