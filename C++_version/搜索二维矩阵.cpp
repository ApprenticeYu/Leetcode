#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	bool search_matrix(vector<vector<int>>& matrix,int target)
	{
		int m = matrix.size();
		int n = matrix[0].size();
		int left = 0;
		int right = m * n - 1;
		while (left <= right)
		{
			int mid = left + ((right - left) >> 1);
			int value = matrix[mid / n][mid % n];
			if (value < target)
			{
				left = mid + 1;
			}
			else if (value > target)
			{
				right = mid - 1;
			}
			else
			{
				return true;
			}
		}
		return false;
	}
};

int main()
{
	Solution result;
	vector<vector<int>> matrix = { {1, 3, 5, 7},{10, 11, 16, 20},{23, 30, 34, 60 } };
	cout << result.search_matrix(matrix, 13) << endl;
	system("pause");
	return 0;
}