#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

class Solution
{
public:
	string max_num(vector<int>& nums)
	{
		sort(nums.begin(), nums.end(), [](const int& x, const int& y)
			{
				long x_t = 10;
				long y_t = 10;
				while (x_t <= x)
				{
					x_t *= 10;
				}
				while (y_t <= y)
				{
					y_t *= 10;
				}
				return (y_t * x + y) > (x_t * y + x);
			});
		if (nums[0] == 0)
		{
			return "0";
		}
		string res;
		for (int& num : nums)
		{
			res += to_string(num);
		}
		return res;
	}
};