#include<bits/stdc++.h>
using namespace std;
int v,e;
vector<int> graph[100001];
int degree[100001];

void topology(){
	vector<int> result;
	queue<int> q;
	for(int i=1;i<=v;i++){
		if(degree[i]==0)q.push(i);
	}
	while(!q.empty()){
		int now=q.front();
		q.pop();
		result.push_back(now);
		for(int i=0;i<graph[now].size();i++){
			degree[graph[now][i]]--;
			if(degree[graph[now][i]]==0){
				q.push(graph[now][i]);
			}
		}
	}
	for (int i = 0; i < result.size(); i++) {
        cout << result[i] << ' ';
    }
}

int main(){
	cin>>v>>e;
	for(int i=0;i<e;i++){
		int a,b;
		cin>>a>>b;
		graph[a].push_back(b);
		degree[b]++;
	}
	topology();
	return 0;
}  
