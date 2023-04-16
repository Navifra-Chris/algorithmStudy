#include <iostream>
#include <algorithm>
#include <cstring>
#define SIZE 501
using namespace std;

int map[SIZE][SIZE] = { 0 };
int visited[SIZE][SIZE] = { 0 };
int M, N;
int cnt = 0;

int Dfs(int r, int c)
{
    if (r == N - 1 && c == M - 1)
        return 1;

    if (visited[r][c] != -1)
        return visited[r][c];

    visited[r][c] = 0;

    int dr[4] = { -1,1,0,0 };
    int dc[4] = { 0,0,-1,1 };

    for (int i = 0; i < 4; i++)
    {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
        if (map[nr][nc] >= map[r][c]) continue;

        visited[r][c] += Dfs(nr, nc);
    }

    return visited[r][c];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> map[i][j];
            visited[i][j] = -1;
        }
    }
    
    Dfs(0, 0);
    
    cout << visited[0][0];
}