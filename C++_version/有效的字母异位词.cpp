#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	bool valid_word(string s, string t)
	{
		if (s.size() != t.size())
		{
			return false;
		}
		vector<int>table(26, 0);
		for (auto& s1 : s)
		{
			table[s1 - 'a']++;
		}
		for (auto& t1 : t)
		{
			table[t1 - 'a']--;
			if (table[t1 - 'a'] < 0)
			{
				return false;
			}
		}
		return true;
	}
};