#include<iostream>
#include<vector>
using namespace std;


class Solution
{
	int find_duplicate_num(vector<int>& nums)
	{
		int slow = 0;
		int fast = 0;
		do
		{
			slow = nums[slow];
			fast = nums[nums[fast]];
		} while (slow != fast);
		slow = 0;
		while (slow != fast)
		{
			slow = nums[slow];
			fast = nums[fast];
		}
		return slow;
	}
};
