#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution
{
public:
	bool word_seperate(string s, vector<string>& words)
	{
		auto word_set = unordered_set <string> ();
		for (auto word : words)
		{
			word_set.insert(word);
		}
		auto dp = vector<bool>(s.size() + 1);
		dp[0] = true;
		for (int i = 1; i <= s.size(); i++)
		{
			for (int j = 0; j < i; j++)
			{
				if (dp[j] && word_set.find(s.substr(j, i - j)) != word_set.end())
				{
					dp[i] = true;
					break;
				}
			}
		}
		return dp[s.size()];
	}
};