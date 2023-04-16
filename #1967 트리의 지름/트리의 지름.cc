#include <iostream>
#include <queue>
#include <algorithm>
#include <string.h>

#define SIZE 10001
using namespace std;
int N, M;
vector<pair<int, int>> tree[SIZE];
int max_dist = 0;
int max_node = 0;
int visited[SIZE] = { 0, };


void Dfs(int now, int dist)
{
	if (visited[now] == 1)
		return;

	visited[now] = 1;
	if (dist > max_dist)
	{
		max_dist = dist;
		max_node = now;
	}

	for (int i = 0; i < tree[now].size(); i++)
	{
		int next = tree[now][i].first;
		int next_d = tree[now][i].second;

		Dfs(next, dist + next_d);
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N-1; i++)
	{
		int parent, child, cost;
		cin >> parent >> child >> cost;
		tree[parent].push_back(pair<int, int>(child, cost));
		tree[child].push_back(pair<int, int>(parent, cost));
	}

	Dfs(1, 0);
	memset(visited, 0, sizeof(visited));
	max_dist = 0;
	Dfs(max_node, 0);

	cout << max_dist;
}