#include<iostream>
using namespace std;

class Solution
{
public:
	int first_false_version(int n)
	{
		int left = 1;
		int right = n;
		while (left < right)
		{
			int mid = left + (right - left) / 2;
			if (isBadVersion(mid))
			{
				right = mid;
			}
			else
			{
				left = mid + 1;
			}
		}
		return left;
	}
};