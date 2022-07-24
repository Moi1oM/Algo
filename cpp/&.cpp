#include <bits/stdc++.h>

using namespace std;

int n,d,p,q;
double cache[51][101];
int connected[51][51], deg[51];

double search2(int here, int days){
	if(days==d) return (here == q ? 1.0 : 0.0);
	double& ret = cache[here][days];
	if(ret > -0.5) return ret;
	ret = 0.0;
	for(int there=0;there<n;++there){
		if (connected[here][there])
			ret+= search2(there, days+1)/deg[here];
	}
	return ret;
}

int main(){
	cin>>n>>d>>p;
	cin>>q;
	for(int i=1;i<=50;i++){
		for(int j=1;j<=100;j++)cache[i][j]=-1.0;
	}
	for(int i=1;i<=n;i++)deg[i]=0;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			int a;
			cin>>a;
			connected[i][j]=a;
			if(a==1){
				deg[i]++;
				deg[j]++;
			}
		}
	}
	cout<<search2(p,1);
	return 0;
}
