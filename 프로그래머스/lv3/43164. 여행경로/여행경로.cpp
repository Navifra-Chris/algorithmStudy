#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
int len;
vector<int> visited(10001, 0);
vector<string> final_path;

void dfs(int depth, string from, vector<string> path, vector<vector<string>> tickets){
    path.push_back(from);
    // string to = "";
    
    if(depth == len){
        if(final_path.empty() || path < final_path){
            final_path = path;
        }
    }
    
    for(int i=0; i<tickets.size(); i++){
        if(visited[i] == 1) continue;
        // cout << tickets[i][0] << " " << tickets[i][1] << endl;
        
        if(tickets[i][0] == from){
            string to = tickets[i][1];
            visited[i] = 1;
            dfs(depth+1, to, path, tickets);
            visited[i] = 0;
        }
    }
    
    
    
    
    
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    len = tickets.size();
    vector<string> path;
    sort(tickets.begin(), tickets.end(),
         [](const auto& a, const auto& b) {
                  if (a[0] == b[0]) {
                      return a[1] < b[1];
                  } else {
                      return a[0] < b[0];
                  }
              });
    
    // for(int i=0; i<tickets.size(); i++){
    //     cout << tickets[i][0] << " " << tickets[i][1] << '\n';
    // }
    dfs(0, "ICN", path, tickets);
    
    answer = final_path;
    
    
    return answer;
}