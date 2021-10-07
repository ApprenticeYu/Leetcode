#include<iostream>
using namespace std;

class Solution
{
public:
	string Ztransform(string S, int num)
	{

		int n = S.size();
		int gap = 2 * num - 2;
		string ret;
		for (int i = 0; i < num; i++)
		{
			for (int j = 0; j + i < n; j += gap)
			{
				ret += S[i + j];
				if ((i != 0) && (i != num - 1) && (j + gap - i < n))
				{

					ret += S[j + gap - i];
				}

			}

		}
		return ret;
	}

};

int main()
{
	Solution result;
	cout << result.Ztransform("PAYPALISHIRING", 4) << endl;
	system("pause");
	return 0;

}