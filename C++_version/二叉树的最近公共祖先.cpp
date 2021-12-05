#include<iostream>
#include<unordered_map>
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
	unordered_map<int, TreeNode*> fa;
	unordered_map<int, bool> vis;
	void dfs(TreeNode* root)
	{
		if (root->left != nullptr)
		{
			fa[root->left->value] = root;
			dfs(root->left);
		}
		if (root->right != nullptr)
		{
			fa[root->right->value] = root;
			dfs(root->right);
		}
	}

	TreeNode* nearest_ancestor(TreeNode* root,TreeNode* p,TreeNode* q)
	{
		fa[root->value] = nullptr;
		dfs(root);
		while (p)
		{
			vis[p->value] = true;
			p = fa[p->value];
		}
		while (q)
		{
			if (vis[q->value]) return q;
			q = fa[q->value];
		}
		return nullptr;
	}
};