#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> one = {1,2,3,4,5};
    vector<int> two = {2,1,2,3,2,4,2,5};
    vector<int> three = {3,3,1,1,2,2,4,4,5,5};
    
    int score1 = 0;
    int score2 = 0;
    int score3 = 0;
    
    for(int i=0; i<answers.size(); i++){
        int ans = answers[i];
        
        if(ans == one[i % one.size()]){
            score1++;
        }
        if(ans == two[i % two.size()]){
            score2++;
        }
        if(ans == three[i % three.size()]){
            score3++;
        }
        
    }
    
    vector<int> scores = {score1, score2, score3};
    int max_elem = *max_element(scores.begin(), scores.end());
    
    for(int i=0; i<scores.size(); i++){
        if(scores[i] == max_elem){
            answer.push_back(i+1);
        }
    }
    
    return answer;
}