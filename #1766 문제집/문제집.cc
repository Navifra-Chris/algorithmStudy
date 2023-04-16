#include <iostream>
#include <queue>
#define SIZE 32001

using namespace std;
int N, M;
priority_queue<int, vector<int>, greater<int>> pq;
vector<int> nextn[SIZE];
int prevn[SIZE] = { 0 };

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin.tie(NULL);

	cin >> N >> M;
	
	for (int i = 0; i < M; i++)
	{
		int from, to;
		cin >> from >> to;

		nextn[from].push_back(to);
		prevn[to] += 1;
	}

	for (int i = 1; i <= N; i++)
	{
		if (prevn[i] == 0)
		{
			pq.push(i);
		}
	}
	
	while (!pq.empty())
	{
		int de = 1;
		int n = pq.top();
		pq.pop();
		cout << n << " ";

		int size = nextn[n].size();
		for (int i = 0; i < size; i++)
		{
			int next = nextn[n][nextn[n].size()-1];
			nextn[n].pop_back();

			prevn[next]--;
			if (prevn[next] == 0)
				pq.push(next);
		}
	}

	
}