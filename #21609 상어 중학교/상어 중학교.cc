#include <iostream>
#include <queue>
#define SIZE 21

using namespace std;

int N, M;
int map[SIZE][SIZE] = { 0 };
int used[SIZE][SIZE] = { 0 };
int dr[] = { -1,1,0,0 };
int dc[] = { 0,0,-1,1 };
int score = 0;

struct Pos
{
	int r, c;
};

struct BlockInfo
{
	int cnt, rainbow;
};

BlockInfo Bfs(Pos start)
{
	queue<Pos> q;
	q.push(start);

	int visited[SIZE][SIZE] = { 0 };
	visited[start.r][start.c] = 1;
	int label = map[start.r][start.c];
	BlockInfo b = { 1,0 };

	while (!q.empty())
	{
		Pos now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nr = now.r + dr[i];
			int nc = now.c + dc[i];

			if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
			if (map[nr][nc] > 0 && map[nr][nc] != label) continue;
			if (used[nr][nc] || visited[nr][nc]) continue;
			if (map[nr][nc] == -1 || map[nr][nc] == -2) continue;

			visited[nr][nc] = 1;
			if (map[nr][nc] > 0) used[nr][nc] = 1;
			b.cnt++;
			if (map[nr][nc] == 0)
			{
				b.rainbow++;
			}
			q.push({ nr, nc });


		}
	}

	return b;

}
void Remove(Pos start)
{
	queue<Pos> q;
	q.push(start);

	int visited[SIZE][SIZE] = { 0 };
	visited[start.r][start.c] = 1;
	int label = map[start.r][start.c];
	map[start.r][start.c] = -2;

	while (!q.empty())
	{
		Pos now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nr = now.r + dr[i];
			int nc = now.c + dc[i];

			if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
			if (map[nr][nc] > 0 && map[nr][nc] != label) continue;
			if (visited[nr][nc] || map[nr][nc] == -2) continue;
			if (map[nr][nc] == -1) continue;

			visited[nr][nc] = 1;
			map[nr][nc] = -2;
			q.push({ nr, nc });

		}
	}
}
int Find()
{
	BlockInfo info = { 0,0 };
	int flag = 1;
	Pos p = { -1,-1 };
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (used[i][j] || map[i][j] <= 0) continue;
			int rainbow_block = 0;
			used[i][j] = 1;
			BlockInfo cur_info = Bfs({ i, j });

			if (cur_info.cnt > info.cnt)
			{
				info.cnt = cur_info.cnt;
				info.rainbow = cur_info.rainbow;
				p.r = i;
				p.c = j;
			}
			else if (cur_info.cnt == info.cnt)
			{
				if (cur_info.rainbow > info.rainbow)
				{
					info.cnt = cur_info.cnt;
					info.rainbow = cur_info.rainbow;
					p.r = i;
					p.c = j;
				}
				else if (cur_info.rainbow == info.rainbow)
				{
					if (i > p.r)
					{
						info.cnt = cur_info.cnt;
						info.rainbow = cur_info.rainbow;
						p.r = i;
						p.c = j;
					}
					else if (i == p.r)
					{
						if (j > p.c)
						{
							info.cnt = cur_info.cnt;
							info.rainbow = cur_info.rainbow;
							p.r = i;
							p.c = j;
						}
					}
				}
			}

		}
	}

	if (info.cnt >= 2)
	{
		score += info.cnt * info.cnt;
		Remove(p);
		flag = 0;
	}

	return flag;

}



void Gravity()
{
	for (int c = 0; c < N; c++)
	{
		for (int r = N - 2; r >= 0; r--)
		{
			if (map[r][c] == -1 || map[r][c] == -2) continue;

			for (int nr = r + 1; nr <= N - 1; nr++)
			{

				if (map[nr][c] == -2)
				{
					map[nr][c] = map[nr - 1][c];
					map[nr - 1][c] = -2;
				}
				else
					break;
			}
		}
	}
}

void Rotate()
{
	int map2[SIZE][SIZE] = { 0 };

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			map2[i][j] = map[j][N - 1 - i];
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			map[i][j] = map2[i][j];
		}
	}
}

void Solve()
{
	while (true)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				used[i][j] = 0;
			}
		}
		int flag = Find();

		if (flag)
			break;

		int de = 1;

		Gravity();
		de = 1;
		Rotate();

		de = 1;
		Gravity();

		de = 1;

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
		for (int j = 0; j < N; j++)
		{
			cin >> map[i][j];
		}
	}

	Solve();
	cout << score;
}