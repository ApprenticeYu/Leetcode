#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	bool IS(string& s1, string& s2, string& s3)
	{
		auto f = vector<int> (s2.size() + 1, false);
		int m = s1.size();
		int n = s2.size();
		int k = s3.size();
		if (m + n != k)
		{
			return false;
		}
		f[0] = true;
		for (int i = 0; i <= m; i++)
		{
			for (int j = 0; j <= n; j++)
			{
				int p = i + j - 1;
				if (i > 0)
				{
					f[j] &= (s1[i - 1] == s3[p]);
				}
				if (j > 0)
				{
					f[j] |= (f[j - 1] && (s2[j - 1] == s3[p]));
				}
			}
		}
		return f[m];
	}
};