#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int delete_duplicate(vector<int>& nums)
	{
		if (nums.size() <= 2)
		{
			return nums.size();
		}
		int slow = 2;
		int fast = 2;
		int n = nums.size();
		while (fast < n)
		{
			if (nums[fast] != nums[slow - 2])
			{
				nums[slow] = nums[fast];
				++slow;
			}
			++fast;
		}
		return slow;
	}
};

int main()
{
	vector<int> nums = { 1,1,1,2,2,3 };
	Solution result;
	cout << result.delete_duplicate(nums) << endl;
	system("pause");
	return 0;
}