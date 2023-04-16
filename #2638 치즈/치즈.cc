#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <string.h>

#define SIZE 101
using namespace std;
struct Pos
{
    int r, c;
};

int N, M;
int map[SIZE][SIZE] = { 0 };
int isOut[SIZE][SIZE] = { 0 };

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

void MarkingOut(int r, int c)
{
    queue<Pos> q;

    q.push({ r,c });
    isOut[r][c] = 1;

    while (!q.empty())
    {
        Pos now = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nr = now.r + dr[i];
            int nc = now.c + dc[i];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (isOut[nr][nc] == 1) continue;
            if (map[nr][nc] == 1) continue;

            q.push({ nr, nc });
            isOut[nr][nc] = 1;
        }
    }
}

bool CanRemove(int r, int c)
{
    int cnt = 0;
    for (int i = 0; i < 4; i++)
    {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
        if (isOut[nr][nc] == 0) continue;

        cnt++;
    }

    if (cnt >= 2) return true;
    else return false;
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
        }
    }

    MarkingOut(0, 0);

    bool is_cheese = true;
    int tmp_map[SIZE][SIZE] = { 0 };
    int cnt = 0;
    while (is_cheese)
    {
        is_cheese = false;
        copy(&map[0][0], &map[0][0] + (SIZE * SIZE), &tmp_map[0][0]);

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (map[i][j] == 1 && CanRemove(i, j))
                {
                    tmp_map[i][j] = 0;
                    is_cheese = true;
                }
            }
        }

        copy(&tmp_map[0][0], &tmp_map[0][0] + (SIZE * SIZE), &map[0][0]);
        memset(isOut, 0, sizeof(isOut));
        MarkingOut(0, 0);
        if (is_cheese)
            cnt++;
    }


    cout << cnt;
}