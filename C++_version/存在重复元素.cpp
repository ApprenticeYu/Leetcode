#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution
{
public:
	bool is_duplicate(vector<int>& nums)
	{
		unordered_set<int> is_set;
		for (int num : nums)
		{
			if (is_set.find(num) != is_set.end())
			{
				return true;
			}
			is_set.insert(num);
		}
		return false;
	}
};