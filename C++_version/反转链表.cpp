#include<iostream>
using namespace std;

struct ListNode
{
	int value;
	ListNode* next;
};

class Solution
{
public:
	ListNode* reverse_list(ListNode* head)
	{
		ListNode* pre = nullptr;
		ListNode* cur = head;
		while (cur)
		{
			ListNode* next = cur->next;
			cur->next = pre;
			pre = cur;
			cur = next;
		}
		return pre;
	}
};