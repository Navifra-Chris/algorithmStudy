#include <iostream>
#define SIZE 10

using namespace std;

int map[SIZE][SIZE] = { 0 };
int num_paper = 0;
int papers[6];
int min_depth = 21e8;

bool CanAttachPaper(int r, int c, int k)
{
	if (r + k > 10 || c + k > 10) return false;
	for (int i = r; i < r+k; i++)
	{
		for (int j = c; j < c+k; j++)
		{
			if (map[i][j] == 0)
				return false;
		}
	}

	return true;
}

void AttachPaper(int r, int c, int k)
{
	papers[k]--;
	num_paper -= k * k;
	for (int i = r; i < r+k; i++)
	{
		for (int j = c; j < c+k; j++)
		{
			map[i][j] = 0;
		}
	}
}

void DetachPaper(int r, int c, int k)
{
	papers[k]++;
	num_paper += k * k;
	for (int i = r; i < r + k; i++)
	{
		for (int j = c; j < c + k; j++)
		{
			map[i][j] = 1;
		}
	}
}

void Dfs(int depth, int r, int c)
{
	if (num_paper == 0)
	{
		min_depth = min(min_depth, depth);
		return;
	}

	for (int i = r; i < SIZE; i++)
	{
		for (int j = c; j < SIZE; j++)
		{
			if (map[i][j] == 0) continue;

			for (int k = 5; k >= 1; k--)
			{
				if (!CanAttachPaper(i, j, k)) continue;
				if (papers[k] <= 0) continue;

				AttachPaper(i, j, k);
				Dfs(depth + 1, r, j + k);
				DetachPaper(i, j, k);
			}

			return;
		}

		c = 0;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	for (int i = 0; i < SIZE; i++)
	{
		for (int j = 0; j < SIZE; j++)
		{
			cin >> map[i][j];
			if (map[i][j])
				num_paper++;
		}
	}
	for (int i = 1; i < 6; i++)
	{
		papers[i] = 5;
	}
	Dfs(0, 0, 0);
	
	if (min_depth == 21e8)
		cout << -1;
	else
		cout << min_depth;
}