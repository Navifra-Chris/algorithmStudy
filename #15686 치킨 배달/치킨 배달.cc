#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
struct Pos
{
	int r, c;
};

vector<Pos> chicken;
vector<Pos> home;
int selected[14] = { 0 };
vector<vector<int>> dist_info;

int map[51][51] = { 0 };
int min_dist = 21e8;

int CalDist()
{
	int sum_dist = 0;
	for (int i = 0; i < home.size(); i++)
	{
		int md = 21e8;
		for (int j = 0; j < chicken.size(); j++)
		{
			if (selected[j] == 0) continue;

			md = min(md, dist_info[i][j]);
		}
		sum_dist += md;
	}

	return sum_dist;
}

void func(int depth, int now)
{
	if (depth == M)
	{
		min_dist = min(min_dist, CalDist());
	}

	for (size_t i = now; i < chicken.size(); i++)
	{
		selected[i] = 1;
		func(depth + 1, i + 1);
		selected[i] = 0;
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin.tie(NULL);
	
	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == 2)
				chicken.push_back({ i,j });
			else if (map[i][j] == 1)
				home.push_back({ i,j });
		}
	}
	
	dist_info = vector<vector<int>>(home.size(), vector<int>(chicken.size()));
	for (int i = 0; i < home.size(); i++)
	{
		for (int j = 0; j < chicken.size(); j++)
		{	
			int dist = abs(home[i].r - chicken[j].r) + abs(home[i].c - chicken[j].c);

			dist_info[i][j] = dist;

		}

	}

	func(0, 0);

	cout << min_dist;
}