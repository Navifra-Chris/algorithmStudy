#include <iostream>
#include <queue>
#include <algorithm>

#define SIZE 301

using namespace std;
int N, M;
int map[SIZE][SIZE] = { 0 };
int mapAfter[SIZE][SIZE] = { 0 };
int visited[SIZE][SIZE] = { 0 };
int non_zero = 0;
int ans = 0;
bool is_split = false;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

int GetZero(int r, int c)
{
	int cnt = 0;

	for (int i = 0; i < 4; i++)
	{
		int nr = r + dr[i];
		int nc = c + dc[i];

		if (map[nr][nc] <= 0)
			cnt++;

	}

	return cnt;
}

void Melt()
{
	non_zero = 0;
	for (int i = 1; i < N-1; i++)
	{
		for (int j = 1; j < M-1; j++)
		{
			if (map[i][j] == 0) continue;

			int cnt_zero = GetZero(i, j);
			mapAfter[i][j] = map[i][j] - cnt_zero;
			if (mapAfter[i][j] > 0)
				non_zero++;
		}
	}

	copy(&mapAfter[0][0], &mapAfter[0][0] + SIZE * SIZE, &map[0][0]);
}

struct Pos
{
	int r, c;
};

bool Bfs(int r, int c)
{
	queue<Pos> q;
	q.push({ r,c });
	int cnt = 1;
	fill(visited[0], visited[SIZE], 0);
	visited[r][c] = 1;
	
	while (!q.empty())
	{
		Pos now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nr = now.r + dr[i];
			int nc = now.c + dc[i];

			if (map[nr][nc] <= 0 || visited[nr][nc] == 1) continue;

			visited[nr][nc] = 1;
			q.push({ nr, nc });
			cnt++;
		}
	}

	if (non_zero != cnt)
		return true;
	else
		return false;
}

void CheckSplit()
{
	for (int i = 1; i < N-1; i++)
	{
		for (int j = 1; j < M-1; j++)
		{
			if (map[i][j] <= 0) continue;
			is_split = Bfs(i, j);
			return;
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
		}
	}
	int ans = 0;
	while (true)
	{
		Melt();
		ans++;
		if (non_zero == 0) break;
		CheckSplit();
		if (is_split)
		{
			cout << ans;
			return 0;
		}
	}
	cout << 0;
}