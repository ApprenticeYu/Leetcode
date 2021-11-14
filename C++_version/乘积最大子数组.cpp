#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int max_array(vector<int>& nums)
	{
		int ans = nums[0];
		int max_num = nums[0];
		int min_num = nums[0];
		for (int i = 1; i < nums.size(); i++)
		{
			max_num = max(max_num * nums[i], max(min_num * nums[i], nums[i]));
			min_num = min(max_num * nums[i], max(min_num * nums[i], nums[i]));
			ans = max(ans, max_num);
		}
		return ans;
	}
};

void main()
{
	vector<int>nums = { 2,3,-2,4 };
	Solution ans;
	cout << ans.max_array(nums) << endl;
	system("pause");
}