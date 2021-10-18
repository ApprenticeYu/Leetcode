#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int max_sub_array(vector<int>& nums)
	{
		int pre = 0;
		int ans = nums[0];
		for (const auto& num : nums)
		{
			pre = max(pre + num, num);
			ans = max(ans, pre);
		}
		return ans;
	}
};

int main()
{
	Solution result;
	vector<int> nums = { -100000 };
	cout << result.max_sub_array(nums) << endl;
	system("pause");
	return 0;
}