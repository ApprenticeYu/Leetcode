#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	vector<vector<int>> ans;
	vector<int> temp;
	void dfs(int cur, vector<int>& nums)
	{
		if (cur == temp.size())
		{
			ans.push_back(temp);
			return;
		}
		temp.push_back(nums[cur]);
		dfs(cur + 1, nums);
		temp.pop_back();
		dfs(cur + 1, nums);
	}

	vector<vector<int>> sub_(vector<int>& nums)
	{
		dfs(0, nums);
		return ans;
	}
};