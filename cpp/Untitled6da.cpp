#include<bits/stdc++.h>
using namespace std;
int d[10000];
int main(){
	int k,n,maxlen=0;
	cin>>k>>n;
	for(int i=0;i<k;i++){
		int a;
		cin>>a;
		d[i]=a;
		if(maxlen<a)maxlen=a;
	}
	int count,i;
	for(i=maxlen;i>=1;i--){
		count=0;
		for(int j=0;j<k;j++){
			count+=d[j]/i;
		}
		if(count==n)break;
	}
	cout<<i;
	return 0;
}
