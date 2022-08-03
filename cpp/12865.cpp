#include<bits/stdc++.h>
using namespace std;
int dp[101][100001]= { 0, };
//dp[i][j] = 처음부터 i번째까지의 물건을 살펴보고, 배낭의 용량이 j였을 때 배낭에 들어간 물건의 가치합의 최댓값
int n,k,w[101],v[101];
//dp[i][j]에는, dp[i-1][j] 의 값과 dp[i-1][j-w[i]]+v[i]
int main(){
	cin>>n>>k;
	for(int i=1;i<=n;i++){
		int a,b;
		cin>>a>>b;
		w[i]=a;
		v[i]=b;
		if(i==1)dp[i][a]=b;
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=k;j++){
			if(j>=w[i]){
				dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);
			}else{
				dp[i][j]=dp[i-1][j];
			}
		}
	}
	cout<<dp[n][k];
	return 0;
}
