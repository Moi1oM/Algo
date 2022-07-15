#include <bits/stdc++.h>
using namespace std;
int d[100];
int fibo(int num){
	if(d[num-1]!=0){
		return d[num-1];
	}
	else {
		d[num-1]=fibo(num-2)+fibo(num-1);
		return d[num-1];
	}
}

int main(){
	int n;
	for(int i=0;i<100;i++)d[i]=0;
	d[0]=1;
	d[1]=1;
	for(int i=1;i<=100;i++){
		if(fibo(i)<2100000000)cout<<fibo(i)<<endl;
		else{
			cout<<i;
			break;
		}
	}
	return 0;
}
