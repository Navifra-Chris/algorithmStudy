#include <iostream>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;
int N, M;
int map[10001][501] = { 0 };
int dr[3] = { -1, 0, 1 };
int cnt = 0;

bool Dfs(int r, int c)
{
	map[r][c] = 1;
	if (c == M - 1)
	{
		cnt += 1;
		return true;
	}


	for (int i = 0; i < 3; i++)
	{
		int nr = r + dr[i];
		int nc = c + 1;

		if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
		if (map[nr][nc] == 1) continue;

		
		if (Dfs(nr, nc))
			return true;
	}

	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < M; j++)
		{
			char ch = s[j];
			
			if (ch == '.')
				map[i][j] = 0;
			else
				map[i][j] = 1;
		}
	}

	for (int i = 0; i < N; i++)
	{
		map[i][0] = 1;
		Dfs(i, 0);
	}

	cout << cnt;

	return 0;


}