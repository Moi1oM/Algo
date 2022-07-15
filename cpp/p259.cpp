#include<bits/stdc++.h>
#define INF 987654321
using namespace std;
int n,m,x,k;
int d[101][101];
int main(){
	cin>>n>>m;
	for(int i=0;i<101;i++){
		fill(d[i],d[i]+501,INF);
	}
	for(int a=1;a<=n;a++){
		for(int b=1;b<=n;b++){
			if(a==b)d[a][b]=0;
		}
	}
	for(int i=1;i<=m;i++){
		int a,b;
		cin>>a>>b;
		d[a][b]=1;
		d[b][a]=1;
	}
	cin>>k>>x;
	for(int k=1;k<=n;k++){
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
			}
		}
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(d[i][j]!=INF)cout<<d[i][j]<<" ";
			else cout<<"INF"<<" ";
		}
		cout<<endl;
	}
	return 0;
}
