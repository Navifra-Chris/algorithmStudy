#include <iostream>

using namespace std;

int N, M;

struct Pos
{
	int r, c;
};

Pos robot;
int d;
int map[51][51] = { 0 };
int visited[51][51] = { 0 };
int dr[] = { -1, 0, 1, 0 };
int dc[] = { 0, 1, 0, -1 };
int cnt = 1;

bool CanMove(int r, int c)
{
	if (map[r][c] == 0 && visited[r][c] == 0)
		return true;

	return false;
}

bool OutOfMap(int r, int c)
{
	if (r < 0 || r >= N || c < 0 || c >= M)
		return true;

	return false;
}

void Solve()
{
	while (1)
	{
		int flag = 0;
		

		for (int i = 0; i < 4; i++)
		{
			d = (d + 3) % 4;
			int nr = robot.r + dr[d];
			int nc = robot.c + dc[d];

			if (OutOfMap(nr, nc)) continue;

			if (CanMove(nr, nc))
			{
				robot.r = nr;
				robot.c = nc;
				flag = 1;
				visited[robot.r][robot.c] = 1;
				cnt++;
				break;
			}
		}

		if (flag == 0)
		{
			int nr = robot.r - dr[d];
			int nc = robot.c - dc[d];

			if (OutOfMap(nr, nc)) continue;

			if (map[nr][nc] == 0)
			{
				robot.r = nr;
				robot.c = nc;
				flag = 1;
			}
		}
		
		if (flag == 0)
			break;
	}

}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;
	cin >> robot.r >> robot.c >> d;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
		}
	}
	visited[robot.r][robot.c] = 1;
	Solve();
	cout << cnt;
}