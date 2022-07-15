#include<bits/stdc++.h>
#define INF 987654321
using namespace std;
int n,m,c;
vector<pair<int,int> >graph[30001];
int d[30001];

void f(int n){
	priority_queue<pair<int,int> >pq;
	pq.push({0,n});
	d[n]=0;
	while(!pq.empty()){
		int dist=-pq.top().first;
		int node=pq.top().second;
		pq.pop();
		if(d[node]<dist)continue;
		for(int i=0;i<graph[node].size();i++){
			int cost=dist+graph[node][i].second;
			
			if(cost<d[graph[node][i].first]){
				d[graph[node][i].first]=cost;
				pq.push(make_pair(-cost,graph[node][i].first));
			}
		}
	}
}

int main(){
	cin>>n>>m>>c;
	for(int i=0;i<m;i++){
		int a,b,c;
		cin>>a>>b>>c;
		graph[a].push_back({b,c});
	}
	fill(d,d+30001,INF);
	f(c);
	int count=0,maxtime=0;
	for(int i=1;i<=n;i++){
		if(d[i]>=0){
			count++;
			if(maxtime<d[i])maxtime=d[i];	
		}
	}
	cout<<count-1<<" "<<maxtime;
	return 0;
}
