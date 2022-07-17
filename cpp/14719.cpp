#include<bits/stdc++.h>
using namespace std;
int h,w;
int d[501];
int main(){
	int sum=0,waterCount=0;
	bool start=false;
	cin>>h>>w;//1~500
	for(int i=1;i<=w;i++)cin>>d[i];
	for(int j=1;j<=h;j++){
		for(int i=2;i<=w;i++){
			if(d[i]>=j){
				if(start){
					sum+=waterCount;
//					cout<<"sum: "<<sum<<" i: "<<i<<" j: "<<j<<" watercount: "<<waterCount<<endl;
					start=false;
				}
			}
			else{
				if(start){
					waterCount++;
//					cout<<waterCount<<" "<<"sum: "<<sum<<" i: "<<i<<" j: "<<j<<endl;
				}
				if(d[i-1]>=j){
					start=true;
					waterCount=1;
				}
				
			}
			if(i==w){
				start=false;
				waterCount=0;
			}
		}
	}
	cout<<sum;
	return 0;
}
