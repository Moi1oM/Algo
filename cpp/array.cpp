#include<iostream>
#include<cmath>

using namespace std;

int main(){
	int luckyNums[20] = {4,8,15,16,23,42};
	
	luckyNums[0]=19;
	luckyNums[10]=90;
	
	cout << luckyNums[0]<<" "<< luckyNums[2]<<" "<<luckyNums[10];
	
	return 0;
}
