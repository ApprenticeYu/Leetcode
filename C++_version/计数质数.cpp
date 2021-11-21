#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int compute_primes(int n)
	{
		vector<int>prime(n, 1);
		int count = 0;
		for (int i = 2; i < n; i++)
		{
			if (prime[i])
			{
				count++;
				if ((long long)i * i < n)
				{
					for (int j = i * i; j < n; j += i)
					{
						prime[j] = 0;
					}
				}
			}
		}
		return count;
	}
};