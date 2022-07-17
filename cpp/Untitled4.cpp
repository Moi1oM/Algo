#include<bits/stdc++.h>
using namespace std;

bool f(int num){
	int row=0;
	bool check=false;
	while(num>0){
		int one;
		one=num%10;
		if(one==6){
			row+=1;
		} else{
			row=0;
		}
		num/=10;
		if(row==3){
			check=true;
			break;
		}
	}
	return check;
	
}

int main(){
	int n,index=0,num=666;
	cin>>n;
	while(true){
		if(f(num)==true){
			index++;
			num++;
		}
		else num++;
		if(index==n)break;
	}
	cout<<num-1;
	return 0;
}
