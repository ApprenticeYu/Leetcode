#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution
{
public:
	vector<string> summary_ranges(vector<int>& nums)
	{
		int n = nums.size();
		int i = 0;
		vector<string>res;
		while (i < n)
		{
			int low = i;
			++i;
			while (i < n && nums[i] == nums[i - 1] + 1)
			{
				++i;
			}
			int high = i - 1;
			string stack = to_string(nums[low]);
			if (low < high)
			{
				stack.append("->");
				stack.append(to_string(nums[high]));
			}
			res.push_back(stack);
		}
		return res;
	}
};