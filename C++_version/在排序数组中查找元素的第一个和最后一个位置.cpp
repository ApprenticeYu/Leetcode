#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int get_position(vector<int>& nums, int target, bool sign)
	{
		int left = (int)nums.size();
		int right = (int)nums.size() - 1;
		int ans = (int)nums.size();
		while (left <= right)
		{
			int middle = (left + right) / 2;
			if (nums[middle] > target || (sign && nums[middle] >= target))
			{
				right = middle - 1;
				ans = middle;
			}
			else
			{
				left = middle + 1;
			}
		}
		return ans;
	}

	vector<int> result(vector<int>& nums, int target)
	{
		int left = get_position(nums, target, true);
		int right = get_position(nums, target, false);
		if (left <= right && right < nums.size() && nums[left] == target && nums[right] == target)
		{
			return vector<int>{left, right};
		}
		return vector<int>{-1, -1};
	}
};