#include<iostream>
using namespace std;

struct Node
{
	int value;
	Node* left;
	Node* right;
	Node* next;
};

class Solution
{
public:
	void handle(Node*& last, Node*& begin, Node*& p)
	{
		if (last)
		{
			last->next = p;
		}
		if (!begin)
		{
			begin = p;
		}
		last = p;
	}

	Node* next_right(Node* root)
	{
		if (!root)
		{
			return root;
		}
		Node* node = root;
		while (node)
		{
			Node* last = nullptr;
			Node* begin = nullptr;
			for (Node* p = node; p != nullptr; p = p->next)
			{
				if (p->left)
				{
					handle(last, begin, p->left);
				}
				if (p->right)
				{
					handle(last, begin, p->right);
				}
			}
			node = begin;
		}
		return root
	}
};

