#include<bits/stdc++.h>
#define INF 987654321
using namespace std;
int n,m,graph[501][501];

int main(){
	cin>>n>>m;
	for(int i=0;i<501;i++){
		fill(graph[i],graph[i]+501,INF);
	}
	for(int a=1;a<=n;a++){
		for(int b=1;b<=n;b++){
			if(a==b)graph[a][b]=0;
		}
	}
	for(int i=0;i<m;i++){
		int a,b,c;
		cin>>a>>b>>c;
		graph[a][b]=c;
	}
	for(int k=1;k<=n;k++){
		for(int a=1;a<=n;a++){
			for(int b=1;b<=n;b++){
				graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b]);
			}
		}
	}
	for(int a=1;a<=n;a++){
		for(int b=1;b<=n;b++){
			if(graph[a][b]==INF){
				cout<<"INF"<<' ';
			} else{
				cout<< graph[a][b]<< " ";
			}
		}
		cout<<endl;
	}
	return 0;
}
