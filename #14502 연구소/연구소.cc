#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <unordered_map>
#define SIZE 1001

using namespace std;

struct Pos
{
	int r, c;
};

int N, M;
int map[8][8] = { 0, };
queue<Pos> q;
int max_safe_zone;

void CalSafeZone()
{
	int tmp_map[8][8] = { 0, };
	copy(&map[0][0], &map[0][0] + 64, &tmp_map[0][0]);
	queue<Pos> tmp_q = q;

	while (!tmp_q.empty())
	{
		Pos now = tmp_q.front();
		tmp_q.pop();

		int dr[4] = { -1,1,0,0 };
		int dc[4] = { 0,0,-1,1 };

		for (int i = 0; i < 4; i++)
		{
			int nr = now.r + dr[i];
			int nc = now.c + dc[i];

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (tmp_map[nr][nc] == 1 || tmp_map[nr][nc] == 2) continue;

			tmp_map[nr][nc] = 2;
			tmp_q.push({ nr,nc });

		}
	}
	int safe_zone_cnt = 0;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (tmp_map[i][j] == 0)
				safe_zone_cnt++;
		}
	}

	if (safe_zone_cnt == 32)
	{
		int asd = 0;
		asd += 1;
	}
	max_safe_zone = max(max_safe_zone, safe_zone_cnt);
}

void SelectWall(int cnt)
{
	if (cnt == 3)
	{
		CalSafeZone();
		return;
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map[i][j] == 0)
			{
				map[i][j] = 1;
				SelectWall(cnt + 1);
				map[i][j] = 0;
			}
		}
	}

}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == 2)
				q.push({ i,j });
		}
	}

	SelectWall(0);

	cout << max_safe_zone;
	return 0;
}