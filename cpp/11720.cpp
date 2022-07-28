#include<bits/stdc++.h>
#include<string>
#include<iostream>
using namespace std;

int main(){
	int n,cnt=0;
	char a[101];
	cin>>n;
	cin>>a;
	for(int i=0;i<n;i++){
		cnt=cnt+stoi(a[i]);
		cout<<cnt<<" "<<a[i]<<" "<<(int)a[i]<<endl;
	}
	cout<<cnt;
	return 0;
}
