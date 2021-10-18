#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution
{
	vector<int> vis;
public:
	void baktrack(vector<int>& nums, vector<vector<int>>& ans, vector<int>& term,int index)
	{
		if (index == nums.size())
		{
			ans.emplace_back(term);
			return;
		}
		for (int i = 0; i < nums.size(); i++)
		{
			if (vis[i] || (i > 0 && nums[i - 1] == nums[i] && !vis[i - 1]))
			{
				continue;
			}
			term.emplace_back(nums[i]);
			vis[i] = 1;
			baktrack(nums, ans, term, index + 1);
			term.pop_back();
			vis[i] = 0;
		}
	}

	vector<vector<int>>full2(vector<int>&nums)
	{
		vector<vector<int>>ans;
		vector<int>term;
		vis.resize(nums.size());
		sort(nums.begin(), nums.end());
		baktrack(nums, ans, term, 0);
		return ans;
	}
};