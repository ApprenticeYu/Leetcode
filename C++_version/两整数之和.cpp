#include<iostream>
using namespace std;

class Solution
{
public:
	int sum_of_two(int num1, int num2)
	{
		while (num2 != 0)
		{
			unsigned int carry = (unsigned int)(num1 & num2) << 1;
			num1 = num1 ^ num2;
			num2 = carry;
		}
		return num1;
	}
};