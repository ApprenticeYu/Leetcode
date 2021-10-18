#include<iostream>
using namespace std;

class Solution
{
public:
	int length_of_lastword(string S)
	{
		int length = 0;
		int index = S.size() - 1;
		while (S[index] == ' ')
		{
			index--;
		}
		while (index >= 0 && S[index] != ' ')
		{
			++length;
			--index;
		}
		return length;
	}
};

int main()
{
	Solution result;
	string S = "luffy is still joyboy";
	cout << result.length_of_lastword(S) << endl;
	system("pause");
	return 0;
}