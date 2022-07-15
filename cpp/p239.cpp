#include<bits/stdc++.h>
#define INF 987654321
using namespace std;
int distance[10001],d[10001];
bool visited[10001];
int n,m,start;
vector<pair<int,int> > graph[10001];

int getSmallestNode(){
	int min_value=INF, index=0;
	for(int i=1;i<=n;i++){
		if(d[i]<min_value&&!visited[i]){
			min_value=d[i];
			index=i;
		}
	}
	return index;
}

dijkstra(int start){
	d[start]=0;
	visited[start]=true;
	for(int j=0;j<graph[start].size();j++){
		d[graph[start][j].first]=graph[start][j].second;
	}
	for(int i=0;i<n-1;i++){
		int now=getSmallestNode();
		visited[now]=true;
		for(int j=0;j<graph[now].size();j++){
			int cost=d[now]+graph[now][j].second;
			if(cost<d[graph[now][j].first]){
				d[graph[now][j].first]=cost;
			}
		}
	}
}

int main(){
	cin>>n>>m>>start;
	for(int i=0;i<m;i++){
		int from,to,length;
		cin>>from>>to>>length;
		graph[from].push_back({to,length});
	}
	fill_n(d,10001,INF);
	dijkstra(start);
	for(int i=1;i<=n;i++){
		if(d[i]==INF){
			cout<<"INF"<<endl;
		}
		else{
			cout<<d[i]<<endl;
		}
	}
	
	return 0;
}
