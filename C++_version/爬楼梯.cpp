#include<iostream>
using namespace std;

class Solution
{
public:
	int climb_stairs(int n)
	{
		if (n <= 0)
		{
			return 0;
		}
		if (n == 1)
		{
			return 1;
		}
		if (n == 2)
		{
			return 2;
		}
		int number_of_one = 1;
		int number_of_two = 2;
		int result = 0;
		for (int i = 3; i <= n; i++)
		{
			result = number_of_two + number_of_one;
			number_of_one = number_of_two;
			number_of_two = result;
		}
		return result;
	}
};

int main()
{
	Solution answer;
	cout << answer.climb_stairs(3) << endl;
	system("pause");
	return 0;
}