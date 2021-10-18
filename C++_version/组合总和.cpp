#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	void combine_sum(vector<int>& candidates, int target, vector<vector<int>>& ans, vector<int>& combine, int index)
	{
		if (index == candidates.size())
		{
			return;
		}
		if (target == 0)
		{
			ans.emplace_back(combine);
			return;
		}
		combine_sum(candidates, target, ans, combine, index + 1);
		if (target - candidates[index] >= 0)
		{
			combine.emplace_back(candidates[index]);
			combine_sum(candidates, target - candidates[index], ans, combine, index);
			combine.pop_back();
		}
	}

	vector<vector<int>>result(vector<int>& candidates, int target)
	{
		vector<vector<int>>ans;
		vector<int> combine;
		combine_sum(candidates, target, ans, combine, 0);
		return ans;
	}
};