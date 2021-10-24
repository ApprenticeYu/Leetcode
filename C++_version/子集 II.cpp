#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution
{
public:
	vector<int> t;
	vector<vector<int>> ans;

	void dfs(bool choose, int cur, vector<int>& nums)
	{
		if (cur == nums.size())
		{
			ans.push_back(t);
			return;
		}
		dfs(false, cur + 1, nums);
		if (!choose && cur > 0 && nums[cur] == nums[cur - 1])
		{
			return;
		}
		t.push_back(nums[cur]);
		dfs(true, cur + 1, nums);
		t.pop_back();
	}


	vector<vector<int>> sub_array(vector<int>& nums)
	{
		sort(nums.begin(), nums.end());
		dfs(false, 0, nums);
		return ans;
	}
};