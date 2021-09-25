#include<iostream>
using namespace std;

struct ListNode
{
	int num;
	ListNode* next;

};

class solution
{

public:
	ListNode* Sum(ListNode* l1, ListNode* l2)
	{

		ListNode* begin = nullptr;
		ListNode* last = nullptr;
		int carry = 0;
		while (l1 || l2)
		{
			int num1 = l1 ? l1->num : 0;
			int num2 = l2 ? l2->num : 0;
			int S = num1 + num2 + carry;

			if (!begin)
			{
				begin = last = new ListNode();
				begin->num = S % 10;

			}
			else
			{
				last->next = new ListNode();
				last->next->num = S % 10;
				last = last->next;

			}
			carry = S / 10;
			if (l1)
			{

				l1 = l1->next;
			}
			if (l2)
			{

				l2 = l2->next;
			}
		}
		if (carry > 0)
		{
			last->next = new ListNode();
			last->next->num = carry;
			last = last->next;
		}
		return begin;
	}
};

