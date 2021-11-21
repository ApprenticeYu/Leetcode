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
	ListNode* remove_list(ListNode* head, int value)
	{
		ListNode* dummy = new ListNode();
		dummy->value = 0;
		dummy->next = head;
		ListNode* temp = dummy;
		while (temp->next != nullptr)
		{
			if (temp->next->value == value)
			{
				temp->next = temp->next->next;
			}
			else
			{
				temp = temp->next;
			}
		}
		return dummy->next;
	}
};