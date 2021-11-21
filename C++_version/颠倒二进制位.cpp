#include<iostream>
using namespace std;

class Solution
{
public:
	uint32_t reverse_bit(uint32_t n)
	{
		uint32_t res = 0;
		for (int i = 0; i < 32 && n > 0; i++)
		{
			res |= (n & 1) << (32 - i);
			n >>= 1;
		}
		return res;
	}
};