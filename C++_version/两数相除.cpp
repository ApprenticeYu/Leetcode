#include<iostream>
using namespace std;

int DIV(long dividend, long divisor)
{
	if (dividend < divisor)
	{
		return 0;
	}
	long temp_divisor = divisor;
	long count = 1;
	while ((temp_divisor + temp_divisor) <= dividend)
	{
		count = count + count;
		temp_divisor = temp_divisor + temp_divisor;
	}
	return count + DIV(dividend - temp_divisor, divisor);
}


int divide(int dividend, int divisor)
{
	if (dividend == 0)
	{
		return 0;
	}
	if (divisor == 1)
	{
		return dividend;
	}
	if (divisor == -1)
	{
		if (dividend > INT_MIN)
		{
			return -dividend;
		}
		else
		{
			return INT_MAX;
		}
	}
	int flag = 1;
	long a = dividend;
	long b = divisor;
	if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0))
	{
		flag = -1;
	}
	a = a > 0 ? a : -a;
	b = b > 0 ? b : -b;
	long result = DIV(a, b);
	if (flag > 0)
	{
		return result > INT_MAX ? INT_MAX : result;
	}
	return -result;
}

int main()
{
	cout << divide(7, -3) << endl;
	system("pause");
	return 0;
}