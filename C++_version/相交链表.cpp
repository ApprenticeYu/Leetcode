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
	ListNode* mix_list(ListNode* head1, ListNode* head2)
	{
		if (!head1 or !head2)
		{
			return nullptr;
		}
		ListNode* p1 = head1;
		ListNode* p2 = head2;
		while (p1 != p2)
		{
			p1 = p1 == nullptr ? head2 : p1->next;
			p2 = p2 == nullptr ? head1 : p2->next;
		}
		return p1;
	}
};