#include<bits/stdc++.h>
using namespace std;

bool f(int num){
	int num2=0,num1;
	num1=num;
	while(num>0){
		num2*=10;
		num2+=num%10;
		num/=10;
	}
	if(num1==num2)return true;
	else return false;
}

int main(){
	int a;
	while(true){
		cin>>a;
		if(a==0)break;
		if(f(a)==true)cout<<"yes"<<endl;
		else cout<<"no"<<endl;
	}
	return 0;
}
