#include<iostream>
using namespace std;

class Solution
{
public:
	string SUM(string S1, string S2)
	{
		reverse(S1.begin(), S1.end());
		reverse(S2.begin(), S2.end());
		string ans;
		int n = max(S1.size(), S2.size());
		int carry = 0;
		for (int i = 0; i < n; i++)
		{
			carry += i < S1.size() ? (S1[i] == '1') : 0;
			carry += i < S2.size() ? (S2[i] == '1') : 0;
			ans.push_back((carry % 2 == 1) ? '1' : '0');
			carry /= 2;
		}
		if (carry)
		{
			ans.push_back('1');
		}
		reverse(ans.begin(), ans.end());
		return ans;
	}
};

int main()
{
	string S1 = "1010";
	string S2 = "1011";
	Solution result;
	cout << result.SUM(S1, S2) << endl;
	system("pause");
	return 0;
}