#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int T, k;
int cnt;
int removed[1000001] = { 0, };
struct Node {
    int value, idx;
};
bool operator < (Node A, Node B) {
    if (A.value < B.value) return true;
    else if (A.value > B.value) return false;
    else if (A.idx < B.idx) return true;
    else return false;
}
priority_queue<Node>bigfirst;
struct Edge {
    int value, idx;
};
bool operator < (Edge A, Edge B) {
    if (A.value > B.value) return true;
    else if (A.value < B.value) return false;
    else if (A.idx > B.idx) return true;
    else return false;
}
priority_queue<Edge>smallfirst;

void init() {
    cin >> k;
    for (int i = 1; i <= k; i++) {
        char x;
        int n;
        cin >> x >> n;
        if (x == 'I') {
            bigfirst.push({ n,i });
            smallfirst.push({ n,i });
            cnt++;
        }
        if (x == 'D') {
            if (n == 1) {
                int flag = 0;
                while (flag == 0 && !bigfirst.empty()) {
                    Node now = bigfirst.top();
                    bigfirst.pop();
                    if (removed[now.idx] == 0) {
                        removed[now.idx] = 1;
                        flag = 1;
                        cnt--;
                    }
                }
            }
            else if (n == -1) {
                int flag = 0;
                while (flag == 0 && !smallfirst.empty()) {
                    Edge now = smallfirst.top();
                    smallfirst.pop();
                    if (removed[now.idx] == 0) {
                        removed[now.idx] = 1;
                        flag = 1;
                        cnt--;
                    }
                }
            }
        }
    }
}

void printing() {
    if (cnt <= 0) {
        cout << "EMPTY\n";
        return;
    }
    else {
        while (1) {
            if (removed[bigfirst.top().idx]) bigfirst.pop();
            else {
                cout << bigfirst.top().value << " ";
                break;
            }
        }
        while (1) {
            if (removed[smallfirst.top().idx]) smallfirst.pop();
            else {
                cout << smallfirst.top().value << "\n";
                return;
            }
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cnt = 0;
        memset(removed, 0, sizeof(removed));
        while (!bigfirst.empty()) bigfirst.pop();
        while (!smallfirst.empty()) smallfirst.pop();
        init();
        printing();
    }

    return 0;
}