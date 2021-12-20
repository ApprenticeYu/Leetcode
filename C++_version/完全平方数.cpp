#include<iostream>
using namespace std;

class Solution
{
public:
	bool perfect_square_1(int n)
	{
		int x = sqrt(n);
		return x * x == n;
	}

	bool perfect_square_4(int n)
	{
		while (n % 4 == 0)
		{
			n /= 4;
		}
		return n % 8 == 7;
	}

	int perfect_square(int n)
	{
		if (perfect_square_1(n))
		{
			return 1;
		}
		if (perfect_square_4(n))
		{
			return 4;
		}
		for (int i = 1; i * i <= n; i++)
		{
			int x = n - i * i;
			if (perfect_square_1(x))
			{
				return 2;
			}
		}
		return 3;
	}
};

