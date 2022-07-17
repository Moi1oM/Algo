#include<bits/stdc++.h>
using namespace std;
int times[501];
int degree[501];
vector<int> topology[501];
int n;

void f(){
	vector<int> result(501);
	for(int i=1;i<=n;i++)result[i]=times[i];
	queue<int> q;
	for(int i=1;i<=n;i++){
		if(degree[i]==0){
			q.push(i);
		}
	}
	while(!q.empty()){
		int now=q.front();
		q.pop();
		
		for(int i=0;i<topology[now].size();i++){
			result[topology[now][i]]=max(result[topology[now][i]],result[now]+times[topology[now][i]]);
			degree[topology[now][i]]--;
			if(degree[topology[now][i]]==0 )q.push(topology[now][i]);
		}
	}
	for(int i=1;i<=n;i++)cout<<result[i]<<endl;
}

int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		int pre;
		cin>>times[i];
		while(true){
			cin>>pre;
			if(pre==-1)break;
			topology[pre].push_back(i);
			degree[i]++;
		}
	}
	f();
	for(int i=1;i<=n;i++){
		for(int j=0;j<topology[i].size();j++){
			cout<<topology[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
