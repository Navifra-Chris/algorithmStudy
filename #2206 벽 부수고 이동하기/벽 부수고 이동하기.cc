#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#define SIZE 1001

using namespace std;

int N, M;
string map[SIZE];
int visited[2][SIZE][SIZE] = { 0 };
int ans = -1;

struct Pos
{
	int r, c;
	int flag;
};

void Bfs(Pos start)
{
	queue<Pos> q;
	q.push(start);
	visited[0][start.r][start.c] = 1;
	visited[1][start.r][start.c] = 1;

	int dr[] = { -1,1,0,0 };
	int dc[] = { 0,0,-1,1 };


	while (!q.empty())
	{
		Pos now = q.front();
		q.pop();

		if (now.r == N - 1 && now.c == M - 1)
		{
			int d0 = visited[0][now.r][now.c];
			int d1 = visited[1][now.r][now.c];
			if (d0 == 0 && d1 == 0) return;
			else if (d0 == 0)
				ans = d1;
			else if (d1 == 0)
				ans = d0;
			else
				ans = min(d0, d1);
		}
			
			
		for (size_t i = 0; i < 4; i++)
		{
			int nr = now.r + dr[i];
			int nc = now.c + dc[i];

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (visited[now.flag][nr][nc]) continue;

			if (map[nr][nc] == '1' && now.flag == 0)
			{
				if (visited[1][nr][nc] > 0) continue;

				visited[1][nr][nc] = visited[0][now.r][now.c] + 1;
				q.push({ nr,nc,1 });
			}
			else if (map[nr][nc] == '0')
			{
				visited[now.flag][nr][nc] = visited[now.flag][now.r][now.c] + 1;
				q.push({ nr,nc,now.flag });
			}


		}
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie();
	cout.tie();


	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		string s;
		cin >> map[i];
	}

	Bfs({ 0,0,0 });

	cout << ans;
}