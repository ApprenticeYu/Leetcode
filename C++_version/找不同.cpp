#include<iostream>
using namespace std;

class Solution
{
public:
	char find_diff(string s, string t)
	{
		int ret = 0;
		for (char ch : s)
		{
			ret ^= ch;
		}
		for (char ch : t)
		{
			ret ^= ch;
		}
		return ret;
	}
};