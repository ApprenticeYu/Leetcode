#include<iostream>
using namespace std;

int max_profit(const int* data, int length)
{
	if (data == nullptr || length < 2)
	{
		return 0;
	}
	int min_value = data[0];
	int max_profit = data[1] - min_value;
	for (int i = 2; i < length; i++)
	{
		if (data[i - 1] < min_value)
		{
			min_value = data[i - 1];
		}
		if (data[i] - min_value > max_profit)
		{
			max_profit = data[i] - min_value;
		}
	}
	return max_profit;
}