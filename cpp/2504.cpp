#include<bits/stdc++.h>
using namespace std;

int main(){
	bool isgood=true;
	char *a[30],b[30];
	int bidx=0,ridx=0,aidx=0;
	cin>>a;
//	cout<<strlen(a);
	for(int i=0;i<strlen(a);i++){
		b[bidx]=a[i];
		if(a[i]=="(")ridx++;
		if(a[i]=="{")aidx++;
		if(a[i]==")")ridx--;
		if(a[i]=="}")aidx++;
		if(ridx<0 || aidx<0){
			isgood=false;
			break;
		}
	}
	cout<<isgood;
	return 0;
}
