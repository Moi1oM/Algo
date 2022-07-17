#include<bits/stdc++.h>
using namespace std;
vector<pair<int,pair<int,int> > >graph;
int parent[100001];
int n,m,result=0,maxCost=0;
int findParent(int x){
	if(parent[x]==x)return x;
	else return parent[x]=findParent(parent[x]);
}
void unionParent(int a,int b){
	a=findParent(a);
	b=findParent(b);
	if(a>b)parent[a]=b;
	else parent[b]=a;
}
int main(){
	cin>>n>>m;
	for(int i=0;i<m;i++){
		int a,b,c;
		cin>>a>>b>>c;
		graph.push_back({c,{a,b}});
	}
	for(int i=1;i<=n;i++)parent[i]=i;
	sort(graph.begin(),graph.end());
	for(int i=0;i<graph.size();i++){
		int cost=graph[i].first;
		int a=graph[i].second.first;
		int b=graph[i].second.second;
		if(findParent(a)!=findParent(b)){
			unionParent(a,b);
			result+=cost;
			if(maxCost<cost)maxCost=cost;
		}
	}
	cout<<result-maxCost;
	return 0;
}
