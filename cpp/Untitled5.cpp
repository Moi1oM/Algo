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
	int start=0,end,mid,nums;
	end=maxlen;
	while(true){
		if(start>=end)break;
		nums=0;
		mid=(start+end)/2;
		for(int i=0;i<k;i++){
			nums+=d[i]/mid;
		}
		if(nums>n)start=mid+1;
		else if (nums<n)end=mid-1;
		else start=mid+1;
	}
	mid=(start+end)/2;
	cout<<mid;
	return 0;
}
