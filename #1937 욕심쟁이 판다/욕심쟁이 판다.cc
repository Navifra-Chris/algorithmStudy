#include <iostream>
#include <algorithm>
#include <cstring>
#define SIZE 100001
using namespace std;

int N;
int map[501][501] = { 0 };
int dp[501][501] = { 0 };
int ans = 0;

int Dfs(int r, int c)
{
    if (dp[r][c] != 0)
        return dp[r][c];

    dp[r][c] = 1;

    int dr[4] = { -1,1,0,0 };
    int dc[4] = { 0,0,-1,1 };

    for (int i = 0; i < 4; i++)
    {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
        if (map[nr][nc] <= map[r][c]) continue;

        dp[r][c] = max(dp[r][c], Dfs(nr, nc)+1);
    }

    return dp[r][c];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> map[i][j];
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            ans = max(ans, Dfs(i, j));
        }
    }

    cout << ans;

}