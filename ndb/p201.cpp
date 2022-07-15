#include <iostream>
#include <stdio.h>
#include <conio.h>

using namespace std;

int main(){
	int n,m,sum,maxlen=0,minlen=100000,start,end,mid;
	int d[10000];
//	scanf("%d %d",&n,&m);
//	cout<<"enter : ";
	cin >>n >>m;
	for(int i=0;i<n;i++){
		scanf("%d",&d[i]);
		if(d[i]>maxlen)maxlen=d[i];
		if(d[i]<minlen)minlen=d[i];
	}
	start=0;
	end=maxlen;
	while(true){
		if(start==end)break;
		sum=0;
		mid=(start+end)/2;
		for(int i=0;i<n;i++){
			if(d[i]>mid)sum+=d[i]-mid;
		}
		if(sum>m){
			start=mid+1;
		} else if(sum<m){
			end=mid-1;
		}else{
			start=mid;
			break;
		}
	}
	cout<<start<<endl;
//	getch();
	return 0;
}
