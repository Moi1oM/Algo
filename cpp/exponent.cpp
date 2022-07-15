#include<iostream>
#include<cmath>
using namespace std;

int power(int baseNum, int poweNum){
	int result=1;
	for(int i =0; i<poweNum;i++){
		result=result*baseNum;
	}
	return result;
}

int main(){
	cout<<power(2,3);
	return 0;
}
