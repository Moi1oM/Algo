#include<bits/stdc++.h>
using namespace std;
vector<int> value;
int d[10001];
int main(){
	int n,m;
	cin>>n>>m;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		value.push_back(x);
	}
	for(int i=1;i<=m;i++)d[i]=10001;
	d[0]=0;
	for(int i=0;i<n;i++)d[value[i]]=1;
	for(int i=0;i<n;i++){
		for(int j=value[i];j<=m;j++){
			if(d[j-value[i]]!=10001){
				d[j]=min(d[j-value[i]]+1,d[j]);
			}
		}
	}
	for(int i=0;i<=m;i++)cout<<d[i]<<" ";
//	if(d[m]==10001)cout<<-1;
//	else cout<<d[m];
	return 0;
}
