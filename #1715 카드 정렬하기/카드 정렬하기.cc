#include <iostream>
#include <queue>

using namespace std;

int N;
priority_queue<int, vector<int> , greater<int>> pq;

int main()
{
	cin >> N;
	int a;
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> a;
		pq.push(a);
	}

	while (pq.size() != 1)
	{
		int n1 = pq.top();
		pq.pop();
		int n2 = pq.top();
		pq.pop();

		pq.push(n1 + n2);
		ans += (n1 + n2);
	}

	cout << ans;

}