#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	void rotate_array_core(vector<int>& nums, int begin, int end)
	{
		while (begin < end)
		{
			swap(nums[begin], nums[end]);
			++begin;
			--end;
		}
	}

	void ratate_array(vector<int>& nums, int k)
	{
		int n = nums.size();
		int mod = k % n;
		rotate_array_core(nums, 0, n - 1);
		rotate_array_core(nums, 0, mod - 1);
		rotate_array_core(nums, mod, n - 1);
	}
};