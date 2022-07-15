#include<bits/stdc++.h>
using namespace std;
vector<int> arr;
int d[100];
int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int x;
		cin >> x;
		arr.push_back(x);
	}
	d[0]=arr[0];
	d[1]=arr[1];
	for(int i=2;i<n;i++){
		d[i]=max(d[i-2]+arr[i],d[i-1]);
	}
//	for(int i=0;i<n;i++)cout<<d[i]<<" ";
	cout<<d[n-1]<<endl;
	return 0;
}
