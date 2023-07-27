#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <climits>
#include <numeric>  // <- 추가

using namespace std;

vector<vector<int>> board;
vector<vector<int>> rotations;
vector<bool> used;
int ans;

vector<vector<int>> copyBoard(vector<vector<int>>& orig) {
    vector<vector<int>> copy = orig;
    return copy;
}

vector<vector<int>> rotate(vector<int>& selected, vector<vector<int>>& rotation_board) {
    int r = selected[0];
    int c = selected[1];
    int s = selected[2];

    vector<vector<int>> ori_board = copyBoard(rotation_board);

    int start_r = r - s - 1;
    int start_c = c - s - 1;

    int end_r = r + s;
    int end_c = c + s;

    int size = s * 2 + 1;

    for (int i = 0, vr = start_r; vr < end_r; i++, vr++) {
        for (int j = 0, vc = start_c; vc < end_c; j++, vc++) {
            if (i <= j && i + j < size - 1) {    // right
                rotation_board[vr][vc + 1] = ori_board[vr][vc];
            }
            else if (i < j && i + j >= size - 1) {  // down
                rotation_board[vr + 1][vc] = ori_board[vr][vc];
            }
            else if (i >= j && i + j > size - 1) {  // left
                rotation_board[vr][vc - 1] = ori_board[vr][vc];
            }
            else if (i > j && i + j <= size - 1) {  // up
                rotation_board[vr - 1][vc] = ori_board[vr][vc];
            }
        }
    }
    return rotation_board;
}

void permutation(vector<vector<int>>& selected) {
    if (selected.size() == rotations.size()) {
        vector<vector<int>> rotation_board = copyBoard(board);
        for (int i = 0; i < rotations.size(); i++) {
            rotation_board = rotate(selected[i], rotation_board);
        }
        int value = INT_MAX;
        for (vector<int>& line : rotation_board) {
            value = min(value, accumulate(line.begin(), line.end(), 0));
        }
        ans = min(ans, value);
        return;
    }

    for (int i = 0; i < rotations.size(); i++) {
        if (!used[i]) {
            used[i] = true;
            selected.push_back(rotations[i]);
            permutation(selected);
            selected.pop_back();
            used[i] = false;
        }
    }
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    board = vector<vector<int>>(n, vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> board[i][j];

    rotations = vector<vector<int>>(k, vector<int>(3));
    for (int i = 0; i < k; i++)
        for (int j = 0; j < 3; j++)
            cin >> rotations[i][j];

    used = vector<bool>(k, false);

    ans = numeric_limits<int>::max();

    vector<vector<int>> selected;
    permutation(selected);

    cout << ans;
    return 0;
}
