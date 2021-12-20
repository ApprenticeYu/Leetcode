#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	void reverse_string(vector<char>& s)
	{
		int n = s.size();
		for (int left = 0, right = n - 1; left < right; left++, right--)
		{
			swap(s[left], s[right]);
		}
	}
};