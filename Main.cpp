#include <iostream>
#include <cstring>
#include <queue>

#define MAX 1001

using namespace std;

int n,m;
int arr[MAX][MAX];
// 0: unbreaked , 1: breaked
int result[MAX][MAX][2];
// up, right, left, down
int dx[4] = {0,1,-1,0};
int dy[4] = {-1,0,0,1};

void BFS(int sx, int sy){
	queue<pair<pair<int,int>,int>> q;
	q.push({{sx,sy},0});
	result[sx][sy][0] = 1;

	while(!q.empty()){
		auto g = q.front();
		q.pop();

		// now x, now y, now breaked
		int nx = g.first.first;
		int ny = g.first.second;
		int nb = g.second;

		for(int i=0; i<4; i++){
			// out of bound
			if(nx+dx[i] < 0 || nx+dx[i] >= m) continue;
			if(ny+dy[i] < 0 || ny+dy[i] >= n) continue;
			// visited check
			if(result[nx+dx[i]][ny+dy[i]][nb] != 0 && result[nx+dx[i]][ny+dy[i]][nb] <= result[nx][ny][nb]+1) continue;

			// 0 -> 0,1
			if(arr[ny+dy[i]][nx+dx[i]] == 0){
				q.push({{nx+dx[i],ny+dy[i]},nb});
				result[nx+dx[i]][ny+dy[i]][nb] = result[nx][ny][nb]+1;
			}
			// 1 -> 0
			else{
				if(nb == 0){
					q.push({{nx+dx[i],ny+dy[i]},1});
					result[nx+dx[i]][ny+dy[i]][1] = result[nx][ny][0]+1;
				}
			}
		}
	}

	// result
	if(result[m-1][n-1][0] == INT32_MAX && result[m-1][n-1][1] == INT32_MAX) cout << "-1\n";
	else cout << min(result[m-1][n-1][0],result[m-1][n-1][1]);
}

int main(){
	// init
	memset(arr,-1,sizeof(arr));

	//input
	cin >> n >> m;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			scanf("%1d",&arr[i][j]);
			result[j][i][0] = INT32_MAX;
			result[j][i][1] = INT32_MAX;
		}
	}

	// cal
	BFS(0,0);
	return 0;
}
