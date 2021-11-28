#include<iostream>
#include<unordered_map>
using namespace std;

class Solution
{
public:
	bool is_isomorphic(string s, string t)
	{
		unordered_map<char, char> s2t;
		unordered_map<char, char> t2s;
		int n = s.length();
		for (int i = 0; i < n; i++)
		{
			char s1 = s[i];
			char t1 = t[i];
			if ((s2t.count(s1) && s2t[s1] != t1) || (t2s.count(t1) && t2s[t1] != s1))
			{
				return false;
			}
			s2t[s1] = t1;
			t2s[t1] = s1;
		}
		return true;
	}
};