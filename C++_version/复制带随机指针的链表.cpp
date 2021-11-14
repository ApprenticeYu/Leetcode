#include<iostream>
using namespace std;

struct ListNode
{
	int value;
	ListNode* next;
	ListNode* random;
};

class Solution
{
public:
	ListNode* duplicate_random(ListNode* head)
	{
		if (!head)
		{
			return nullptr;
		}
		for (ListNode* node = head; node != nullptr; node = node->next->next)
		{
			ListNode* new_node = new ListNode();
			new_node->value = node->value;
			new_node->next = node->next;
			node->next = new_node;
		}
		for (ListNode* node = head; node != nullptr; node = node->next->next)
		{
			ListNode* new_node = node->next;
			new_node->random = (node->random != nullptr) ? node->random->next : nullptr;
		}
		ListNode* new_head = head->next;
		for (ListNode* node = head; node != nullptr; node = node->next)
		{
			ListNode* new_node = node->next;
			node->next = new_node->next;
			new_node->next = (new_node->next != nullptr) ? new_node->next->next : nullptr;
		}
		return new_head;
	}
};