#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int remove_number(vector<int>& nums, int target)
	{
		if (nums.size() == 0)
		{
			return 0;
		}
		int left = 0;
		int right = nums.size();
		while (left < right)
		{
			if (nums[left] == target)
			{
				nums[left] = nums[right - 1];
				right--;
			}
			else
			{
				left++;
			}
		}
		return left;

	}
};

int main()
{
	vector<int> nums;
	nums.push_back(3);
	nums.push_back(2);
	nums.push_back(2);
	nums.push_back(3);
	Solution result;
	cout << result.remove_number(nums, 3) << endl;
	system("pause");
	return 0;
}