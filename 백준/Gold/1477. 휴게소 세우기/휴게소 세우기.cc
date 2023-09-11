#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, M, L;
vector<int>v;
priority_queue<int>pq;
int maxi = -1;

void init() {
    cin >> N >> M >> L;
    for (int i = 1; i <= N; i++) {
        int rest;
        cin >> rest;
        v.push_back(rest);
    }
    v.push_back(0);
    v.push_back(L);
    sort(v.begin(), v.end());
    //for (int i = 1; i < v.size(); i++) {
    //    int len = v[i] - v[i - 1];
    //    if (len > maxi) maxi = len;
    //}
}

bool checking(int mid) {
    int now = 0;
    int next = 1;
    int cnt = 0;

    while (next <= N + 1) {
        if (v[next] - now <= mid) {
            now = v[next];
            next++;
        }
        else {
            now += mid;
            cnt++;
        }
    }

    if (cnt > M) return false;
    else return true;
}

int bs() {
    int right = L;
    int left = 1;
    int ans = (right + left) / 2;

    while (left <= right) {
        int mid = (right + left) / 2;

        if (checking(mid)) {
            ans = mid;
            right = mid - 1;
        }
        else left = mid + 1;
    }
    return ans;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();
    int ans = bs();
    cout << ans;

    return 0;
}