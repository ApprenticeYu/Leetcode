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
	ListNode* separate_list(ListNode* head, int x)
	{
		if (head == nullptr)
		{
			return head;
		}
		ListNode* small_head = new ListNode();
		ListNode* small = small_head;
		ListNode* large_head = new ListNode();
		ListNode* large = large_head;
		while (head)
		{
			if (head->value < x)
			{
				small->next = head;
				small = small->next;
			}
			else
			{
				large->next = head;
				large = large->next;
			}
			head = head->next;
		}
		large->next = nullptr;
		small->next = large_head->next;
		return small_head->next;
	}
};
