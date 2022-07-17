#include<bits/stdc++.h>
using namespace std;
int n,num[12],s[4];
int mmmax=-1234567890,mmmin=1234567890;
void f(int a,int b,int c,int d,int depth,int res){
	int nexres;
//	cout<<a<<" "<<b<<" "<<c<<" "<<d<<" depth: "<<depth<<" res: "<<res<<" "<<endl;
	if(depth==n){
		if(mmmax<res)mmmax=res;
		if(mmmin>res)mmmin=res;
		return ;
	}
	if(a>0){
		nexres=res+num[depth+1];
		f(a-1,b,c,d,depth+1,nexres);
	}
	if(b>0){
		nexres=res-num[depth+1];
		f(a,b-1,c,d,depth+1,nexres);
	}
	if(c>0){
		nexres=res*num[depth+1];
		f(a,b,c-1,d,depth+1,nexres);
	}
	if(d>0){
		nexres=res/num[depth+1];
		f(a,b,c,d-1,depth+1,nexres);
	}
	return;
}

int main(){
	cin>>n;
	for(int i=1;i<=n;i++)cin>>num[i];
	cin>>s[0]>>s[1]>>s[2]>>s[3];
	f(s[0],s[1],s[2],s[3],1,num[1]);
	cout<<mmmax<<"\n"<<mmmin;
	return 0;
}
