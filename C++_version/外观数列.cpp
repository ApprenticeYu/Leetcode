#include<iostream>
using namespace std;

class Solution
{
public:
	string count(int n)
	{
		if (n <= 0)
		{
			return "";
		}
		string arr = "1";
		if (n == 1)
		{
			return arr;
		}
		for (int i = 1; i < n; i++)
		{
			char word = arr[0];
			int num = 1;
			string temp = "";
			for (int j = 1; j < arr.size(); j++)
			{
				if (arr[j] == word)
				{
					++num;
				}
				else
				{
					char temp2 = num + '0';
					temp += temp2;
					temp += word;
					word = arr[j];
					num = 1;
				}
			}
			char temp2 = num + '0';
			temp += temp2;
			temp += word;
			arr = temp;
		}
		return arr;
	}
};

int main()
{
	Solution result;
	cout << result.count(1) << endl;
	system("pause");
	return 0;
}