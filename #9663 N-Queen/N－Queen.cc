#include <iostream>

using namespace std;

int row[15] = { 0 };
int N;
int ans = 0;

bool Check(int depth)
{
	for (int i = 0; i < depth; i++)
	{
		if ((row[i] == row[depth]) || (abs(i - depth) == abs(row[i] - row[depth])))
			
			return true;

	}
		return false;
}
void func(int depth)
{
	if (depth == N)
	{
		ans++;
		return;
	}

	for (int col = 0; col < N; col++)
	{
		row[depth] = col;

		if (Check(depth)) continue;

		func(depth + 1);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin.tie(NULL);

	cin >> N;

	func(0);

	cout << ans;
}
