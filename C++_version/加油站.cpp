#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int gas_station(vector<int>& gas, vector<int>& cost)
	{
		int n = gas.size();
		int i = 0;
		while (i < n)
		{
			int current_sum = 0;
			int current_cost = 0;
			int cut = 0;
			while (cut < n)
			{
				current_sum += gas[i];
				current_cost += cost[i];
				if (current_cost > current_sum)
				{
					break;
				}
				else
				{
					++cut;
				}
			}
			if (cut == n)
			{
				return i;
			}
			else
			{
				i = i + cut + 1;
			}
		}
		return -1;
	}
};