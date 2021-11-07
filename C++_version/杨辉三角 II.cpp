#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	vector<int> tringle2(int rows)
	{
		vector<int> ans(rows + 1);
		ans[0] = 1;
		for (int i = 1; i <= rows; i++)
		{
			ans[i] = 1LL * ans[i - 1] * (rows - i + 1) / i;
		}
		return ans;
	}
};