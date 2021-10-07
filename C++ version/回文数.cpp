#include <iostream>
using namespace std;

class solution
{
public:
	bool ispalindrome(int num)
	{
		int reverse_num = 0;
		if (num < 0 || (num % 10 == 0 && num != 0))
		{

			return false;
		}
		while (num > reverse_num)
		{

			reverse_num = reverse_num * 10 + num % 10;
			num /= 10;
		}
		return reverse_num == num || num == reverse_num / 10;
	}

};

int main()
{

	solution result;
	cout << result.ispalindrome(-101) << endl;
	system("pause");
	return 0;
}