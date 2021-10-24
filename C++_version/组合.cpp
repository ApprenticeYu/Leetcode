#include<iostream>
#include<vector>
using namespace std;

class Solution
{
	vector<vector<int>> ans;
	vector<int> temp;
public:
	void dfs(int carry, int n, int k)
	{
		if (temp.size() + (n - carry + 1) < k)
		{
			return;
		}
		if (temp.size() == k)
		{
			ans.push_back(temp);
			return;
		}
		temp.push_back(carry);
		dfs(carry + 1, n, k);
		temp.pop_back();
		dfs(carry + 1, n, k);
	}

	vector<vector<int>> combine(int n, int k)
	{
		dfs(1, n, k);
		return ans;
	}
};
