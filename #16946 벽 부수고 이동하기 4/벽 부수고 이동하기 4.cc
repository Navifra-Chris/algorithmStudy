#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <string.h>
#include <set>
#define SIZE 1001

using namespace std;
int map[SIZE][SIZE] = { 0 };
int num[SIZE][SIZE] = { 0 };
int visited[SIZE][SIZE] = { 0 };
int N, M;
int label = 1;
int dr[] = { -1,1,0,0 };
int dc[] = { 0,0,-1,1 };
vector<int> group;


struct Pos
{
	int r, c;
};

void Labeling(int r, int c)
{
	queue<Pos> q;

	q.push({ r,c });
	visited[r][c] = label;

	int cnt = 1;

	while (!q.empty())
	{
		Pos now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nr = now.r + dr[i];
			int nc = now.c + dc[i];

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (visited[nr][nc] > 0) continue;
			if (map[nr][nc]) continue;

			cnt++;
			q.push({ nr, nc });
			visited[nr][nc] = label;
		}
 	}

	group.push_back(cnt);
}

void Solve(int r, int c)
{
	int cnt = 1;
	set<int> Search;
	for (int i = 0; i < 4; i++)
	{
		int nr = r + dr[i];
		int nc = c + dc[i];

		if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
		int label_idx = visited[nr][nc];

		if (Search.find(label_idx) != Search.end()) continue;

		Search.insert(label_idx);
		cnt += group[label_idx];
	}

	cout << cnt%10;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N >> M;
	group.push_back(0);
	for (int i = 0; i < N; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < M; j++)
		{
			map[i][j] = s[j] - '0';
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map[i][j] == 1 || visited[i][j] > 0) continue;

			Labeling(i, j);
			label++;
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map[i][j] == 0)
			{
				cout << 0;
				continue;
			}
			
			Solve(i, j);
		}
		cout << '\n';
	}
}