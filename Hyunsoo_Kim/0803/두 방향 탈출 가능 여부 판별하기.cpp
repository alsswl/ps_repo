#include <bits/stdc++.h>

using namespace std;

#define max_num 100
int n, m;
int grid[max_num][max_num];
bool visited[max_num][max_num];

int di[2]{0, 1};
int dj[2]{1, 0};
// 
bool InRange(int x, int y){
    return x >= 0 && x < n && y >= 0 && y < m;
}

bool check(int x, int y){
    if(!InRange(x, y)){
        return false;
    }

    if(visited[x][y] || grid[x][y] == 0){
        return false;
    }

    return true;
}

void DFS(int x, int y){
    for(int i = 0; i < 2; i++){
        int nx = x + di[i];
        int ny = y + dj[i];
        if(check(nx, ny)){
            visited[nx][ny] = true;
            DFS(nx, ny);
        }
    }
}


int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> grid[i][j];
        }
    }

    visited[0][0] = 1;
    DFS(0, 0);

    cout << visited[n-1][m-1];

    return 0;
}
