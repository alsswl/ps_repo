#include <bits/stdc++.h>

using namespace std;

#define MAX_NUM 1000

int n, m;
int vertex_cnt;

vector<int> gh[MAX_NUM+1];
bool visited[MAX_NUM+1];

void DFS(int v){
    for(int i = 0; i < gh[v].size(); i++){
        int curr_v = gh[v][i];
        if(!visited[curr_v]){
            visited[curr_v] = true;
            vertex_cnt++;
            DFS(curr_v);
        }
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m;
    
    int v1, v2;

    for(int i = 0; i < m; i++){
        cin >> v1 >> v2;
        gh[v1].push_back(v2);
        gh[v2].push_back(v1);
    }

    visited[1] = true;
    DFS(1);

    cout << vertex_cnt;
    
    return 0;
}
