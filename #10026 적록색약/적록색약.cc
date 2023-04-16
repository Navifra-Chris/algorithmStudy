#include <iostream>
#include <algorithm>
#include <cstring>
#define SIZE 101
using namespace std;

string map[SIZE];
int visited[SIZE][SIZE] = { 0 };
int N;

void Dfs(int r, int c)
{
    int dr[4] = { -1,1,0,0 };
    int dc[4] = { 0,0,-1,1 };

    for (int i = 0; i < 4; i++)
    {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
        if (visited[nr][nc] == 1) continue;
        if (map[nr][nc] != map[r][c]) continue;

        visited[nr][nc] = 1;
        Dfs(nr, nc);

    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int cnt=0;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> map[i];
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (visited[i][j] == 1) continue;

            cnt++;
            visited[i][j] = 1;
            Dfs(i, j);
        }
    }
    cout << cnt << " ";

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (map[i][j] == 'G')
                map[i][j] = 'R';
        }
    }
    
    memset(visited, 0, sizeof(visited));
    cnt = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (visited[i][j] == 1) continue;

            cnt++;
            visited[i][j] = 1;
            Dfs(i, j);
        }
    }

    cout << cnt;
}