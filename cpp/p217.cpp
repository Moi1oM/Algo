#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,d[30001];
	cin>>n;
	for(int i=1;i<=n;i++)d[i]=0;
	for(int i=2;i<=n+1;i++){
		d[i]=d[i-1]+1;
		if(i%2==0){
			d[i]=min(d[i],d[i/2]+1);
		}
		if(i%3==0){
			d[i]=min(d[i],d[i/3]+1);
		}
		if(i%5==0){
			d[i]=min(d[i],d[i/5]+1);
		}
	}
	cout<<d[n]<<endl;
	return 0;
}
