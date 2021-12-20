#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	bool sequence(vector<int>& nums)
	{
		int n = nums.size();
		if (n < 3)
		{
			return false;
		}
		int small = INT_MAX;
		int mid = INT_MAX;
		for (auto num : nums)
		{
			if (num < small)
			{
				small = num;
			}
			else if (num < mid)
			{
				mid = num;
			}
			else if(num > mid)
			{
				return true;
			}
		}
		return false;
	}
};