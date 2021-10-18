#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	int different_path_2(vector<vector<int>>& matrix)
	{
		int m = matrix.size();
		int n = matrix[0].size();
		vector<int> f(n);
		f[0] = (matrix[0][0] == 0);
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (matrix[i][j] == 1)
				{
					f[j] = 0;
					continue;
				}
				if (j > 0 && matrix[i][j - 1] == 0)
				{
					f[j] += f[j - 1];
				}
			}
		}
		return f.back();
	}
};

int main()
{
	vector<vector<int>> matrix = { {0,1},{0,0} };
	Solution result;
	cout << result.different_path_2(matrix) << endl;
	system("pause");
	return 0;
}