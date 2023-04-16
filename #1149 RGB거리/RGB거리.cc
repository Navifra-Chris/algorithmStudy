#include <iostream>
#include <vector>
#define SIZE 1001

using namespace std;

int N;
int arr[SIZE][3] = { 0 };
int dp[SIZE][3] = {0};


void Solve()
{
	for (int i = 1; i <= N; i++)
	{
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i - 1][0];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i - 1][1];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i - 1][2];
	}

	cout << min(dp[N][0], min(dp[N][1], dp[N][2]));
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			cin >> arr[i][j];
		}
	}

	Solve();

}