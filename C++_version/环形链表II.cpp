#include<iostream>
using namespace std;

struct ListNode
{
	int value;
	ListNode* next;
};

class Solution
{
	ListNode* loop_list(ListNode* head)
	{
		if (!head)
		{
			return nullptr;
		}
		ListNode* slow = head;
		ListNode* fast = head;
		while (fast)
		{
			slow = slow->next;
			if (!fast->next)
			{
				return nullptr;
			}
			fast = fast->next->next;
			if (slow == fast)
			{
				ListNode* pre = head;
				while (pre != slow)
				{
					pre = pre->next;
					slow = slow->next;
				}
				return pre;
			}
		}
		return nullptr;
	}
};