#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int search_position(vector<int>& nums, int target)
	{
		int n = nums.size();
		int left = 0;
		int right = n - 1;
		int ans = n;
		while (left <= right)
		{
			int mid = left + ((right - left) >> 1);
			if (nums[mid] >= target)
			{
				right = mid - 1;
				ans = mid;
			}
			else
			{
				left = mid + 1;
			}
		}
		return ans;
	}
};

int main()
{
	Solution result;
	vector<int> nums = {1, 3, 5, 6};
	cout << result.search_position(nums, 2) << endl;
	system("pause");
	return 0;
}