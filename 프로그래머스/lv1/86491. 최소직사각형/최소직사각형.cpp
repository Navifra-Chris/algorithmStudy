#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    
    vector<int> bigs;
    vector<int> smalls;
    
    for(int i; i<sizes.size(); i++){
        int r = sizes[i][0];
        int c = sizes[i][1];
        
        bigs.push_back(max(r, c));
        smalls.push_back(min(r, c));
        
    }
    
    int big = *max_element(bigs.begin(), bigs.end());
    int small = *max_element(smalls.begin(), smalls.end());
    
    answer = big*small;
    return answer;
}