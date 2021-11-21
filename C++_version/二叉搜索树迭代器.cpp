#include<iostream>
#include<stack>
using namespace std;

struct TreeNode
{
	int value;
	TreeNode* left;
	TreeNode* right;
};

class Solution
{
private:
	TreeNode* cur;
	stack<TreeNode*>Tree_stack;
public:
	Solution (TreeNode* root):cur(root) {};
	int get_next()
	{
		while(cur)
		{
			Tree_stack.push(cur);
			cur = cur->left;
		}
		TreeNode* temp = Tree_stack.top();
		Tree_stack.pop();
		int num = temp->value;
		temp = temp->right;
		return num;
	}

	bool has_next()
	{
		return cur || !Tree_stack.empty();
	}

};
