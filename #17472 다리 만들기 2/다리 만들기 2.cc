#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

struct Pos
{
    int r, c;
};

struct Bridge
{
    Pos p;
    int dir, from, to, len;
};

int N, M;
int map[11][11] = { 0 };
vector<Pos> lands;
queue<Bridge> bq;
vector<Bridge> bridges;

int visited[11][11] = { 0 };
int land_cnt = 1;
int dr[] = { 1, 0, -1, 0 };
int dc[] = { 0, 1, 0, -1 };
int connected_info[7][7] = { 0 };
int visited_land[7] = { 0 };
int min_len = 21e8;

bool IsOutOfRange(int r, int c)
{
    if (r < 0 || r >= N || c < 0 || c >= M)
        return true;
    else
        return false;
}

void Dfs(int r, int c)
{
    for (int i = 0; i < 4; i++)
    {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (IsOutOfRange(nr, nc)) continue;
        if (visited[nr][nc] > 0) continue;
        if (map[nr][nc] == 0)
        {
            if (i == 2 || i == 3) continue;
            bq.push({ nr, nc, i, land_cnt, 0, 0 });
        }
        else
        {
            visited[nr][nc] = land_cnt;
            Dfs(nr, nc);
        }
    }
}

void VerifyBridge()
{
    int size = bq.size();
    for (int i = 0; i < size; i++)
    {
        Bridge bridge = bq.front();
        bq.pop();

        int nr = bridge.p.r;
        int nc = bridge.p.c;

        int aa = 1;
        aa++;

        while (true)
        {
            nr = nr + dr[bridge.dir];
            nc = nc + dc[bridge.dir];

            if (IsOutOfRange(nr, nc)) break;

            if (map[nr][nc] > 0)
            {
                if (bridge.from == visited[nr][nc]) break;

                int len = abs(nr - bridge.p.r) + abs(nc - bridge.p.c);
                if (len < 2) break;

                bridge.to = visited[nr][nc];
                bridge.len = len;
                bridges.push_back(bridge);
                break;
            }
        }

    }
}

void DfsConnected(int now)
{
    visited_land[now] = 1;
    for (int next = 1; next < land_cnt; next++)
    {
        if (connected_info[now][next] == 0) continue;
        if (visited_land[next] == 1) continue;

        DfsConnected(next);
    }
}
bool IsConnected(vector<int> check_bridge)
{
    memset(visited_land, 0, sizeof(visited_land));
    memset(connected_info, 0, sizeof(connected_info));

    for (int i = 0; i < bridges.size(); i++)
    {
        if (check_bridge[i] == 0) continue;

        int from = bridges[i].from;
        int to = bridges[i].to;
        connected_info[from][to] = 1;
        connected_info[to][from] = 1;

    }
    
    DfsConnected(1);

    for (int i = 1; i < land_cnt; i++)
    {
        if (visited_land[i] == 0)
            return false;
    }
    return true;
}

int SumLen(vector<int> check_bridge)
{
    int sum = 0;
    for (int i = 0; i < check_bridge.size(); i++)
    {
        if (check_bridge[i] == 0) continue;

        sum += bridges[i].len;
    }
    return sum;
}

void Solution(int depth, vector<int> &check_bridge)
{
    if (depth == bridges.size())
    {
        if (count(check_bridge.begin(), check_bridge.end(), 1) == land_cnt-2)
        {
            if (IsConnected(check_bridge))
            {
                int len = SumLen(check_bridge);
                min_len = min(min_len, len);
            }
        }
        
        return;
    }

    for (int i = 0; i < 2; i++)
    {
        check_bridge[depth] = i;
        Solution(depth + 1, check_bridge);

    }


}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> map[i][j];
            if (map[i][j])
                lands.push_back({ i,j });
        }
    }

    // marking land
    for (int i = 0; i < lands.size(); i++)
    {
        int r = lands[i].r;
        int c = lands[i].c;

        if (visited[r][c] > 0) continue;
        visited[r][c] = land_cnt;
        Dfs(r, c);
        land_cnt++;
    }

    VerifyBridge();

    vector<int> check_bridge(bridges.size(), 0);
    Solution(0, check_bridge);

    if (min_len == 21e8)
        cout << -1;
    else
        cout << min_len;

}