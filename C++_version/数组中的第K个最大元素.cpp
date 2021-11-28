#include<iostream>
#include<vector>
using namespace std;

int quick_sort_core(vector<int>& nums, int left, int right)
{
	int i = left - 1;
	for (int j = 0; j < right; j++)
	{
		if (nums[j] <= nums[right])
		{
			swap(nums[++i], nums[j]);
		}
	}
	swap(nums[i + 1], nums[right]);
	int result = i + 1;
	return result;
}

int quick_sort(vector<int>& nums, int left, int right)
{
	int i = rand() % (right - left + 1) + 1;
	swap(nums[i], nums[right]);
	return quick_sort_core(nums, left, right);
}

int k_max(vector<int>& nums, int left, int right, int index)
{
	int i = quick_sort(nums, left, right);
	if (i == index)
	{
		return nums[i];
	}
	else
	{
		return i < index ? k_max(nums, i + 1, right, index) : k_max(nums,left, i - 1, index);
	}
}

int k_max_core(vector<int>& nums, int k)
{
	srand(time(0));
	int n = nums.size();
	return k_max(nums, 0, n - 1, n - k);
}