#include<iostream>
using namespace std;

class Solution
{
public:
	bool is_valid_sequence(string s)
	{
		int length = s.length();
		int i = 0;
		int slots = 1;
		while (i < length)
		{
			if (slots == 0)
			{
				return false;
			}
			else if (s[i] == ',')
			{
				i++;
			}
			else if (s[i] == '#')
			{
				slots--;
				i++;
			}
			else
			{
				while (i < length && s[i] != ',')
				{
					i++;
				}
				slots++;
			}
		}
		return slots == 0;
	}
};
