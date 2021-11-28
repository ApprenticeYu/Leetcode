#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

class Solution
{
	vector<int> temp;
	vector<vector<int>> ans;

public:
	void dfs(int cur, int n, int k, int sum)
	{
		if (temp.size() + (n - cur + 1) < k || temp.size() > k)
		{
			return;
		}
		if (temp.size() == k && accumulate(temp.begin(), temp.end(), 0) == sum)
		{
			ans.push_back(temp);
			return;
		}
		temp.push_back(cur);
		dfs(cur + 1, n, k, sum);
		temp.pop_back();
		dfs(cur + 1, n, k, sum);
	}

	vector<vector<int>> total(int n, int k)
	{
		dfs(1, 9, k, n);
		return ans;
	}
};