#include<iostream>
#include<vector>
using namespace std;

class Solution
{
public:
	bool valid(vector<vector<char>>& board)
	{
		int row[9][9];
		int column[9][9];
		int subboxes[3][9][9];
		memset(row, 0, sizeof(row));
		memset(column, 0, sizeof(column));
		memset(subboxes, 0, sizeof(subboxes));
		for (int i = 0; i < 9; i++)
		{
			for (int j = 0; j < 9; j++)
			{
				char c = board[i][j];
				if (c != '.')
				{
					int index = c - '0' - 1;
					row[i][index]++;
					column[j][index]++;
					subboxes[i / 3][j / 3][index]++;
					if (row[i][index] > 1 || column[j][index] > 1 || subboxes[i / 3][j / 3][index] > 1)
					{
						return false;
					}
				}
			}
		}
		return true;

	}
};
